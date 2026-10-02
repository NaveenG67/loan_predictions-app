import pandas as pd
import os

Artifacts_path = "../artifacts/reports"
os.makedirs(Artifacts_path, exist_ok=True)

def basic_eda(data: pd.DataFrame):
    print('\n' + '=' * 60)
    print('Exploratory Data Analysis'.center(60))
    print('=' * 60)

    print(f'\nDataset Shape: {data.shape}')

    print('\nTarget Variable Distribution'.center(60))
    print(data['Loan_Status'].value_counts())

    print('\nNumerical variable Distribution'.center(60))
    print(data.describe())

    print('\nCategorical variable Distribution'.center(60))
    print(data.describe(include='O'))

    print('\nEducation Variable Distribution'.center(60))
    print(data['Education'].value_counts())

    print('\nSelf Employed Variable Distribution'.center(60))
    print(data['Self_Employed'].value_counts())

    print(pd.crosstab(data['Self_Employed'], data['Loan_Status']))

    with open('dataset_summary.txt', 'w') as file:
        file.write('\n' + '=' * 60)
        file.write('\nExploratory Data Analysis\n'.center(60))
        file.write('\n'+'=' * 60)

        file.write(f'\nDataset Shape: {data.shape}\n')

        file.write('\nTarget Variable Distribution\n'.center(60))
        file.write(str(data['Loan_Status'].value_counts()))

        file.write('\nEducation Variable Distribution\n'.center(60))
        file.write(str(data['Education'].value_counts()))

        file.write('\nSelf Employed Variable Distribution\n'.center(60))
        file.write(str(data['Self_Employed'].value_counts()))


def main():
    from data_ingestion import load_data

    data = load_data()
    basic_eda(data)

if __name__ == '__main__':
    main()
