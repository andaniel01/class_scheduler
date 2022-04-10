from src.scheduler_generator import SchedulerGenerator

class SchedulerManager:

    def __init__(self):
        self.student_batch = []

    def add_student_schedule(self, scheduler):
        self.student_batch.append(scheduler)

    def edit_schedule(self, field_name, index, value):
        # data['student names']
        # student_names = data['student names']
        # dict['course_names'] = course_names
        # dict['sessions'] = sessions
        # dict['dates'] = dates
        # dict['start_times'] = start_times
        # dict['end_times'] = end_times
        # dict['notes'] = notes
        print()