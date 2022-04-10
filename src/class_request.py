import datetime
import math


class ClassRequest:

    def __init__(self, student_name, course_name, session, date, start_time, end_time, note):
        self.student_name = student_name
        self.course_name = course_name
        self.session = session
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.note = note

    def is_invalid_request(self):

        # check student name
        if not isinstance(self.student_name, str):
            return True

        # course check
        if not isinstance(self.course_name, str):
            return True

        # session check
        if isinstance(self.session, int) or isinstance(self.session, float):
            if math.isnan(self.session):
                return True
        elif not isinstance(self.session, str):
            return True

        # date check and past date check
        if not isinstance(self.date, datetime.datetime):
            return True
        else:
            if self.date.date() < datetime.date.today():
                return True

        # start time check
        if not isinstance(self.start_time, datetime.time):
            return True

        return False

    def __str__(self):
        string = "Student Name: {0} \n" \
                 "Course Name:  {1} \n" \
                 "Session:      {2} \n" \
                 "Date:         {3} \n" \
                 "Start Time:   {4} \n" \
                 "End Time:     {5} \n" \
                 "Note:         {6} \n"

        return string.format(self.student_name, self.course_name, self.session, self.date, self.start_time,
                             self.end_time, self.note)
