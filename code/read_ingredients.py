#!/usr/bin/env python

from code.recipes import ingredient_collector as ic
from code.recipes.utils import dict_to_df
import pandas as pd

ingredients, ing_counts = ic.get_all_ingredients()
one_hot_encoding = ic.one_hot_ingredient_coding()
print(one_hot_encoding)



# codes = dict_to_df(ingredients)
# counts = dict_to_df(ing_counts)
# df = pd.concat([codes, counts], axis=1)
# df = df.reset_index()
# df.columns = ['ingredient', 'code', 'count']
# df = df.set_index('ingredient')

# df.to_csv('../data/recipes/foodcom/all_ingredients.csv')
