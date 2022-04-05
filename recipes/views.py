from django.shortcuts import render
from utils.recipes.factory import make_recipe
from recipes.models import Recipe


def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        # 'recipes': [make_recipe() for _ in range(10)], #geração de dados aleatórios via lib faker
        'recipes': recipes
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })

