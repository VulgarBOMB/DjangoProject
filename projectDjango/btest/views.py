from django.shortcuts import render
from .models import *


def index(request):
    return render(request, "btest/index.html")


def lunches(request):
    lunch_structures = LunchStructure.objects.all()

    for lunch_structure in lunch_structures:
        print("--------------------")
        print(lunch_structure.lunch)
        print("--------------------")
        for meals in lunch_structure.meals.all():
            print(meals.name)

    return render(request, "btest/lunches.html", {
        'lunch_structures': lunch_structures,
    })


def meals(request):
    meal_list = Meal.objects.all()
    lunch_structure_list = LunchStructure.objects.all()
    meals_list = []

    for meal_item in meal_list:
        arr = []
        for lunch_structure in lunch_structure_list:
            for meals in lunch_structure.meals.all():
                if meal_item.name == meals.name:
                    arr.append(Lunch.objects.get(id=lunch_structure.lunch.id))
                    print(str(Lunch.objects.get(id=lunch_structure.lunch.id)) + " - " + str(meals.name))
        meals_list.append({'meal': meal_item, 'lunches': arr})

    return render(request, "btest/meals.html", {
        'meals_list': meals_list,
    })
