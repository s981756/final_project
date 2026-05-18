import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from other.fetch_data import glass_types_data

#main code for building model
def build_model():

    df, target_name = glass_types_data()

    X = df[['Al', 'Si']]
    #glass type
    y = df['Type_of_glass']


    # I selected k=19 for the KNN classifier.
    k = 19
    knn = KNeighborsClassifier(n_neighbors=k)

    #fitting model to dataset
    knn.fit(X, y)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=42,
        stratify=y
    )

    y_pred = knn.predict(X_test)
    y_train_pred = knn.predict(X_train)


    return knn, X_train, y_train, X_test, y_test, y_pred, y_train_pred


def accuracy_of_model():

    knn, X_train, y_train, X_test, y_test, y_pred, y_train_pred = build_model()
    
    # create confusion matrix
    conf_matrix_knn = pd.crosstab(
        y_test,
        y_pred,
        rownames=['Actual'],
        colnames=['Predicted']
    )
    
    print("Confusion Matrix for Testing Data:")
    print(conf_matrix_knn)

    # Add a 'correct' column for the visualization on training data
    train_df = X_train.copy()
    train_df['Type_of_glass'] = y_train
    train_df['KNN_prediction'] = y_train_pred
    train_df['correct'] = train_df['KNN_prediction'] == train_df['Type_of_glass']

    # Create a visualization for training data
    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        data=train_df,
        x='Al',
        y='Si',
        hue='correct',
        style='correct',
        s=100,
        palette={True: 'green', False: 'red'}
    )

    plt.title('KNN Algorithm: Correct vs Incorrect Predictions')
    plt.xlabel('Al composition')
    plt.ylabel('Si composition')
    plt.legend(title='Prediction Correct')
    plt.grid(True)
    plt.savefig('/workspaces/final_project/plots/knn_model_training_results.png', dpi=150)
    plt.close()

    print("\nA visualization for the training data has been made and put into the 'plots' folder.\n")

    # Add a 'correct' column for the visualization on test data
    test_df = X_test.copy()
    test_df['Type_of_glass'] = y_test
    test_df['KNN_prediction'] = y_pred
    test_df['correct'] = test_df['KNN_prediction'] == test_df['Type_of_glass']

    # Create a visualization for test data
    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        data=test_df,
        x='Al',
        y='Si',
        hue='correct',
        style='correct',
        s=100,
        palette={True: 'green', False: 'red'}
    )

    plt.title('KNN Algorithm: Correct vs Incorrect Predictions')
    plt.xlabel('Al composition')
    plt.ylabel('Si composition')
    plt.legend(title='Prediction Correct')
    plt.grid(True)
    plt.savefig('/workspaces/final_project/plots/knn_model_test_results.png', dpi=150)
    plt.close()

    print("\nA visualization for the test data has been made and put into the 'plots' folder.\n")
    print("_________________________________________________________________________________\n")