from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from . import views

app_name = "main"
urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload_image, name='upload_image'),
    path('upload_private', views.upload_image_private, name='upload_image_private'),
    path('register', views.register, name="register"),
    path('logout', views.logout_account, name="logout"),
    path('login', views.login_account, name="login"),
    path('private', views.private, name="private"),
    path('remove/<int:pk>', views.delete_image, name='image_delete'),
    path('search', views.search, name='search'),
    path('clear', views.clear, name='clear'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
