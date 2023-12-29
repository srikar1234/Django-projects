from django.shortcuts import render
from django.http import HttpResponse
#current package importing
from .models import Post
# Create your views here.
# Views always have to resppond as a HTTP Response or an exception
#either return http response or else render (returns http response as default)

# dummy data to view on the template.html file
# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blogpost',
#         'content': 'Firstpost',
#         'date_posted':'abce, 2023'
#     } ,
#     {
#         'author': 'ABCDMS',
#         'title': 'Blogpost2',
#         'content': 'Secpost',
#         'date_posted':'abce, 2021'
#     },

#     {
#         'author': 'Mochicat',
#         'title': 'Blogpost3',
#         'content': 'Thirdpost',
#         'date_posted':'abce, 2024'
#     } 
# ]

def home(request):
    #passing the dummy data using the context variable.
    # The HTML file accesses the context object contents using 'posts' key 
    context = {
        'posts': Post.objects.all()
    }
    #Add context to function as an argument
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About page'})