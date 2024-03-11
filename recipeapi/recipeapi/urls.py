"""
URL configuration for recipeapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import SimpleRouter
from recipe import views
from rest_framework.authtoken import views as rviews #import aliasing
router=SimpleRouter()
router.register('recipe',views.RecipeDetails)
router.register('review',views.ReviewDetails)
router.register('user',views.CreateUser)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api-token-auth/',rviews.obtain_auth_token), #login view
    # path('api/recipes/filter/', views.filter_recipes, name='filter_recipes'),
    # path('api/recipes/search/', views.search_recipes, name='search_recipes'),
    path('logout',views.user_logout.as_view(),name="logout"),
    path('search',views.search.as_view(),name="search"),

    # path('recipes/filter/', views.RecipeFilter, name='RecipeFilter'),
]
