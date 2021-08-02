from django.shortcuts import render, HttpResponse, redirect
from .models import Recipe

# Create your views here.
def index(request):
    context = {
        'AllRecipes': Recipe.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):
    print(request.POST)
    name = request.POST['name']
    description = request.POST['description']
    ingredients = request.POST['ingredients']
    servings = request.POST['servings']
    Recipe.objects.create(name=name, description=description, ingredients=ingredients, servings=servings)
    print('Recipe successfully created')
    return redirect('/')

def oneRecipe(request, recipeID):
    context = {
        'recipe': Recipe.objects.get(id=recipeID)
    }
    return render(request, 'oneRecipe.html', context)

def update(request):
    recipe_to_update = Recipe.objects.get(id=request.POST['id'])
    recipe_to_update.name = request.POST['name']
    recipe_to_update.description = request.POST['description']
    recipe_to_update.ingredients = request.POST['ingredients']
    recipe_to_update.servings = request.POST['servings']
    return redirect(f'/recipe/{recipe_to_update.id}')

def destroy(request):
    recipe_to_destroy = Recipe.objects.get(id=request.POST['id'])
    recipe_to_destroy.delete()
    return redirect('/')