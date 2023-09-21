from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from .models import Movie
from .serializers import MovieSerializer


# ОБРАБОТКА ТОЛЬКО ЗАПРОСОВ А serializer ЗА ОБРАБОТКУ ДАННЫХ (чтение изменение удаление)


class MovieViewSet(viewsets.ModelViewSet):  # ReadOnlyModelViewSet - не дает удалять и менять
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


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
