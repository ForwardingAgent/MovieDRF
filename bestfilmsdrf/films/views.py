from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics, viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from .models import Movie, Category
from .serializers import MovieSerializer, CategorySerializer

from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter, OpenApiResponse, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
# views ОБРАБОТКА ТОЛЬКО ЗАПРОСОВ А serializer ЗА ОБРАБОТКУ ДАННЫХ (чтение изменение удаление)


class LargeResultsSetPagination(PageNumberPagination):
        # page_size = 5
        page_size_query_param = "page_size" # 'page_size/записей на странице'  # клиент может поменять кол-во записей в выдаче на странице вместо 3, но не более значения max_page_size
        max_page_size = 1000

        def get_paginated_response(self, data):
                return Response({
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
                'count': self.page.paginator.count,
                'pages': self.page.paginator.num_pages,
                'results': data
                })

@extend_schema_view(
        get=extend_schema(description="Here you can get a list of Movies. 'page' - Номер страницы из списка; 'page_size' - Количество фильмов на странице", summary="Get Movie", tags=["Movie"]),
        post=extend_schema(description="Here you can add a Movie", summary="Post Movie", tags=["Movie"]),
)

class MovieAPIList(generics.ListCreateAPIView):
        queryset = Movie.objects.all()
        serializer_class = MovieSerializer
        permission_classes = (IsAuthenticated, )
        pagination_class = LargeResultsSetPagination  # свой класс пагинации (см. выше)


@extend_schema_view(
        get=extend_schema(description="Here you can get a list of Categories", summary="Get Categories", tags=["Categories"]),
        post=extend_schema(description="Here you can add a Category", summary="Post Category", tags=["Categories"]),
)

class CategoryAPIList(generics.ListCreateAPIView):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer
        # permission_classes = (IsOwnerOrReadOnly, )  # собственный, из permissions.py
        permission_classes = (IsAuthenticated, )
        pagination_class = LargeResultsSetPagination  # свой класс пагинации (см. выше)

@extend_schema_view(
        get=extend_schema(description="Here you can get a list of Categories", summary="Get Categories", tags=["Categories"]),
        put=extend_schema(description="Here you can update a Category", summary="Put a Category", tags=["Categories"]),
        patch=extend_schema(description="Here you can change a Category", summary="Patch a Category", tags=["Categories"]),
)

class CategoryAPIUpdate(generics.RetrieveUpdateAPIView):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer
        # permission_classes = (IsOwnerOrReadOnly, )  # собственный, из permissions.py
        permission_classes = (IsAuthenticated, )
        pagination_class = LargeResultsSetPagination  # свой класс пагинации (см. выше)

@extend_schema_view(
        get=extend_schema(summary="Get Movie!", tags=["Movie"]),
        put=extend_schema(summary="Put Movie!", tags=["Movie"]),
        patch=extend_schema(summary="Patch Movie!", tags=["Movie"]),
)

class MovieAPIUpdate(generics.RetrieveUpdateAPIView):
        queryset = Movie.objects.all()
        serializer_class = MovieSerializer
        # permission_classes = (IsOwnerOrReadOnly, )  # собственный, из permissions.py
        permission_classes = (IsAuthenticated, )
        #authentication_classes = (TokenAuthentication, )  # по какому варианту из сеттингс авторизироваться по сессии или по токену

# @extend_schema_view(
#         get=extend_schema(description="Тут описание", summary="Get Movie", tags=["Movie"]),
#         put=extend_schema(summary="Put Movie", tags=["Movie"]),
#         patch=extend_schema(summary="Patch Movie", tags=["Movie"]),
#         delete=extend_schema(summary="Delete Movie", tags=["Movie"]),
# )
# class MovieAPIDestroy(generics.RetrieveUpdateDestroyAPIView): один класс для 4 методов
#         queryset = Movie.objects.all()
#         serializer_class = MovieSerializer
#         permission_classes = (IsAdminUser, )



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
# 8 class MovieViewSet(viewsets.ModelViewSet)  # ModelViewSet - дает возможность ч/з роутеры полный CRUD (см. из чего состоит)) | ReadOnlyModelViewSet - не дает удалять и менять | в 9 заменили на mixins 
    # queryset = Movie.objects.all()
    # serializer_class = MovieSerializer

# 8
# 7 class MovieAPIList(generics.ListCreateAPIView):  MovieAPIList c ListCreateAPIView теперь и отдает по GET и добавляет по POST
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
# 
# 
# class MovieAPIUpdate(generics.UpdateAPIView):
#     queryset = Movie.objects.all()  # ленивый запрос, выбирается только одна конкретная запись которая приходит с адреса path('api/v1/movie/<int:pk>/', MovieAPIUpdate.as_view()),
#     serializer_class = MovieSerializer
# 
# 
# 7 ниже один вариант класса для всех функций CRUD с url: path('api/v1/moviedetail/<int:pk>/', MovieAPIDetailView.as_view())
# class MovieAPIDetailView(generics.RetrieveUpdateDestroyAPIView):  RetrieveUpdateDestroyAPIView все функции CRUD
#     queryset = Movie.objects.all()  # ленивый запрос, выбирается только одна конкретная запись которая приходит с адреса 'api/v1/moviedetail/<int:pk>'
#     serializer_class = MovieSerializer


# 7 
# class MovieAPIView(APIView):  APIView базовый класс, во главе всех классов представления DRF
#     def get(self, request):
#         # lst = Movie.objects.all().values() - values возвращает словарь | в 4/15.0 убрал
#         lst = Movie.objects.all()
#         return Response({'posts': MovieSerializer(lst, many=True).data})  # 4/15.0 lst - весь список статей 
#         # many - то что MovieSerializer надо обработать не одну запись а список записей и сл-но выдавать тоже список | data - словарь из табл. Movie 
#     
#     def post(self, request):
#         serializer = MovieSerializer(data=request.data)  # преобразовывает входные данные в объект сериализатор 
#         serializer.is_valid(raise_exception=True)  #  проверяем (с полями сериалайзера, которые он взял из модели) и если ошибка, то отправляем обратно какие поля обязательны, а не 404
#         serializer.save()  # приходит из serializers из create и тут сохраняется в бд
#         return Response({'post': serializer.data})  # data ссылается на новый созданный объект serializer, его не надо создавать MovieSerializer(post_new)
#         
# 
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)  # проверяем наличие ключа если есть-берем, если нет-возвращаем None
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#         
#         try:
#             instance = Movie.objects.get(pk=pk)  # проверяем наличие значения (записи)
#         except:
#             return Response({"error": "Object does not exists"})
#         
#         serializer = MovieSerializer(data=request.data, instance=instance)  # преобразовывает входные данные в объект сериализатор 
#         serializer.is_valid(raise_exception=True)  #  проверяем и если ошибка, то отправляем обратно какие поля обязательны, а не 404
#         serializer.save() # при создании 2 параметров MovieSerializer(data=request.data, instance=instance) автоматом вызывается def update(instance, data) в serializer.py тк есть instance и data
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
        # def post(self, request):
        #   post_new = Movie.objects.create(
        #     title=request.data['title'],
        #     content=request.data['content'],
        #     cat_id=request.data['cat_id']
        #   )
        #   return Response({'post': MovieSerializer(post_new).data})  # model_to_dict - преобразовывает объект в словарь
