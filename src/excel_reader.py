import pandas as pd


def filter_dataframe(dataframe):
    

def read_single_excel(excel_path):
    excel_path = '../test_datas/iData Replay Application Form-3.xlsx'
    excel_data = pd.read_excel(excel_path, header=3)
    return excel_data


def read_multiple_excel(folder_path):
    print()
