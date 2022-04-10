from .class_request import ClassRequest
import datetime


class SchedulerGenerator:
    def __init__(self):
        self.student_name = ""
        self.duplicate_names = []
        self.class_requests = []
        self.rejected_requests = []

    def builder(self, data):
        student_names = data['student names']

        # find name from excel
        retrived_name = ""
        duplicate_names = []  # error notification later
        for name in student_names:
            if isinstance(name, str):
                if retrived_name == "" or retrived_name == name:
                    retrived_name = name
                else:
                    duplicate_names.append(name)

        # print(retrived_name)
        # print(duplicate_names)
        self.student_name = retrived_name
        self.duplicate_names = duplicate_names
        class_requests = []
        rejected_requests = []
        for i in range(len(student_names)):
            new_request = ClassRequest(retrived_name, data['course_names'][i], data['sessions'][i], data['dates'][i],
                                       data['start_times'][i], data['end_times'][i], data['notes'][i])
            if new_request.is_invalid_request():
                rejected_requests.append(new_request)
            else:
                class_requests.append(new_request)

        print("============ Valid Class Requests ============")
        for item in class_requests:
            print(item)

        print("============ Invalid Class Requests ============")
        for item in rejected_requests:
            print(item)

    def edit_student_requests(self, field_name, index, valid):
        successful_edit = False
        edit_list = []
        if valid:
            edit_list = self.class_requests
        else:
            edit_list = self.rejected_requests

        if field_name == 'student_names':
            value = input("Current Student Name is [" + edit_list[field_name][index] + "] Edit Student Name to:  ")
            edit_list[field_name][index] = value
        elif field_name == 'course_names':
            value = input("Current Course Name is [" + edit_list[field_name][index] + "] Edit Course Name to:  ")
            edit_list[field_name][index] = value
        elif field_name == 'sessions':
            value = input("Current Session is [" + edit_list[field_name][index] + "] Edit Session to:  ")
            edit_list[field_name][index] = value
        elif field_name == 'dates':
            value = input("Current Date is [" + edit_list[field_name][index] + "] Edit Date to (format ):  ")

            edit_list[field_name][index] = value
        elif field_name == 'start_times':
            print()
        elif field_name == 'end_times':
            print()
        elif field_name == 'notes':
            print()
        else:
            return successful_edit

    def write_student_valid_schedule(self):
        date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
        f = open(self.student_name + "_valid_" + date + ".txt", "w+")
        f.write("============ Valid Class Requests ============")
        f.write("----------------------------------------------")
        for item in self.class_requests:
            f.write(item)
        f.close()

    def write_student_invalid_schedule(self):
        date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
        f = open(self.student_name + "_invalid_" + date + ".txt", "w+")
        f.write("============ Invalid Class Requests ============")
        f.write("----------------------------------------------")
        for item in self.rejected_requests:
            f.write(item)
        f.close()
