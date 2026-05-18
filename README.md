
**Project Name: Glass Identifier**

Name: Kaitlyn Murray

-----------------------------------------------------------------------------------------

Video summary: 

**Purpose of Project**

The purpose of this project was to use a Glass Identification dataset to build a Machine Learning model that uses a KNN classifier to identify glass samples based on the composition of Al and Si in them. This could be used in foresic studies and sciences as it could provide insight into where glass samples came from.

**Methods**

To begin, I used pandas and matplotlib in order to create visualizations of the different elements contained in the glass samples in the UCI dataset. I generated many plots to see which variables would be the best to build my KNN model. 
These are some of the plots:

![Al vs. K](/workspaces/final_project/plots/Al_v_K.png)

<!-- 
<img src="/workspaces/final_project/plots/Al_v_K.png" width=325 height=225>
<img src="/workspaces/final_project/plots/Fe_v_Si.png" width=325 height=225>
<img src="/workspaces/final_project/plots/Al_v_Si.png" width=325 height=225> -->

I ultimately chose to use Al and Si as the two variables for the model. This is because the plot looked like it had the most defined groups of each of the glass types, so it would have the most accurate KNN classifier model.

For the KNN classier, I ultimately chose a k value of 19, as I tried many different k values and this one had the greates accuracy when working with the test data. 

**Running Program**

First, run the app.py file by typing "python3 app.py" into the terminal. The program will prompt you to pick one of three choices: Run theprogram, see the accuracy of the model, or quit. These choices are numbered so you will need to type 1, 2, or 3 into the terminal. 

if you type 1, the program will prompt you to put in the concentrations of Al and Si found in your glass sample. Because the minimum composition of Al in the dataset is 0.29 and the maximum is 3.5, you will need to put in a value between those for it to work. Also, the minimum composition for Si is 69.81 and the maximum is 75.41, so the value for that composition should be between those two values. After this, the program will give you a prediction of what glass type your sample was based on those compositions. It will also print the accuracy of the model. 

if you type 2, the program will print the confusion matrix for the model, and it will also create a visualization for the model's accuracy with the testing data and the training data, which will both be stored in the "plots" folder. 

Since the main code for the program is on a while loop, if you type 3, the program stop. 

