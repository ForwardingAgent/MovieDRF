import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Movie
# ОБРАБОТКА ЗАПРОСОВ В views.py А serializer ЗА ОБРАБОТКУ ДАННЫХ (чтение изменение удаление)


class MovieSerializer(serializers.ModelSerializer):  # ModelSerializer сериал-р который работает с моделями (берет из БД преобразует в json и отправляет в ответ на запросу)
    class Meta:
        model = Movie
        fields = ("id", "title", "content", "cat")  # если все поля из бд вернуть то fields = "__all__"

# 6
# class MovieSerializer(serializers.Serializer): 
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


# 4
# class MovieModel:  - используем для примера вместо класса в model.py
#     def __init__(self, title, content) -> None:
#         self.title = title
#         self.content = content

# class MovieSerializer(serializers.Serializer): 
#     title = serializers.CharField(max_length=255) - атрибуты (title, content...) должны быть с теми же именами что и локальные св-ва в объектах класса MovieModel
#     content = serializers.CharField()
#
# def encode():
#     model = MovieModel('Зеленая миля', 'Content: Зеленая миля')
#     model_serial = MovieSerializer(model) - пропускаем объект model через сериалайзер | отрабатывает особенный класс который вместо атрибутов (title, content в MovieSerializer) создает data (словарь dict) состоящую из свойств локальных атрибутов 
#     print(model_serial.data, type(model_serial.data), sep='\n')  - data это сериализованные данные
#     json = JSONRenderer().render(model_serial.data)  - JSONRenderer преобразует объект сериализации model_serial в БАЙТОВУЮ json-строку
#     print(json)
# 
# def decode():
#     stream = io.BytesIO(b'{"title":"Shrek", "content":"Content: Shrek"}')  - типа запрос от клиента
#     data = JSONParser().parse(stream)  -  создаем объект класса JSONParser
#     serializer = MovieSerializer(data=data)  -  именованный параметр data
#     serializer.is_valid()
#     print(serializer.validated_data)