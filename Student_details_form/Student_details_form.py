from tkinter import *
from os import system

system('cls')


def submit():
    student_data = [str(Student_first_name_entry.get()), str(Student_last_name_entry.get()),
                    str(Student_DOB_entry.get()), str(Student_Admission_no_entry.get())]

    if student_data[0:] == ["", "", "", ""]:
        return

    else:
        new_window = Tk()
        new_window.geometry("{}x{}+{}+{}".format(700, 300, 460, 200))
        new_window.config(bg="sky blue")
        window.destroy()

        title_label = Label(new_window, font=("Consolas", 25), text="Student's Details", bg="sky blue")
        title_label.place(x=100, y=0)

        Student_first_name_details = Label(new_window, font=("MV Boli", 15),
                                           text=f"Student's first name: {student_data[0]}", bg="sky blue")
        Student_first_name_details.place(x=0, y=100)

        Student_last_name_details = Label(new_window, font=("MV Boli", 15),
                                          text=f"Student's last name: {student_data[1]}", bg="sky blue")
        Student_last_name_details.place(x=0, y=150)

        Student_DOB_details = Label(new_window, font=("MV Boli", 15),
                                    text=f"Student's DOB in (DD/MM/YYYY): {student_data[2]}", bg="sky blue")
        Student_DOB_details.place(x=0, y=200)

        Student_Admission_no_details = Label(new_window, font=("MV Boli", 15),
                                             text=f"Student's Admission No. : {student_data[3]}", bg="sky blue")
        Student_Admission_no_details.place(x=0, y=250)

        new_window.mainloop()


window = Tk()
window.geometry("{}x{}+{}+{}".format(700, 350, 460, 200))
window.title("Student's detail form")
window.config(bg="sky blue")

Titlelabel = Label(window, text="Enter the students details", font=("consolas", 25, "bold"), bg="sky blue")
Titlelabel.place(x=100, y=0)

Student_first_name_label = Label(window, text="Student's first name:  ", font=("MV Boli", 15), bg="sky blue")
Student_first_name_label.place(x=0, y=100)
Student_first_name_entry = Entry(window, font=("MV Boli", 15), bg="sky blue")
Student_first_name_entry.place(x=215, y=100)

Student_last_name_label = Label(window, text="Student's last name:  ", font=("MV Boli", 15), bg="sky blue")
Student_last_name_label.place(x=0, y=150)
Student_last_name_entry = Entry(window, font=("MV Boli", 15), bg="sky blue")
Student_last_name_entry.place(x=215, y=150)

Student_DOB_label = Label(window, text="Student's DOB in (DD/MM/YYYY):  ", font=("MV Boli", 15), bg="sky blue")
Student_DOB_label.place(x=0, y=200)
Student_DOB_entry = Entry(window, font=("MV Boli", 15), bg="sky blue")
Student_DOB_entry.place(x=360, y=200)

Student_Admission_no_label = Label(window, text="Student's Admission No. :  ", font=("MV Boli", 15), bg="sky blue")
Student_Admission_no_label.place(x=0, y=250)
Student_Admission_no_entry = Entry(window, font=("MV Boli", 15), bg="sky blue")
Student_Admission_no_entry.place(x=270, y=250)

submitButton = Button(window, text="SUBMIT", font=("MV Boli", 13), bg="sky blue", activebackground="sky blue",
                      command=submit)
submitButton.place(x=300, y=310)

window.mainloop()
