import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def create_great_school_dataframe():
    school_profile = pd.read_csv(r'C:\Users\huyt\Desktop\Bootcamp\Projects\UCB_project_3\school_profile.csv')
    school_census = pd.read_csv(r'C:\Users\huyt\Desktop\Bootcamp\Projects\UCB_project_3\school_census.csv')

    dataset = school_profile.merge(school_census, on="gsID")
    dataset = dataset.dropna()
    return dataset

dataset = create_great_school_dataframe()
dataset = dataset.dropna()

X = dataset[["parentRating","Asian","enrollment"]]
y= dataset["gsRating"].values.reshape(-1,1)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

from sklearn.linear_model import LinearRegression
model = LinearRegression()

model.fit(X_train, y_train)
training_score = model.score(X_train, y_train)
testing_score = model.score(X_test, y_test)

### END SOLUTION

plt.scatter(model.predict(X_train), model.predict(X_train) - y_train, c="blue", label="Training Data")
plt.scatter(model.predict(X_test), model.predict(X_test) - y_test, c="orange", label="Testing Data")
plt.legend()
plt.hlines(y=0, xmin=y.min(), xmax=y.max())
plt.title("Residual Plot")

parentRating_user = input("What is the estimated parent rating? [Enter 1-5] ")
enrollment_user = input("How many students are enrolled at this school? ")
asian_user = input ('What is the % of Asian students?[Enter 0-100(%)]')

user_data = pd.DataFrame({"parentRating":[parentRating_user],
                  "Asian Population (%)": [asian_user],
                         "Enrollment (# of students)": [enrollment_user]})

value = model.predict(user_data)[0]
s = pd.Series(value)
import math
print("GS Rating is: " + str(math.floor(s[0])))
