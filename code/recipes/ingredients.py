#!/usr/bin/env python3

import pandas as pd
import ast

ingredients_file = '../../data/all_ingredients.csv'
super_ingredients_file = '../../data/ingredients.txt'

with open(super_ingredients_file, 'r') as f:
    lines = f.readlines()

supers = {}
prev_line = ""
for line in lines:
    if prev_line.startswith('<en') and line.startswith('en'):
        super_ing = prev_line.split("<en:")[1].strip()
        ings = line.split('en:')[1].strip().split(',')

        for ing in ings:
            supers[ing.strip().lower()] = super_ing
    prev_line = line


# The information in super ingredients file is useless
def get_super_ingredient(ingredient):
    try:
        return supers[ingredient]
    except:
        return ingredient

ingredients = pd.read_csv(ingredients_file)
ingredients['supers'] = ingredients.apply(lambda x: get_super_ingredient(x['ingredient']), axis=1)
ingredients = ingredients[ingredients['count']/ingredients.shape[0] > 0]

ingredients.to_csv('filtered.csv')
