# 🧠 AI Churn Prediction System

This project is a machine learning-based **Churn Prediction System** for banks. It uses customer data to predict whether a customer is likely to leave (churn). The model is trained using **Logistic Regression**, saved as a `.pkl` file, and integrated into a **React.js** frontend through a **Flask** backend.

---

## 🚀 Features

- Predicts bank customer churn using AI
- Machine learning model trained with Logistic Regression
- Model saved in `model.pkl` format
- Flask backend handles model inference and API
- React.js frontend for user-friendly input and prediction
- Accuracy: **83.91%** on test data

---

## 🧰 Tech Stack

| Component       | Technology         |
|----------------|--------------------|
| Machine Learning | Logistic Regression (Scikit-learn) |
| Backend        | Flask (Python)     |
| Frontend       | React.js           |
| Model Storage  | Pickle (`model.pkl`) |
| Dataset        | `BankChurners.csv` (public dataset) |

---

## ⚙️ How It Works

1. Preprocess the dataset (`BankChurners.csv`)
2. Train the Logistic Regression model using selected features
3. Save the trained model to a `model.pkl` file
4. Use Flask to expose a prediction API
5. Use React.js to collect user input and display results dynamically

---




## 📥 Input Features Used

The following input features from the dataset (`BankChurners.csv`) were used to train the model:

1. `CLIENTNUM` – Unique customer identifier  
2. `Customer_Age` – Age of the customer  
3. `Gender` – Gender of the customer (`Male`, `Female`)  
4. `Dependent_count` – Number of dependents  
5. `Education_Level` – Education qualification (`High School`, `Graduate`, etc.)  
6. `Marital_Status` – Marital status (`Married`, `Single`, etc.)  
7. `Income_Category` – Income bracket (`Less than $40K`, `$40K - $60K`, etc.)  
8. `Card_Category` – Type of card (`Blue`, `Gold`, `Platinum`, etc.)  
9. `Months_on_book` – Number of months as a customer  
10. `Total_Relationship_Count` – Total number of products held  
11. `Months_Inactive_12_mon` – Number of inactive months in the last 12 months  
12. `Contacts_Count_12_mon` – Number of contacts with the bank in the last 12 months  
13. `Credit_Limit` – Customer's credit limit  
14. `Total_Revolving_Bal` – Total revolving balance  
15. `Avg_Open_To_Buy` – Average available open-to-buy credit  
16. `Total_Amt_Chng_Q4_Q1` – Change in transaction amount from Q4 to Q1  
17. `Total_Trans_Amt` – Total transaction amount over the last 12 months  
18. `Total_Trans_Ct` – Total number of transactions  
19. `Total_Ct_Chng_Q4_Q1` – Change in transaction count from Q4 to Q1  
20. `Avg_Utilization_Ratio` – Average credit utilization ratio  
21. `Naive_Bayes_Classifier_Attrition_Flag_..._1` – Probability feature (engineered by original data source)  
22. `Naive_Bayes_Classifier_Attrition_Flag_..._2` – Probability feature (engineered by original data source)

Categorical features like `Gender`, `Education_Level`, `Marital_Status`, `Income_Category`, and `Card_Category` were encoded using **One-Hot Encoding** during preprocessing.

## 📁 Folder Structure

