import tkinter as tk
from tkinter import messagebox

def calculate_result():
    student_name = entry_name.get()
    ADE_marks = int(entry_ade.get())
    Eco_marks = int(entry_eco.get())
    maths_marks = int(entry_maths.get())
    dbms_marks = int(entry_dbms.get())
    python_marks = int(entry_python.get())

    pass_mark = 33

    total_marks = ADE_marks + Eco_marks + maths_marks + dbms_marks + python_marks
    average_marks = total_marks / 5.0

    result_text = ""
    result_text += "-----------------------------------------\n"
    result_text += "Report Card\n"
    result_text += f"Report Card: {student_name}\n"
    result_text += "School Name: ADYPU    YEAR: 2023\n"
    result_text += "-----------------------------------------\n"
    result_text += "SUBJECT\t\tMARKS\t\tMAX\tPASS/FAIL\n"
    result_text += "-----------------------------------------\n"

    def append_subject(subject, marks):
        nonlocal result_text
        result = "PASS" if marks >= pass_mark else "FAIL"
        result_text += f"{subject}\t\t{marks}\t\t100\t{result}\n"

    append_subject("ADE", ADE_marks)
    append_subject("Eco", Eco_marks)
    append_subject("Maths", maths_marks)
    append_subject("DBMS", dbms_marks)
    append_subject("Python", python_marks)

    result_text += "-----------------------------------------\n"
    result_text += f"Total={total_marks}      Average={average_marks}\n"

    if (
        ADE_marks >= pass_mark
        and Eco_marks >= pass_mark
        and maths_marks >= pass_mark
        and dbms_marks >= pass_mark
        and python_marks >= pass_mark
    ):
        result_text += "PASS\n"
    else:
        result_text += "FAIL\n"

    result_text += "-----------------------------------------\n"

    if (
        ADE_marks <= pass_mark and Eco_marks >= pass_mark and maths_marks >= pass_mark
    ):
        result_text += "You failed in ADE\n"
    elif (
        ADE_marks >= pass_mark and Eco_marks <= pass_mark and maths_marks >= pass_mark
    ):
        result_text += "You failed in Eco\n"
    elif (
        ADE_marks >= pass_mark and Eco_marks >= pass_mark and maths_marks <= pass_mark
    ):
        result_text += "You failed in Mathematics\n"
    elif dbms_marks <= pass_mark and python_marks <= pass_mark:
        result_text += "You Failed in DBMS and Python\n"
    elif dbms_marks >= pass_mark and python_marks <= pass_mark:
        result_text += "You Failed in Python\n"
    elif dbms_marks <= pass_mark and python_marks >= pass_mark:
        result_text += "You Failed in DBMS\n"
    elif (
        ADE_marks <= pass_mark
        and Eco_marks <= pass_mark
        and maths_marks <= pass_mark
        and dbms_marks <= pass_mark
        and python_marks <= pass_mark
    ):
        result_text += "Failed\n"
    else:
        result_text += "Pass\n"

    result_text += "-----------------------------------------\n"

    output_file_path = entry_output_file.get()

    try:
        with open(output_file_path, "w") as file:
            file.write(result_text)
        messagebox.showinfo("Success", f"Result has been saved to {output_file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create main window
root = tk.Tk()
root.title("Student Result Calculator")

# Create and place widgets
label_name = tk.Label(root, text="Enter student name:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_ade = tk.Label(root, text="Enter marks in ADE:")
label_ade.pack()

entry_ade = tk.Entry(root)
entry_ade.pack()

label_eco = tk.Label(root, text="Enter marks in Eco:")
label_eco.pack()

entry_eco = tk.Entry(root)
entry_eco.pack()

label_maths = tk.Label(root, text="Enter marks in Maths:")
label_maths.pack()

entry_maths = tk.Entry(root)
entry_maths.pack()

label_dbms = tk.Label(root, text="Enter marks in DBMS:")
label_dbms.pack()

entry_dbms = tk.Entry(root)
entry_dbms.pack()

label_python = tk.Label(root, text="Enter marks in Python:")
label_python.pack()

entry_python = tk.Entry(root)
entry_python.pack()

label_output_file = tk.Label(root, text="Enter output file name:")
label_output_file.pack()

entry_output_file = tk.Entry(root)
entry_output_file.pack()

calculate_button = tk.Button(root, text="Calculate Result", command=calculate_result)
calculate_button.pack()

# Start the main loop
root.mainloop()
