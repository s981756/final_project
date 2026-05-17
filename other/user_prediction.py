from other.ml_model import build_model
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def predict(Al_comp, Si_comp):

    knn, X_train, y_train, X_test, y_test, y_pred, y_train_pred = build_model()

    #predicting user input
    user_comps = pd.DataFrame({'Al': [Al_comp], 'Si': [Si_comp]})
    prediction = knn.predict(user_comps)

    #creating new dict so that program can output glass type as an actual glass type and not just a number
    glass_types = {
        1: "Float Processed Building Window",
        2: "Non-float Processed Building Window",
        3: "Float Processed Building Window",
        5: "Container",
        6: "Tableware",
        7: "Headlamp"
    }

    glass_type = glass_types[prediction[0]]

    print(f"\nThe model predicted that your glass sample is most likely from a {glass_type}.\n")

    # compute accuracy on test data
    accuracy_knn = (y_pred == y_test).mean()

    # display results on test data
    print("\nAccuracy Score:")
    print(f"KNN classifier accuracy (k={19}): {accuracy_knn:.2%}\n")
    print("_________________________________________________________________________________\n")

  