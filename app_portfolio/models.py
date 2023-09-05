from django.db import models

# Create your models here.
class About_me(models.Model):
    name = models.CharField(max_length=40)
    intro = models.TextField()
    details = models.TextField()
    address = models.TextField()
    phone = models.CharField(max_length= 13)
    email = models.EmailField()
    fb_link = models.TextField()
    insta_link = models.TextField()
    git_link = models.TextField()
    linkedin_link = models.TextField()

class Services(models.Model):
    icon = models.ImageField(upload_to='icons/')
    service_title = models.CharField(max_length=40)
    detail = models.TextField()

class My_works(models.Model):
    works_name = models.CharField(max_length=40)
    catagory = models.TextField()
    photo = models.ImageField(upload_to='images/')

class Guest_message(models.Model):
    guest_name = models.CharField(max_length=40)
    email = models.EmailField()
    message = models.TextField()

class Testimonial(models.Model):
    photo = models.ImageField(upload_to='testi_img/')
    name = models.CharField(max_length= 20)
    designation = models.CharField(max_length=30)
    message = models.TextField()

class Post_type(models.Model):
    type = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.type}'
   
class Post(models.Model):
    photo = models.ImageField(upload_to='image/')
    types = models.ManyToManyField(Post_type)
    title = models.TextField()
    text = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    email = models.EmailField(max_length= 100, null=True)
    text = models.TextField()
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)

