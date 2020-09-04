from django.urls import path
from . import views 
urlpatterns = [
    path('', views.index, name = 'index'),
    path('signup/', views.signup, name = 'signup'),
    path('signup_done/', views.signup_done, name = 'signup_done'),
    path('logout/', views.logout, name = 'logout'),
    path('blog/', views.blog, name = 'blog'),
    path('blog_c/', views.blog_c, name = 'blog_c'),
    path('blog_d/', views.blog_d, name = 'blog_d'),
    path('blog_u/<int:pk>', views.blog_u, name = 'blog_u'),
]