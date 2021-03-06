from django.contrib import admin
from django.urls import path
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.director_create_listview),
    path('api/v1/director/<int:id>', views.director_detail_view),
    path('api/v1/movies/', views.movie_create_listview),
    path('api/v1/movies/<int:id>/', views.movie_detail_view),
    path('api/v1/reviews/', views.review_create_listview),
    path('api/v1/reviews/<int:id>/', views.review_detail_view)
]
