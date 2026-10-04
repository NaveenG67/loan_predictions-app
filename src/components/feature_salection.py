import pandas as pd
import numpy as np

def select_features(data:pd.DataFrame):
    data = data.drop(columns=['Loan_ID'])

    data['Loan_Amount_log'] = np.log(data['LoanAmount'])

    data["Gender"] = data["Gender"].fillna(data["Gender"].mode())
    data["Married"] = data["Married"].fillna(data["Married"].mode())
    data["Dependents"] = data["Dependents"].fillna(data["Dependents"].mode())
    data["Self_Employed"] = data["Self_Employed"].fillna(data["Self_Employed"].mode())
    data["Loan_Amount_Term"] = data["Loan_Amount_Term"].fillna(data["Loan_Amount_Term"].median())
    data["LoanAmount"] = data["LoanAmount"].fillna(data["LoanAmount"].mean())
    data["Credit_History"] = data["Credit_History"].fillna(data["Credit_History"].median())
    data["Loan_Amount_log"] = data["Loan_Amount_log"].fillna(data["Loan_Amount_log"].mean())

    data.isnull().sum()

    X = data.drop(columns=['Loan_Status'])
    y = data['Loan_Status']

    return X,y
def main():
    from config.paths import DATA_PATH
    from components.data_ingestion import load_data
    data = pd.read_csv(DATA_PATH /'loan-prediction.csv')
    X,y = select_features(data)

    print(X.shape)
    print(y.shape)

if __name__ == '__main__':
    main()