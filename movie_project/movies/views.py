from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import MovieSerializer, RegisterSerializer
from django.db.models import Q
from .utils import fetch_movies_from_tmdb
from django.shortcuts import get_object_or_404


class RegisterView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieListCreateView(APIView):
    def get(self, request):
        search = request.query_params.get('search')
        genre = request.query_params.get('genre')
        min_rating = request.query_params.get('min_rating')
        max_rating = request.query_params.get('max_rating')

        movies = Movie.objects.all()
        filters = Q()

        if search:
            filters &= Q(title__icontains=search)
        if genre:
            filters &= Q(genre__iexact=genre)
        if min_rating:
            filters &= Q(rating__gte=min_rating)
        if max_rating:
            filters &= Q(rating__lte=max_rating)

        movies = movies.filter(filters)

        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailView(APIView):
    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return Response({'message': 'Movie deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class TMDBSearchView(APIView):
    def get(self, request):
        query = request.query_params.get('query', '')
        if not query:
            return Response({'error': 'Query parameter is required'}, status=400)
        data = fetch_movies_from_tmdb(query)
        return Response(data)
