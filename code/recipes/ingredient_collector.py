#!/usr/bin/env python

import ast
import csv
from code.recipe_personalization.recipe_gen import language
from collections import defaultdict
import numpy as np
import pandas as pd

N_RECIPES = 100

recipe_file = 'data/recipes/foodcom/PP_recipes.csv'
ingredients = {}
ing_counts = defaultdict(int)
ingredient_col = 3

def ingredient_code_to_int(code_list):
    '''Args:
    code_list (list of list of string)
    '''
    return _string_to_int(code_list)

def _string_to_int(string):
    return ast.literal_eval(string)

def ingredient_code_to_string(code):
    '''Args:
    code (list of strings)
    '''
    return language.pretty_decode(code).strip()



def get_ingredients_of_a_recipe(ing, ing_no):
    codes = ingredient_code_to_int(ing)
    for code in codes:
        ing_str = ingredient_code_to_string(code)
        if ing_str not in ingredients:
            ingredients[ing_str] = ing_no
            ing_no += 1
        ing_counts[ing_str] += 1
    return ing_no


lines = []
with open(recipe_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        lines.append(row)

ingredients_lists = [x[ingredient_col] for x in lines[1:]]

def get_all_ingredients():
    ing_no = 0
    for ing in ingredients_lists:
        ing_no = get_ingredients_of_a_recipe(ing, ing_no)
    return ingredients, ing_counts


def one_hot_ingredient_coding():

    # number of ingredients
    max_ing_int = max(ingredients.values())
    # number of recipes
    n_recipes = len(ingredients_lists)

    recipe_one_hot = np.zeros((n_recipes, max_ing_int+1), dtype=np.int32)

    for i, ing in enumerate(ingredients_lists):
        codes = ingredient_code_to_int(ing)
        for code in codes:
            ing_str = ingredient_code_to_string(code)
            ing_no = ingredients[ing_str]
            recipe_one_hot[i, ing_no] = 1
    recipe_one_hot = pd.DataFrame(recipe_one_hot, index=None, columns=range(max_ing_int+1))
    recipe_one_hoe.drop([0], axis=1, inplace=True )
    return recipe_one_hot
