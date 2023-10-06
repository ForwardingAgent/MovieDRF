"""bestfilmsdrf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
# from films.views import MovieAPIList, MovieAPIUpdate, MovieAPIDetailView  # 8 заменили на MovieViewSet
from films.views import MovieAPIList, MovieAPIUpdate,  CategoryAPIList, CategoryAPIUpdate # MovieAPIDestroy,  # MovieViewSet
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

# 10
# router = routers.DefaultRouter()  # 8
# router.register(r'movie', MovieViewSet, basename='movie')  # movie для формирования маршрута в urls
# print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),  # подключена авторизация на основе сессий, появилось login в DRF
    path('api/v1/movie/', MovieAPIList.as_view()),
    path('api/v1/movie/<int:pk>/', MovieAPIUpdate.as_view()),
    path('api/v1/category/', CategoryAPIList.as_view()),
    path('api/v1/category/<int:pk>/', CategoryAPIUpdate.as_view()),
    # path('api/v1/moviedelete/<int:pk>/', MovieAPIDestroy.as_view()),
    # path(r'api/v1/auth/', include('djoser.urls')),  # djoser было, сам 2 (base, jwt) добавил ниже
    path(r'api/v1/auth/', include('djoser.urls.base')),  # djoser 
    path(r'api/v1/auth/', include('djoser.urls.jwt')),  # djoser 
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # djoser авторизация по token | какие варианты работы c user это есть в djoser-Base Endpoints

    # 10 
    # 8 path('api/v1/', include(router.urls)),  # 8 include - включаем все маршруты которые находятся в urls, они генерируются в router.register(r'movie', MovieViewSet)
    # выше формируется http://127.....api/v1/movie/  movie из router и этот маршрут выдат и список всех записей и ниже форму для добавления новой
    # можно добавить число http://127.....api/v1/movie/9/ и выдаст одну статью и возможность ее изменить и удалить
    # 8 path('api/v1/movielist/', MovieViewSet.as_view({'get': 'list'})),  #  list и put в документации viewsets actions
    # 8 path('api/v1/movielist/<int:pk>/', MovieViewSet.as_view({'put': 'update'})),
]
urlpatterns += [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

if settings.DEBUG:  # DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # навести на static и подсказка покажет: какие импорты добавить и что передать в ф-ию static
