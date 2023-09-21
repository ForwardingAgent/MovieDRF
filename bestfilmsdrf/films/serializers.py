import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Movie


# ОБРАБОТКА ЗАПРОСОВ В views.py А serializer ЗА ОБРАБОТКУ ДАННЫХ (чтение изменение удаление)

class MovieSerializer(serializers.ModelSerializer):  # ModelSerializer сериал-р который работает с моделями (берет из БД преобразует в json и отправляет в ответ на запросу)
    class Meta:
        model = Movie
        fields = ("title", "content", "cat")  # если все поля из бд вернуть то fields = "__all__"

# class MovieSerializer(serializers.Serializer):  # ModelSerializer сериал-р который работает с моделями (берет из БД преобразует в json и отправляет в ответ на запросу)
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
# 
#     def create(self, validated_data):  # validated_data приходит из view из post после is_valid
#         return Movie.objects.create(**validated_data)  # передаем в сreate раcпакованый в словарь validated_data 
# 
#     def update(self, instance, validated_data):  # instanse объект (ссылка на объект) Movie
#         instance.title = validated_data.get('title', instance.title)  # в get берем нужный ключ, а если нет то возвращаем instance.title | dict.get(key[, default]) если нет key возвращаем default
#         instance.content = validated_data.get('content', instance.content)
#         instance.time_update = validated_data.get('time_update', instance.time_update)
#         instance.is_published = validated_data.get('is_published', instance.is_published)
#         instance.cat_id = validated_data.get('cat_id', instance.cat_id)
#         instance.save()
#         return instance
#     
#     def delete(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)  # в get берем нужный ключ, а если нет то возвращаем instance.title | dict.get(key[, default]) если нет key возвращаем default
#         instance.content = validated_data.get('content', instance.content)
#         instance.time_update = validated_data.get('time_update', instance.time_update)
#         instance.is_published = validated_data.get('is_published', instance.is_published)
#         instance.cat_id = validated_data.get('cat_id', instance.cat_id)
#         instance.delete()
#         return instance


# class MovieModel:
#     def __init__(self, title, content) -> None:
#         self.title = title
#         self.content = content
#
# def encode():
#     model = MovieModel('Зеленая миля', 'Content: Зеленая миля')
#     model_serial = MovieSerializer(model)
#     print(model_serial.data, type(model_serial.data), sep='\n')
#     json = JSONRenderer().render(model_serial.data)  # JSONRenderer преобразует объект сериализации в json-строку
#     print(json)
# 
# def decode():
#     stream = io.BytesIO(b'{"title":"Shrek", "content":"Content: Shrek"}')
#     data = JSONParser().parse(stream)
#     serializer = MovieSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)