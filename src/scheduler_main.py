from src.excel_reader import ExcelReader
from src.scheduler_generator import SchedulerGenerator
from src.google_calendar_api import *

excel_reader = ExcelReader()
df = excel_reader.read_single_excel("dummy")

data_dict = excel_reader.filter_dataframe_into_dict(df)
print(data_dict)

scheduler_generator = SchedulerGenerator()
scheduler_generator.builder(data_dict)
print("Sdfsfsdfdfsdfsdfdsfsfd")
list_events = scheduler_generator.class_requests_to_param_lists()

# post_new_event(list_events)
print("get today")
get_today_events(data_dict['dates'][0])
