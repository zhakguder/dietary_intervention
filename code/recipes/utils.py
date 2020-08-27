#!/usr/bin/env python

import pandas as pd

def dict_to_df(dict):
    '''Args:
    dict: dict of ingredients
    '''
    col1 = list(dict.keys())
    col2 = list(dict.values())

    return pd.DataFrame.from_dict({'a': col1, 'b': col2}).set_index('a')
