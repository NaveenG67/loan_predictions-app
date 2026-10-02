from data_ingestion import load_data

def main():
    data = load_data()
    print('Row and Column Count')
    print(data.shape,'\n','_'*60)
    print('Top 5 Values')
    print(data.head(),'\n','_'*60)

if __name__ == '__main__':
        main()