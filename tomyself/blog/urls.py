from . import views
from django.urls import path

urlpatterns = [

    path('', views.index, name="index"),
    path('login/', views.login_view, name="login_view"),
    path('register/', views.register, name="register"),
    path('logout', views.logout_view, name="logout_view"),
    path('post/', views.post, name="post"),
    path('profile/', views.profile, name="profile"),
    path('<int:id>/like/', views.like, name="likes")
]