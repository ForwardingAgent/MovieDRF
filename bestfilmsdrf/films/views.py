from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Movie, Category
from .serializers import MovieSerializer
# views ОБРАБОТКА ТОЛЬКО ЗАПРОСОВ А serializer ЗА ОБРАБОТКУ ДАННЫХ (чтение изменение удаление)


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'  # клиент может поменять кол-во записей в выдаче на странице вместо 3, но не более значения max_page_size
    max_page_size = 10000

class MovieAPIList(generics.ListCreateAPIView):
        queryset = Movie.objects.all()
        serializer_class = MovieSerializer
        permission_classes = (IsAuthenticatedOrReadOnly, )
        # pagination_class = LargeResultsSetPagination  # свой класс пагинации (см. выше)


class MovieAPIUpdate(generics.RetrieveUpdateAPIView):
        queryset = Movie.objects.all()
        serializer_class = MovieSerializer
        # permission_classes = (IsOwnerOrReadOnly, )  # собственный, из permissions.py
        permission_classes = (IsAuthenticated, )
        authentication_classes = (TokenAuthentication, )  # по какому варианту из сеттингс авторизироваться по сессии или по токену


class MovieAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
        queryset = Movie.objects.all()
        serializer_class = MovieSerializer
        permission_classes = (IsAdminUser, )



# 10
# class MovieViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#     # queryset = Movie.objects.all() убираем тк в get_queryset есть, но в urls надо прописать basename=Movie
#     serializer_class = MovieSerializer
# 
#     def get_queryset(self):
#         # return Movie.objects.all()[:3]  # 3 записи из списка
#         pk = self.kwargs.get('pk')  # для списка или одной записи
#         if not pk:
#             return Movie.objects.all()[:3]
#         else:
#             return Movie.objects.filter(pk=pk)
# 
#     @action(methods=['get'], detail=True)  # 9 (выводим категории) methods с какими методами работаем | detail=False возвращает список если True то одна запись
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)  # по pk выбираем категорию
#         return Response({'cats': cats.name})  # по cats.name берем отдельную категорию .../api/v1/movie/4(1,2..)/category/

# 9
# class MovieViewSet(viewsets.ModelViewSet)  # ReadOnlyModelViewSet - не дает удалять и менять | в 9 заменили на mixins 
    # queryset = Movie.objects.all()
    # serializer_class = MovieSerializer

# 8
# class MovieAPIList(generics.ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
# 
# 
# class MovieAPIUpdate(generics.UpdateAPIView):
#     queryset = Movie.objects.all()  # ленивый запрос, выбирается только одна конкретная запись
#     serializer_class = MovieSerializer
# 
# 
# class MovieAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Movie.objects.all()  # ленивый запрос, выбирается только одна конкретная запись
#     serializer_class = MovieSerializer


# 7 
# class MovieAPIView(APIView):
#     def get(self, request):
#         # lst = Movie.objects.all().values() - values возвращает словарь
#         lst = Movie.objects.all()
#         return Response({'posts': MovieSerializer(lst, many=True).data})  # 4/15.0 lst - весь список статей | many - то что MovieSerializer надо обработать не одну запись а список записей и сл-но выдавать тоже список | data - словарь из табл. Movie 
#     
#     def post(self, request):
#         serializer = MovieSerializer(data=request.data)  # преобразовывает входные данные в объект сериализатор 
#         serializer.is_valid(raise_exception=True)  #  проверяем и если ошибка, то отправляем обратно какие поля обязательны, а не 404
#         serializer.save()  # прихоит из serializers из create и тут сохраняется в бд
#         return Response({'post': serializer.data})  # data ссылается на новый созданный объект serializer, его не надо создавать MovieSerializer(post_new)
#         
# 
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)  # проверяем наличие ключа
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#         
#         try:
#             instance = Movie.objects.get(pk=pk)  # проверяем наличие значения
#         except:
#             return Response({"error": "Object does not exists"})
#         
#         serializer = MovieSerializer(data=request.data, instance=instance)  # преобразовывает входные данные в объект сериализатор 
#         serializer.is_valid(raise_exception=True)  #  проверяем и если ошибка, то отправляем обратно какие поля обязательны, а не 404
#         serializer.save() # при создании 2 параметров MovieSerializer(data=request.data, instance=instance) автоматом вызывается def update(instance, data) в serializer.py
#         return Response({'post': serializer.data})  # data ссылается на новый созданный объект serializer, его не надо создавать MovieSerializer(post_new)
# 
# 
#     def delete(self, request, *args, **kwargs):
#             pk = kwargs.get('pk', None)  # проверяем наличие ключа
#             if not pk:
#                 return Response({"error": "Method DELETE not allowed"})
#             
#             try:
#                 instance = Movie.objects.get(pk=pk)  # проверяем наличие значения
#                 instance.delete()
#             except:
#                 return Response({"error": "Object does not exists"})
#             
#             return Response({'post': "delete post" + str(pk)})  
# 

        # post_new = Movie.objects.create(
        #   title=request.data['title'],
        #   content= и тд...
        # )
        # return Response({'post': MovieSerializer(post_new).data})  # model_to_dict - преобразовывает объект в словарь
