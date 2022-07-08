#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import pandas as pd
from pandas.core.frame import DataFrame

def generate():
    list_test = []
    for j in os.listdir('./test/'):
            list_test.append('./test/'+j)
    fname = list_test[0]
    test= DataFrame({'fname':list_test})
    return test

