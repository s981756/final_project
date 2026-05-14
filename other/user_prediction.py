from other.ml_model import build_model

def predict(Al_comp, Si_comp):

    knn, X, y = build_model()

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

    print(f"The model predicted that your glass sample is likely from a {glass_type}.")
  