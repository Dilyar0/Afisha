from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import DirectorSerializer, MovieSerializer, ReviewSerializer
from .models import Director, Movie, Review


@api_view(['GET'])
def director_create_listview(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def director_detail_view(request, id):
    try:
        directors = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error", f"Директор с id = {id} не существует!!!"})
    data = DirectorSerializer(directors).data
    return Response(data=data)


@api_view(['GET'])
def movie_create_listview(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_detail_view(request, id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error", f"Фильм с id = {id} не существует!!!"})
    data = MovieSerializer(movies).data
    return Response(data=data)


@api_view(['GET'])
def review_create_listview(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error', f"Review with id = {id} does not exist"})
    data = ReviewSerializer(review).data
    return Response(data=data)