from .class_request import ClassRequest

class SchedulerGenerator:
    def __init__(self):
        self.student_name = ""
        self.duplicate_names = []
        self.class_requests = []
        self.rejected_requests = []


    def builder(self, data):
        student_names = data['student names']

        #find name from excel
        retrived_name = ""
        duplicate_names = []    #error notification later
        for name in student_names:
            if isinstance(name, str):
                if retrived_name == "" or retrived_name == name:
                    retrived_name = name
                else:
                    duplicate_names.append(name)

        #print(retrived_name)
        #print(duplicate_names)
        self.student_name = retrived_name
        self.duplicate_names = duplicate_names
        class_requests = []
        rejected_requests = []
        for i in range(len(student_names)):
            new_request = ClassRequest(retrived_name, data['course_names'][i], data['sessions'][i], data['dates'][i], data['start_times'][i], data['end_times'][i], data['notes'][i])
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


