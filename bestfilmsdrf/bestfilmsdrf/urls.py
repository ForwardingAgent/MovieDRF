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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from films.views import MovieAPIList, MovieAPIUpdate, MovieAPIDetailView  # 8 заменили на MovieViewSet
from films.views import MovieViewSet
from rest_framework import routers

router = routers.SimpleRouter()  # 8
router.register(r'movie', MovieViewSet)  # movie для формирования маршрута в urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),  # 8 include - включаем все маршруты которые находятся в urls, они генерируются в router.register(r'movie', MovieViewSet)
    # выше формируется http://127.....api/v1/movie/  movie из router
    # path('api/v1/movielist/', MovieViewSet.as_view({'get': 'list'})),  #  list и put в документации
    # path('api/v1/movielist/<int:pk>/', MovieViewSet.as_view({'put': 'update'})),
]

if settings.DEBUG:  # DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # навести на static и подсказка покажет: какие импорты добавить и что передать в ф-ию static
