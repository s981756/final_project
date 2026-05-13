import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from other.fetch_data import glass_types_data


def build_model(Al_comp, Si_comp):

    df, target_name, features = glass_types_data()

    #where user comps should go later:
    X = df[features]
    #glass type
    y = df['Type_of_glass']

    # X_train, X_test, y_train, y_test = train_test_split(
    #     X,
    #     y,
    #     test_size=0.3,
    #     random_state=42,
    #     stratify=y
    #     )

    # I selected k=19 for the KNN classifier.
    k = 19
    knn = KNeighborsClassifier(n_neighbors=k)

    #fitting data from dataset into model
    knn.fit(X, y)

    #predicting user input
    user_comps = str(Al_comp) + " " + str(Si_comp)
    user_data = [float(x) for x in user_comps.split()]
    prediction = knn.predict([user_data])

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
    print(glass_type)


    # create confusion matrix
    # conf_matrix_knn = pd.crosstab(
    #     y_test,
    #     y_pred,
    #     rownames=['Actual'],
    #     colnames=['Predicted'],
    #     dropna=False
    # )

    # # compute accuracy on test data
    # accuracy_knn = (y_pred == y_test).mean()

    # # display results on test data
    # print(f"KNN classifier accuracy (k={k}): {accuracy_knn:.2%}\n")
    # print(conf_matrix_knn)

    # # Add a 'correct' column for the visualization on test data
    # test_df = X_test.copy()
    # test_df['Type_of_glass'] = y_test
    # test_df['KNN_prediction'] = y_pred
    # test_df['correct'] = test_df['KNN_prediction'] == test_df['Type_of_glass']

    # # Add a 'correct' column for the visualization on training data
    # train_df = X_train.copy()
    # train_df['Type_of_glass'] = y_train
    # train_df['KNN_prediction'] = y_train_pred
    # train_df['correct'] = train_df['KNN_prediction'] == train_df['Type_of_glass']

    # # Create a visualization of KNN classifier results
    # # os.makedirs("plots", exist_ok=True)

    # # Create a visualization for test data
    # plt.figure(figsize=(8, 6))
    # sns.scatterplot(
    #     data=test_df,
    #     x='Al',
    #     y='Si',
    #     hue='correct',
    #     style='correct',
    #     s=100,
    #     palette={True: 'green', False: 'red'}
    # )

    # plt.title('KNN Algorithm: Correct vs Incorrect Predictions')
    # plt.xlabel('Al Composition')
    # plt.ylabel('Si composition')
    # plt.legend(title='Prediction Correct')
    # plt.grid(True)
    # plt.savefig('plots/knn_model_test_results.png', dpi=150)
    # plt.close()
