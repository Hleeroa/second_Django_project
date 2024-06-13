from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def recipe(request, dish_name):
    try:
        dish = DATA[dish_name]
    except KeyError:
        return HttpResponse('Dish is not found')
    servings = int(request.GET.get('servings', 1))
    ingredients = {}
    for name, amount in dish.items():
        new_amount = dish[name] * servings
        ingredients[name] = round(new_amount, 3)
    return render(request, 'calculator/index.html', context={'ingredients': ingredients})


def main_page(request):
    return HttpResponse('Easy ancient recipies')


def calculator(request):
    servings = int(request.GET.get('servings'))
    context = {}
    for recipe in DATA:
        upper_context = context[recipe] = {}
        for ingredient, amount in recipe:
            calculations = amount * servings
            upper_context[ingredient] = calculations
    return render(request, 'calculator/index.html', context)
