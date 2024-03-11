from django.shortcuts import render
from recipe.models import Recipe,Review
from recipe.serializers import RecipeSerializer,UserSerializer,ReviewSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import filters,status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework.views import APIView




class RecipeDetails(viewsets.ModelViewSet):
    queryset=Recipe.objects.all()
    serializer_class=RecipeSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewDetails(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateUser(viewsets.ModelViewSet):
    queryset =User.objects.all()
    serializer_class =UserSerializer


class user_logout(APIView):
    permission_classes=[IsAuthenticated,]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class search(APIView):
    def get(self,request):

        query=self.request.query_params.get('search')
        if(query):
            recipes=Recipe.objects.filter(Q(title__icontains=query)|Q(cuisine__icontains=query))
            r=RecipeSerializer(recipes,many=True)
            return Response(r.data)
        if not query.exists():
            return Response("No results found", status=status.HTTP_404_NOT_FOUND)







