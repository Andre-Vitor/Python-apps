# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 03:25:34 2021

@author: T-Gamer
"""
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

# st.title('My first app')

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]})

# st.write(df)
# st.dataframe(df)


"""
# My first app
Here's our first attempt at using data to create a table:
"""

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df