import pytest
#importing glass_types_data() function
from other.fetch_data import glass_types_data
#importing make_plot() function
from other.making_plots import make_plot

from other.program import get_elements

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


#running fetch_data
# glass_types_data()

# #running function to make different plots
# make_plot('Na', 'Si')
# make_plot('Na', 'Mg')
# make_plot('Na', 'Al')

make_plot("Ba", "Fe")

# get_elements()