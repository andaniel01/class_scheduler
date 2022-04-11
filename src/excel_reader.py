import pandas as pd


class ExcelReader:

    def __init__(self):
        pass

    def filter_dataframe_into_dict(self, dataframe):
        student_names = dataframe['Student name'].to_list()
        course_names = dataframe['course name'].to_list()
        sessions = dataframe['session'].to_list()
        dates = dataframe['date'].to_list()
        start_times = dataframe['start time'].to_list()
        end_times = dataframe['End time'].to_list()
        notes = dataframe['Note'].to_list()

        dict = {}
        dict['student names'] = student_names
        dict['course_names'] = course_names
        dict['sessions'] = sessions
        dict['dates'] = dates
        dict['start_times'] = start_times
        dict['end_times'] = end_times
        dict['notes'] = notes
        return dict

    def read_single_excel(self, excel_path):
        excel_path = '../test_datas/iData Replay Application Form-3.xlsx'
        excel_data = pd.read_excel(excel_path, header=2)
        print(excel_data)
        return excel_data


    def read_multiple_excel(self, folder_path):
        print()
