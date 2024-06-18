import time
import json
import pyexcel
import os

# the relevant models to track student performance 
class StudentProfile:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        # self.standing = standing

    def dictionary(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age
        }
    # save to json
    # def add(self, name, age):
    #     student = StudentProfile(1, "name", 10)
    #     with open("students.json", "w") as file:
    #         student = StudentProfile(id, name, age)
    #         json.dump(student.dictionary(), file)

# def create_profile(name, age):

class TrainerProfile:
    def __init__(self, id, name, students):
        self.id = id
        self.name  = name
        self.students = students


class TrialPerformance:
    # students = StudentProfile()
    def __init__(self, trial_id, title, student_name, student_id, subject, round, score, time_now):
        self.students = StudentProfile()
        self.id = trial_id
        self.title = title
        self.student_tag = [student_name, student_id]
        self.subject = subject
        self.round = round
        self.score = score
        time_now = time.localtime()
        self.time_now = time_now
        
        

