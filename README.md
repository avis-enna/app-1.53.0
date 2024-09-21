# MCQ Based Online Exam Application

## Overview
This project consists of two Python scripts, `question_master.py` and 
`exam_client.py`, designed to manage and take multiple-choice questions (MCQ) 
exams. The questions are stored in a CSV file named `questions.csv`.

- **`question_master.py`**: Allows administrators to add, search, delete, modify, and 
display questions.
- **`exam_client.py`**: Allows students to take the exam and see their results.

## Files
- **`questions.csv`**: The file where questions are stored in the following format:


      num,question,option1,option2,option3,option4,correctoption
      1,10+20 ans is,op1=20,op2=30,op3=40,op4=10,op2
      2,20-10 ans is,op1=20,op2=30,op3=40,op4=10,op4
      3,2*2 ans is,op1=4,op2=5,op3=6,op4=7,op1


 Question_master

### Description
This script allows administrators to manage the questions in the `questions.csv` file. 
The available operations are:
1. Add a question
2. Search for a question by question number
3. Delete a question by question number
4. Modify a question by question number
5. Display all questions
6. Exit menu

### Usage
Run the script using Python:

      python question_master.py


Menu Options
	•	Add a question: Adds a new question to the CSV file.
	•	Search for a question: Searches for a question based on the question 
number.
	•	Delete a question: Deletes a question based on the question number.
	•	Modify a question: Modifies an existing question based on the question 
number.
	•	Display all questions: Displays all the questions in the CSV file.
	•	Exit menu: Exits the menu.


exam_client.py

Description

This script allows students to take an MCQ exam. It reads questions from the 
questions.csv file and administers the test.
Usage

Run the script using Python:

		python exam_client.py


Workflow
	1.	Displays the current date and time.
	2.	Prompts the student to enter their name and university.
	3.	Displays each question with options and prompts the student to enter 
their choice.
	4.	At the end of the test, displays the student's name, university, and score.

Example

When the script is run, the following sample screen is displayed:

Display
Today's date and time: 15/Sep/2024 12.46.30

Enter student name    : *****
Enter university      : cisco

1) 10+20 is equal what?
   op1) 20
   op2) 30
   op3) 40
   op4) 10
Enter your choice:

On completion of the test, the following details are displayed:
Student name = *****
University   = cisco
Marks-scored = 8 correct out of 10 questions

Logging

Both scripts use logging to record informational messages and errors. The logs provide a 
record of events and can help in troubleshooting issues.
Exception Handling

The scripts are designed to handle exceptions gracefully. For instance, if the 
questions.csv file is not found, an appropriate error message is logged.
Requirements

	•	Python 3.x
	•	questions.csv file in the correct format



