# 9.1 - Writing Grades to a Plain Text File

def write_grades_to_file(filename):
    # Open the file in append mode
    with open(filename, "a") as file:
        while True:
            # Prompt user for input
            grade = input("Enter a grade (or -1 to quit): ")
            if grade == "-1":
                break
            # Write the grade to the file with a newline
            file.write(f"{grade}\n")
            
write_grades_to_file("grades.txt")


