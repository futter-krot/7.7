from django.contrib import admin
from django.urls import path, include 

# urlpatterns = [
#     path('accounts/', include('allauth.urls')),
#     path('admin/', admin.site.urls),
#     path('', views.books_list),
#     path('index/', views.index),
#     path('index/book_increment/', views.book_increment),
#     path('index/book_decrement/', views.book_decrement),
#     path('redactions/', views.redactions),
#     path('author/create', AuthorEdit.as_view(), name='author_create'),  
#     path('authors', AuthorList.as_view(), name='author_list'),
#     path('author/create_many', author_create_many, name='author_create_many'),
#     path('login/', login, name='login'),  
#     path('logout/', logout, name='logout'),
# ]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('p_library.urls')),
    path('accounts/', include('allauth.urls')),
]