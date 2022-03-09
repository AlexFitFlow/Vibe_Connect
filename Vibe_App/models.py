from django.db import models
import re
import bcrypt

class UserManager(models.Manager):

    def register_validator(self, post_data, pic_data):
        errors = {}
        if len(post_data['first_name']) < 1:
            errors['first_name'] = 'First name is too short.'
        if len(post_data['last_name']) < 1:
            errors['last_name'] = 'Last Name must be at least one character long.'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):        
            errors['email'] = "Invalid email address."
        if len(post_data['email']) > 30:
            errors['email'] = 'Email address is too long.'
        if len(post_data['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters long.'
        if post_data['password'] != post_data['confirm_password']:
            errors['confirm_password'] = 'Passwords do not match.'
        if pic_data == -1:
            errors['profile_picture'] = 'Profile Picture is needed.'
        try:
            user = User.objects.get(email = post_data['email'])
            errors['email_in_use'] = 'This email is already associated with an account.'
        except:
            pass
        return errors

    def login_validator(self, postData):
        errors = {}
        check = User.objects.filter(email=postData['email'])
        if not check:
            errors['email'] = "Email has not been registered"
        else:
            if not bcrypt.checkpw(postData['password'].encode(), check[0].password.encode()):
                errors['email'] = "Email and password do not match."
        return errors

    def edit_validator(self, post_data):
        errors = {}
        if len(post_data['first_name']) < 1:
            errors['first_name'] = 'First name is too short.'
        if len(post_data['last_name']) < 1:
            errors['last_name'] = 'Last Name must be at least one character long.'
        if len(post_data['email']) > 30:
            errors['email'] = 'Email address is too long.'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    profile_picture = models.ImageField(default='/static/images/default.jpg', null=True)
    bio = models.CharField(max_length=100, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = UserManager()

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(default='deafault.png', blank=True)
    user_post = models.ForeignKey(User, related_name='user_post', on_delete=models.CASCADE, default=1)
    image_user_likes = models.ManyToManyField(User, related_name='image_liked_posts')

class Wall_Message(models.Model):
    message = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='user_messages', on_delete=models.CASCADE)
    user_likes = models.ManyToManyField(User, related_name='liked_posts')


class Comment(models.Model):
    comment = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    wall_message = models.ForeignKey(Wall_Message, related_name="post_comments", on_delete=models.CASCADE)

class Comment2(models.Model):
    comment = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='user2_comments', on_delete=models.CASCADE)
    image_message = models.ForeignKey(Post, related_name="image_comments", on_delete=models.CASCADE)

class Profile(models.Model):
    name = models.CharField(max_length=25)
    profile_picture = models.ImageField(default='dafault.jpg', null=True)
    bio = models.CharField(max_length=25)

class Content(models.Model):
    wall_message = models.OneToOneField(Wall_Message, on_delete=models.CASCADE, blank=True, null=True)
    image = models.OneToOneField(Post, on_delete=models.CASCADE, blank=True, null=True)

class Album(models.Model):
    title = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    creator = models.ForeignKey(User, related_name="albums", on_delete=models.CASCADE)


class Album_Photo(models.Model):
    title = models.TextField(max_length=255, null=True)
    description = models.TextField(max_length=255, null=True)
    album = models.ForeignKey(Album, related_name="album_image", on_delete=models.CASCADE)
    cover = models.ImageField(default='deafault.png', blank=True)








