import os

import matplotlib.pyplot as plt
import pandas as pd
from config.paths import CHARTS_PATH

def save_bar_chart(series,title,filename,xlabel='',ylabel='Count'):
    plt.figure(figsize=(10,10))
    plt.bar(series.value_counts().keys(),series.value_counts().values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.tight_layout()

    plt.savefig(os.path.join(CHARTS_PATH,filename))
    plt.close()

def save_histogram_chart(series,title,filename,bins=20):
    plt.figure(figsize=(10,10))
    plt.hist(series,bins=bins)
    plt.title(title)
    plt.xlabel(series.name)
    plt.ylabel('Frequency')

    plt.tight_layout()

    plt.savefig(os.path.join(CHARTS_PATH,filename))
    plt.close()

def save_stacked_bar(crosstab,title,filename):
    plt.figure(figsize=(10,10))
    crosstab.plot(kind='bar')
    plt.title(title)
    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS_PATH,filename))
    plt.close()

def save_box_plot(series,title,filename):
    plt.figure(figsize=(10,10))
    series.plot(kind='box')
    plt.title(title)
    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS_PATH,filename))
    plt.close()

def create_visuals(data:pd.DataFrame):
    save_bar_chart(data['Loan_Status'],
                   title = 'Loan Status Distribution',
                   filename ='Loan_Status_Distribution.png')

    save_box_plot(data['LoanAmount'],
                  title = 'Loan Amount Distribution',
                  filename ='Loan_Amount_Distribution.png')

    save_histogram_chart(data['LoanAmount'],
                         title = 'Loan Amount Distribution',
                         filename ='Loan_Amount_Distribution.png')


    save_box_plot(data['ApplicantIncome'],
                  title = 'Applicant Income Distribution',
                  filename ='Applicant_Income_Distribution.png')

    save_histogram_chart(data['ApplicantIncome'],
                         title = 'Applicant Income Distribution',
                         filename ='Applicant_Income_Distribution.png')

    save_box_plot(data['ApplicantIncome'],
                  title = 'ApplicantIncome Distribution',
                  filename ='Applicant_Income_Distribution.png')


def main():
    from src.components.data_ingestion import load_data
    data = load_data()
    create_visuals(data)

if __name__ == '__main__':
    main()