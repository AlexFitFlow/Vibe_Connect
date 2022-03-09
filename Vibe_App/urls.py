from django.urls import path     
from . import views

urlpatterns = [
    path('', views.main),
    path('sign_page', views.sign_page),
    path('login', views.login),
    path('register', views.register),
    path('create_page', views.create_page),
    path('main', views.main),
    path('home', views.home),
    path('upload', views.upload_page),
    path('logout', views.logout),
    path('create_album', views.create_album),
    path('account_edit', views.account_edit),
    path('update_user/<int:user_id>', views.update_user),
    path('post_message', views.post_message),
    path('add_comment/<int:the_id>', views.post_comment),
    path('image_message/<int:image_id>', views.image_message),
    path('user_profile/<int:id>', views.profile),
    path('like/<int:id>', views.add_like),
    path('like2/<int:id>', views.add_image_like),
    path('delete_post/<int:id>', views.delete_post),
    path('delete_image/<int:id>', views.delete_image),
    path('upload_image', views.upload_image),
    path('upload_image2', views.upload_image2),
    path('about_us', views.about_us),
    path('create_album', views.create_album),
    path('create_album_photo', views.create_album_photo),
    path('delete_album/<int:id>', views.delete_album),
    path('delete_album_photo/<int:id>', views.delete_album_photo)
]