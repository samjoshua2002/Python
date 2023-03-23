import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, name, age, roll_no, room_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.room_no = room_no

class Transaction:
    def __init__(self, student, amount, date):
        self.student = student
        self.amount = amount
        self.date = date

class Hostel:
    def __init__(self):
        self.students = {}
        self.transactions = []

    def add_student(self, student):
        self.students[student.roll_no] = student

    def remove_student(self, roll_no):
        del self.students[roll_no]

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_student_transactions(self, roll_no):
        student_transactions = [t for t in self.transactions if t.student.roll_no == roll_no]
        return student_transactions


class HostelManagementApp:
    def __init__(self, master):
        self.master = master
        master.title("Hostel Management System")

        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0)

        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)

        self.age_label = tk.Label(master, text="Age:")
        self.age_label.grid(row=1, column=0)

        self.age_entry = tk.Entry(master)
        self.age_entry.grid(row=1, column=1)

        self.roll_no_label = tk.Label(master, text="Roll No:")
        self.roll_no_label.grid(row=2, column=0)

        self.roll_no_entry = tk.Entry(master)
        self.roll_no_entry.grid(row=2, column=1)

        self.room_no_label = tk.Label(master, text="Room No:")
        self.room_no_label.grid(row=3, column=0)

        self.room_no_entry = tk.Entry(master)
        self.room_no_entry.grid(row=3, column=1)

        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.submit_button.grid(row=4, column=1)

    def submit(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        roll_no = self
d