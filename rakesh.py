import tkinter as tk
from tkinter import messagebox

class StudentDataEntryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Data Entry Form")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        # Create variables to store input
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.roll_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.course_var = tk.StringVar()

        # Build the form
        self.create_widgets()

    def create_widgets(self):
        # Title label
        tk.Label(self.root, text="Enter Student Details", font=("Arial", 16, "bold")).pack(pady=10)

        # Frame to hold form entries
        form_frame = tk.Frame(self.root)
        form_frame.pack(padx=20, pady=10)

        # Name
        tk.Label(form_frame, text="Name:", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)
        tk.Entry(form_frame, textvariable=self.name_var, width=30).grid(row=0, column=1, pady=5)

        # Age
        tk.Label(form_frame, text="Age:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
        tk.Entry(form_frame, textvariable=self.age_var, width=30).grid(row=1, column=1, pady=5)

        # Roll Number
        tk.Label(form_frame, text="Roll No:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=5)
        tk.Entry(form_frame, textvariable=self.roll_var, width=30).grid(row=2, column=1, pady=5)

        # Email
        tk.Label(form_frame, text="Email:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", pady=5)
        tk.Entry(form_frame, textvariable=self.email_var, width=30).grid(row=3, column=1, pady=5)

        # Course
        tk.Label(form_frame, text="Course:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", pady=5)
        tk.Entry(form_frame, textvariable=self.course_var, width=30).grid(row=4, column=1, pady=5)

        # Buttons Frame
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="Submit", width=12, command=self.submit_data).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Clear", width=12, command=self.clear_form).grid(row=0, column=1, padx=10)

    def submit_data(self):
        name = self.name_var.get().strip()
        age = self.age_var.get().strip()
        roll = self.roll_var.get().strip()
        email = self.email_var.get().strip()
        course = self.course_var.get().strip()

        # Basic validation
        if not name or not age or not roll or not email or not course:
            messagebox.showwarning("Validation Error", "All fields are required.")
            return

        if not age.isdigit():
            messagebox.showwarning("Validation Error", "Age must be a number.")
            return

        # You can add more validation like email format here

        # For now, just show success message
        messagebox.showinfo("Success", f"Data submitted:\nName: {name}\nAge: {age}\nRoll No: {roll}\nEmail: {email}\nCourse: {course}")

        # You might want to save the data to a file or database here

        self.clear_form()

    def clear_form(self):
        self.name_var.set("")
        self.age_var.set("")
        self.roll_var.set("")
        self.email_var.set("")
        self.course_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentDataEntryApp(root)
    root.mainloop()
