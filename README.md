# Bank-Campaign-Prediction

This project contains 3 files :

1. h8dsft_Milestone1.ipynb      : The notebook of the project
2. bestRandomForest_6Sep21.pkl  : Best Model predictor saved from the notebook, can used for predict other data
3. HTransformer.py		          : Additional Transformer related the best Model (you must call all class inside this Transfomer to execute the model predictor)

__Desclaimer__ 
- This model used scikit-learn version 0.24.1

## Dataset

The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed.

There are four datasets:
1. bank-additional-full.csv with all examples (41188) and 20 inputs, ordered by date (from May 2008 to November 2010), very close to the data analyzed in [Moro et al., 2014]
2. bank-additional.csv with 10% of the examples (4119), randomly selected from poin 1, and 20 inputs.
3. bank-full.csv with all examples and 17 inputs, ordered by date (older version of this dataset with less inputs).
4. bank.csv with 10% of the examples and 17 inputs, randomly selected from 3 (older version of this dataset with less inputs).

The smallest datasets are provided to test more computationally demanding machine learning algorithms (e.g., SVM).

The classification goal is to predict if the client will subscribe (yes/no) a term deposit (variable y).

In this notebook we will use dataset number 3 and 4 for modeling purpose.

## Attribute Information:

Input variables:

__bank client data:__
1. age (numeric)<br>
2. job : type of job (categorical: "admin.","unknown","unemployed","management","housemaid","entrepreneur","student","blue-collar","self-employed","retired","technician","services") <br>
3. marital : marital status (categorical: "married","divorced","single"; note: "divorced" means divorced or widowed)<br>
4. education (categorical: "unknown","secondary","primary","tertiary")<br>
5. default: has credit in default? (binary: "yes","no")<br>
6.  balance: average yearly balance, in euros (numeric) <br>
7. housing: has housing loan? (binary: "yes","no")<br>
8. loan: has personal loan? (binary: "yes","no")<br>

__related with the last contact of the current campaign:__
9. contact: contact communication type (categorical: "unknown","telephone","cellular") <br>
10. day: last contact day of the month (numeric)<br>
11.  month: last contact month of year (categorical: "jan", "feb", "mar", ..., "nov", "dec")<br>
12. duration: last contact duration, in seconds (numeric)<br>

__other attributes:__
13. campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)<br>
14. pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric, -1 means client was not previously contacted)<br>
15.  previous: number of contacts performed before this campaign and for this client (numeric)<br>
16. poutcome: outcome of the previous marketing campaign (categorical: "unknown","other","failure","success")<br>

__Output variable (desired target):__
17. y - has the client subscribed a term deposit? (binary: 'yes','no')<br>

You could download dataset from [here](https://www.kaggle.com/jsphyg/weather-dataset-rattle-package).<br>


## Goals

1. How much percentage of successful campaign in dataset?
2. Does client's balance affecting the successfull of customer?
3. Which contact method do produce the highest successfull campaign? How duration is going?
4. Which ccustomer's job who has highest succesfull campaign?
5. Does customer who has loan (housing, loans or credit) tend to reject the campaign promotion?
6. Create a model which could predict if the client will subscribe a term deposit or not (variable y).
