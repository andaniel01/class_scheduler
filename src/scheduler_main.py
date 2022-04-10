from src.excel_reader import ExcelReader
from src.scheduler_generator import SchedulerGenerator

excel_reader = ExcelReader()
df = excel_reader.read_single_excel("dummy")

data_dict = excel_reader.filter_dataframe_into_dict(df)
print(data_dict)

scheduler_generator = SchedulerGenerator()
scheduler_generator.builder(data_dict)
