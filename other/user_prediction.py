from other.ml_model import build_model
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def predict(Al_comp, Si_comp):

    knn, X, y = build_model()

    knn.fit(X, y)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=42,
        stratify=y
    )

    knn = KNeighborsClassifier(n_neighbors=19)
    knn.fit(X_train, y_train)

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

    print(f"The model predicted that your glass sample is most likely from a {glass_type}.\n")

    y_pred = knn.predict(X_test)
    y_train_pred = knn.predict(X_train)

    # compute accuracy on test data
    accuracy_knn = (y_pred == y_test).mean()

    # display results on test data
    print("Accuracy Score:")
    print(f"KNN classifier accuracy (k={19}): {accuracy_knn:.2%}\n")

  