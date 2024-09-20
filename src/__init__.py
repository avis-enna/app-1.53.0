import csv
import random
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='exam_client.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

QUESTIONS_FILE = 'questions.csv'

class Question:
    def __init__(self, num, question, option1, option2, option3, option4, correctoption):
        self.num = num
        self.question = question
        self.options = {
            'op1': option1,
            'op2': option2,
            'op3': option3,
            'op4': option4
        }
        self.correctoption = correctoption

    def display_question(self):
        print(f"\nQuestion {self.num}: {self.question}")
        option_list = list(self.options.items())
        random.shuffle(option_list)
        for i, (key, value) in enumerate(option_list, start=1):
            print(f"{i}) {value}")
        return option_list

    def check_answer(self, user_answer, shuffled_options):
        correct_answer = shuffled_options[int(user_answer)-1][0]
        return correct_answer == self.correctoption

class Exam:
    def __init__(self, student_name, university):
        self.student_name = student_name
        self.university = university
        self.questions = self.load_questions()
        self.score = 0

    def load_questions(self):
        questions = []
        try:
            with open(QUESTIONS_FILE, mode='r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    questions.append(
                        Question(row['num'], row['question'], row['option1'],
                                 row['option2'], row['option3'], row['option4'],
                                 row['correctoption'])
                    )
            logging.info("Questions loaded successfully.")
        except FileNotFoundError:
            logging.error(f"{QUESTIONS_FILE} not found.")
            print(f"Error: {QUESTIONS_FILE} not found.")
        except Exception as e:
            logging.error(f"An error occurred while loading questions: {e}")
            print(f"An error occurred while loading questions: {e}")
        return questions

    def start_exam(self):
        random.shuffle(self.questions)
        for question in self.questions:
            shuffled_options = question.display_question()
            while True:
                try:
                    user_answer = input("Enter your choice (1, 2, 3, 4): ")
                    if user_answer not in ['1', '2', '3', '4']:
                        raise ValueError("Invalid choice, please enter a number between 1 and 4.")
                    if question.check_answer(user_answer, shuffled_options):
                        self.score += 1
                    break
                except ValueError as ve:
                    logging.warning(ve)
                    print(ve)

        self.display_results()

    def display_results(self):
        print("\nExam Completed!")
        print(f"Student name = {self.student_name}")
        print(f"University   = {self.university}")
        print(f"Marks-scored = {self.score} correct out of {len(self.questions)} questions")
        logging.info(f"Exam completed for {self.student_name} from {self.university}. Score: {self.score}/{len(self.questions)}")

def main():
    # Display today's date and time
    current_datetime = datetime.now().strftime("%d/%b/%Y %H:%M:%S")
    print(f"Today's date and time: {current_datetime}")

    # Get student details
    student_name = input("Enter student name: ")
    university = input("Enter university: ")

    # Start the exam
    exam = Exam(student_name, university)
    exam.start_exam()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.critical(f"Critical error: {e}")
        print(f"An unexpected error occurred: {e}")