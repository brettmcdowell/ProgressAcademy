# System for Progress Academy to automate their student ranking using Average Test Score and Progress Score
# Subroutine for the main program
import sys

def Progress_Academy():
    # Subroutine for the menu of the system that allows the end user to select which program to launch
    def menu():
        print("\nEnter 1 for the average score calculator\nEnter 2 for the progress score calculator")
        menu_selection = input("Input: ")
        if menu_selection == '1':
            # Executes the average score calculator subroutine
            Average_Score()
        elif menu_selection == '2':
            # Executes the progress score calculator subroutine
            Progress_Score()
        else:
            # Error handling method for invalid input
            print("Please enter a valid input")
            menu()

    # Subroutine for the average score calculator function referenced in Task 1
    def Average_Score():
        # Class that calculates the average score of a student using three subject scores
        class AverageScore:
            def __init__(self, maths_actual, english_actual, science_actual):
                # Initialising three key variables used in calculations
                self.maths_actual = maths_actual
                self.english_actual = english_actual
                self.science_actual = science_actual

            # Subroutine that calculates the student's average score and returns the result
            def Average_calculation(self):
                average_total = (self.maths_actual + self.english_actual + self.science_actual) / 3
                average_total = round(average_total, 2)
                return "Student's average score is " + str(average_total)

        # Allows the end user to input the three scores of the student and then calculates and prints the average score
        maths_actual = int(input("\nPlease enter the student's maths score out of 100: "))
        if maths_actual > 100:
            print("Value too large")
            Average_Score()
        english_actual = int(input("Please enter the student's english score out of 100: "))
        if english_actual > 100:
            print("Value too large")
            Average_Score()
        science_actual = int(input("Please enter the student's science score out of 100: "))
        if science_actual > 100:
            print("Value too large")
            Average_Score()
        average_score_final = AverageScore(maths_actual, english_actual, science_actual)
        print(AverageScore.Average_calculation(average_score_final))
        print("\nPlease enter 1 to calculate another average score\nPlease enter 2 to go back to the menu\nPlease enter any other key to quit")
        continue_option = input("Input: ")
        if continue_option == '1':
            Average_Score()
        elif continue_option == '2':
            menu()
        else:
            sys.exit()

    # Subroutine for the progress score calculator function referenced in Task 2
    def Progress_Score():
        # Class that calculates the progress score of a student using mock and actual scores for three subjects
        class ProgressScore:
            def __init__(self, maths_mock, maths_actual, english_mock, english_actual, science_mock, science_actual):
                # Initialising six key variables used in calculations
                self.maths_mock = maths_mock
                self.maths_actual = maths_actual
                self.english_mock = english_mock
                self.english_actual = english_actual
                self.science_mock = science_mock
                self.science_actual = science_actual

            # Subroutine that calculates the student's progress score and returns the result
            def Progress_calculation(self):
                maths_progress = (self.maths_actual - self.maths_mock) / 10
                english_progress = (self.english_actual - self.english_mock) / 10
                science_progress = (self.science_actual - self.science_mock) / 10
                average_progress = (maths_progress + english_progress + science_progress) / 3
                average_progress = round(average_progress, 2)
                return "Student's average progress score is " + str(average_progress)

        # Allows end user to input the scores of the student and then calculates and prints the progress score
        maths_mock = int(input("\nPlease enter the student's mock maths score out of 100: "))
        if maths_mock > 100:
            print("Value too large")
            Progress_Score()
        maths_actual = int(input("Please enter the student's actual maths score out of 100: "))
        if maths_actual > 100:
            print("Value too large")
            Progress_Score()
        english_mock = int(input("Please enter the student's mock english score out of 100: "))
        if english_mock > 100:
            print("Value too large")
            Progress_Score()
        english_actual = int(input("Please enter the student's actual english score out of 100: "))
        if english_actual > 100:
            print("Value too large")
            Progress_Score()
        science_mock = int(input("Please enter the student's mock science score out of 100: "))
        if science_mock > 100:
            print("Value too large")
            Progress_Score()
        science_actual = int(input("Please enter the student's actual science score out of 100: "))
        if science_actual > 100:
            print("Value too large")
            Progress_Score()
        progress_score_final = ProgressScore(maths_mock, maths_actual, english_mock, english_actual, science_mock, science_actual)
        print(ProgressScore.Progress_calculation(progress_score_final))
        print("\nPlease enter 1 to calculate another progress score\nPlease enter 2 to go back to the menu\nPlease enter any other key to quit")
        continue_option = input("Input: ")
        if continue_option == '1':
            Progress_Score()
        elif continue_option == '2':
            menu()
        else:
            sys.exit()
    menu()
Progress_Academy()
