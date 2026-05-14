import pytest
#importing glass_types_data() function
from other.fetch_data import glass_types_data
#importing make_plot() function
from other.making_plots import make_plot
#importing build_model() function
from other.ml_model import build_model
#importing predict() function
from other.user_prediction import predict
#importing accuracy_of_model()
from other.ml_model import accuracy_of_model

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


# #running fetch_data
# glass_types_data()

# #running function to make different plots
# make_plot('Al', 'Si')

menu_option = int(input("Welcome to the Glass Identifier. Please select one option from the menu: \n  1. Run program\n  2. See accuracy of model\n"))
if menu_option == 1:
    print("Please insert the composition of each element found within your glass sample.")
    comp1 = float(input("Al: "))
    comp2 = float(input("Si: "))
    if Al_comp < 0.29 or Al_comp > 3.5:
        print("Sorry, invaild number.")
    elif Si_comp < 69.81 or Si_comp > 75.41:
        print("Sorry, invalid number.")
    else:
        predict(comp1, comp2)
elif menu_option == 2:
    accuracy_of_model()
# elif menu_option == 1:








