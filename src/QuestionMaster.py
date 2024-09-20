import csv
import json
import shutil
from datetime import datetime

QUESTIONS_FILE = 'questions.csv'
BACKUP_FILE = 'questions_backup.csv'


def read_questions():
    questions = []
    with open(QUESTIONS_FILE, mode='w') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            questions.append(row)
    return questions


def write_questions(questions):
    with open(QUESTIONS_FILE, mode='w', newline='') as file:
        fieldnames = ['num', 'question', 'option1', 'option2', 'option3', 'option4', 'correctoption']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for question in questions:
            writer.writerow(question)


def backup_questions():
    shutil.copy(QUESTIONS_FILE, BACKUP_FILE)
    print("Backup successful.")


def restore_questions():
    shutil.copy(BACKUP_FILE, QUESTIONS_FILE)
    print("Restore successful.")


def export_questions_to_json():
    questions = read_questions()
    with open('questions.json', 'w') as json_file:
        json.dump(questions, json_file, indent=4)
    print("Export to JSON successful.")


def add_question():
questions = read_questions()
    num = len(questions) + 1
    question = input("Enter the question: ")
    option1 = input("Enter option 1: ")
    option2 = input("Enter option 2: ")
    option3 = input("Enter option 3: ")
    option4 = input("Enter option 4: ")
    correctoption = input("Enter correct option (op1, op2, op3, op4): ")

    questions.append({
        'num': num,
        'question': question,
        'option1': option1,
        'option2': option2,
        'option3': option3,
        'option4': option4,
        'correctoption': correctoption
    })

    write_questions(questions)
    print(f"Question {num} added successfully.")


def search_question(num):
    questions = read_questions()
    for question in questions:
        if question['num'] == str(num):
            print(question)
            return
    print(f"Question {num} not found.")


def delete_question(num):
    questions = read_questions()
    questions = [question for question in questions if question['num'] != str(num)]
    write_questions(questions)
    print(f"Question {num} deleted successfully.")


def modify_question(num):
    questions = read_questions()
    for question in questions:
        if question['num'] == str(num):
            question['question'] = input("Enter new question: ")
            question['option1'] = input("Enter new option 1: ")
            question['option2'] = input("Enter new option 2: ")
            question['option3'] = input("Enter new option 3: ")
            question['option4'] = input("Enter new option 4: ")
            question['correctoption'] = input("Enter new correct option (op1, op2, op3, op4): ")
            write_questions(questions)
            print(f"Question {num} modified successfully.")
            return
    print(f"Question {num} not found.")


def display_questions():
    questions = read_questions()
    for question in questions:
        print(question)


def main():
    while True:
        print("\n1) Add a question")
        print("2) Search for a question")
        print("3) Delete a question")
        print("4) Modify a question")
        print("5) Display all questions")
        print("6) Backup questions")
        print("7) Restore questions")
        print("8) Export questions to JSON")
        print("9) Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_question()
        elif choice == '2':
            num = input("Enter question number to search: ")
            search_question(num)
        elif choice == '3':
            num = input("Enter question number to delete: ")
            delete_question(num)
        elif choice == '4':
            num = input("Enter question number to modify: ")
            modify_question(num)
        elif choice == '5':
            display_questions()
        elif choice == '6':
            backup_questions()
        elif choice == '7':
            restore_questions()
        elif choice == '8':
            export_questions_to_json()
        elif choice == '9':
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()