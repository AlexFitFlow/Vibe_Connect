from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Wall_Message, Comment, Post, Content, Album, Album_Photo, Comment2
import bcrypt
from django.shortcuts import  render


def main(request):
    return render(request, 'main.html')

def sign_page(request):
    return render(request, 'sign_in.html')

def create_page(request):
    return render(request, 'create_account.html')

def about_us(request):
    return render(request, 'about_us.html')

def home(request):
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'post_count': Wall_Message.objects.count(),
        'id': request.session['user_id'],
        'content': Content.objects.all() 
    }
    return render(request, 'home.html', context)

def upload_page(request):
    context = {
        'albums': Album.objects.filter(creator_id=request.session['user_id']),
        'id': request.session['user_id']
    }
    return render(request, 'upload_image.html', context)

def create_album(request):
    return render(request, 'create_album.html')

def account_edit(request):
    context = {
        'user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'account_edit.html', context)

def login(request):
    errors = User.objects.login_validator(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/sign_page')
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id
        return redirect('/home')

def register(request):
    Profile_Pic = ''
    if 'profile_picture' not in request.FILES: 
        Profile_Pic = -1
    else:
        Profile_Pic = request.FILES['profile_picture']

    errors = User.objects.register_validator(request.POST, Profile_Pic)

    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/create_page')
    else:
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            bio = request.POST['bio'],
            profile_picture = Profile_Pic,
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        )
        request.session['user_id'] = user.id
        request.session['greeting'] = user.first_name
        return redirect('/home')

def update_user(request, user_id):
    errors = User.objects.edit_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/account_edit')
    user = User.objects.get(id=user_id)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.bio = request.POST['bio']
    print(request.FILES)
    if request.FILES.get('profile_picture', False):
        user.profile_picture = request.FILES['profile_picture']
    else: 
        user.profile_picture = user.profile_picture
    user.email = request.POST['email']
    user.save()
    return redirect('/account_edit')

def post_message(request):
    the_message=request.POST.get('mess', False)
    post = Wall_Message.objects.create(message=the_message, poster=User.objects.get(id=request.session['user_id']))
    content = Content.objects.create(
        wall_message = post,
        image = None
        )
    print('created_wall_message')
    return redirect('/home')

def post_comment(request, the_id):
    poster = User.objects.get(id=request.session['user_id'])
    message = Wall_Message.objects.get(id=the_id)
    Comment.objects.create(comment=request.POST['comment'], poster=poster, wall_message=message)
    return redirect('/home')

def image_message(request, image_id):
    message = Post.objects.get(id=image_id)
    poster = User.objects.get(id=request.session['user_id'])
    Comment2.objects.create(comment=request.POST['comment'], poster=poster, image_message=message)
    return redirect('/home')

def add_like(request, id):
    liked_message = Wall_Message.objects.get(id=id)
    user_liking = User.objects.get(id=request.session['user_id'])
    liked_message.user_likes.add(user_liking)
    return redirect('/home')

def add_image_like(request, id):
    liked_message = Post.objects.get(id=id)
    user_liking = User.objects.get(id=request.session['user_id'])
    liked_message.image_user_likes.add(user_liking)
    return redirect('/home')

def delete_post(request, id):
    destroyed = Wall_Message.objects.get(id=id)
    destroyed.delete()
    return redirect('/home')

def delete_image(request, id):
    destroyed = Post.objects.get(id=id)
    destroyed.delete()
    return redirect('/home')

def delete_album(request, id):
    destroyed = Album.objects.get(id=id)
    destroyed.delete()
    return redirect('/upload')

def delete_album_photo(request, id):
    destroyed = Album_Photo.objects.get(id=id)
    destroyed.delete()
    return redirect('/upload')

def profile(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    User.objects.get(id=id)
    return render(request, 'profile.html', context)

def upload_image(request):
    Post.objects.create(
        title = request.POST['title'],
        cover = request.FILES['image'],
        user_post = User.objects.get(id=request.session['user_id'])
    )
    return redirect('/upload')

def upload_image2(request):
    post = Post.objects.create(
        title = request.POST['title'],
        cover = request.FILES['image'],
        user_post = User.objects.get(id=request.session['user_id'])
    )
    content = Content.objects.create(
        image = post,
        wall_message = None
    )
    return redirect('/home')

def create_album(request):
    album = Album.objects.create(
        title = request.POST['title'],
        description = request.POST['description'],
        creator_id = request.session['user_id']
    )
    return redirect('/upload')

def create_album_photo(request):
    album = Album.objects.get(id=request.POST['album_image'])
    album_photo = Album_Photo.objects.create(
        title = request.POST['title'],
        description = request.POST['description'],
        cover = request.FILES['image'],
        album = album
    )
    return redirect('/upload')

def logout(request):
    request.session.flush()

    return redirect('/')