import pytest
#importing glass_types_data() function
from other.fetch_data import glass_types_data
#importing make_plot() function
from other.making_plots import make_plot
#importing build_model() function
from other.ml_model import build_model

from other.user import User

# from other.program import get_elements

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


# #running fetch_data
# glass_types_data()

# #running function to make different plots
# make_plot('Na', 'Si')
# make_plot('Na', 'Mg')
# make_plot('Na', 'Al')
# make_plot("Ba", "Fe")

# get_elements()

# #running function to use ml_model
# build_model()

# comp1 = float(input("Please enter the comp of Al in your glass sample: "))
# comp2 = float(input("Please enter the comp of Si in your glass sample: "))

comp1 = 2.5
comp2 = 74.3

build_model(comp1, comp2)







