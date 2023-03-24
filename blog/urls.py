from django.urls import path, include
from . import views

urlpatterns = [path('', views.PostView.as_view()),
               path('<int:pk>/', views.PostDetail.as_view()),
               path('review/<int:pk>', views.AddComments.as_view(), name='add_comments'),
               path('<int:pk>/add_likes/', views.AddLike.as_view(), name='add_like'),
               path('<int:pk>/del_likes/', views.DelLike.as_view(), name='del_like'),
               path('accounts/', views.LogIn.as_view(), name='login'),]
