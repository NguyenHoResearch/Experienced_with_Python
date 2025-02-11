"""-----What will I learn in this project-----
- 1. What are CSV Files?
- 2. Reading CSV Files
- 3. Writing to CSV Files
- 4. Using the csv Module
- 5. Project 17: Student Report Generator
"""

# %% 1. What are CSV Files?
# CSV or comma separated values files are plain text files that store tabular data.
# Commonly used in spreadsheets, databases and data analysis.
""" 
Name, Math, Science, English
Alice, 85,90,88
Bob, 75,80,72
Charlie, 95,98,97
"""

# %% 2. Reading CSV Files
import csv

# Reading a csv file 
with open('students.csv', 'r') as file:
  reader = csv.reader(file)
  for row in reader:
    print(row)

# Reading a file into a dictionary.
with open('students.csv', 'r') as file:
  reader = csv.DictReader(file)
  for row in reader:
    print(row)

#%% 3. Writing to CSV Files
import csv

with open('new_students_v1.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(['Name', 'Math', 'Science', 'English'])
  writer.writerow(['Daisy', 88, 92, 85])

with open('new_students_v2.csv', 'w', newline='') as file:
  writer = csv.DictWriter(file, fieldnames=['Name', 'Math', 'Science', 'English'])
  writer.writeheader()
  writer.writerow({'Name': 'Eve', 'Math': 91, 'Science': 87, 'English': 90})

# %% 4. Using the csv Module
# The csv Module used: csv.reader(), csv.writer(), csv.DictWriter(). 

# %% 5. Project 17: Student Report Generator
import csv

# Step 1: Read student data and calculate avergaes
def process_student_data(input_file, output_file):
  try:
    with open(input_file, 'r') as infile:
      reader = csv.DictReader(infile)
      student_reports = []

      for row in reader:
        name = row['Name']
        math = int(row['Math'])
        science = int(row['Science'])
        english = int(row['English'])
        average = round((math + science + english) / 3, 2)
        status = "Pass" if average >= 60 else "Fail"

        student_reports.append({
          'Name': name,
          'Math': math,
          'Science': science,
          'English': english,
          'Average': average,
          'Status': status
        })

    # Step 2: Write processed data to a new CSV
    with open(output_file, 'w', newline='') as outfile:
      fieldnames = ["Name", "Math", "Science", "English", "Average", "Status"]
      writer = csv.DictWriter(outfile, fieldnames=fieldnames)
      writer.writeheader()
      writer.writerows(student_reports)

    print(f"Student report generated in {output_file} successfully.")

  except FileNotFoundError:
    print(f"Error: File {input_file} not found")
  except KeyError:
    print("Error: Invalid column names in the input file")
  except Exception as e:
    print(f"An error occurred: {e}")

# Main Program
input_file = "/Users/nguyenho/Desktop/Experienced_with_Python/Practices/Working_with_data/project_17/students.csv"
output_file = "/Users/nguyenho/Desktop/Experienced_with_Python/Practices/Working_with_data/project_17/student_report.csv"

process_student_data(input_file, output_file)
# %%
