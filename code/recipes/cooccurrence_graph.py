#!/usr/bin/env python3

from pandas_ods_reader import read_ods

ingredients_file = 'filtered_most_seen_super.ods'

ingredients = read_ods(ingredients_file, sheet=1)

print(ingredients)
