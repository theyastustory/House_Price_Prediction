# House_Price_Prediction
Aim to normalise house search by using latest machine learning algorithms

## What it does
This is an application in which we can just feed in the location, area, availability, square footage, BHK and a bathroom and we can know the price of the house we need. 

## How we built it
1. We set up LinuxOne cloud on virtual machine and installed jupyter lab on it.
2. Then we chose the dataset from kaggle.
3. We cleaned the dataset as per our need.
4. Then in the jupyter notebook we wrote the code for data preprocessing.
5. Then we split the train and test data.
6. We applied the Linear Regression model with the accuracy of 82%.
7. Next model we applied is lasso with the accuracy of 81.2%.
8. The next model we used  is Ridge with the accuracy of  82.3% and imported pickle.
9. We dumped our ridge model with the name RidgeModel.pkl.
10. And then we imported cleaned_data.csv and the RidgeModel.pkl inside our IDE.
11. And then we made a simple skeletal structure of flask.
12. Here the libraries we used are flask, Scikit-learn, Pandas, Pickle-mixin. So, in our terminal first we imported all the libraries.
13. We created a template called as index.html where our model page is rendered out.
14. We used bootstrap for the general design of our application.
15. We integrate our ML model and HTML file by sending the value of the object using render_template.

## How it works
1) Collecting Data: First step was to collect data. We collected data from different sources and merged them together to form our training data set.

2) Then we trained the model using machine learning algorithm which in this case is multiple linear regression.

3) Based on the generated graphs, we predicted the cost of the house
