# System for Progress Academy to automate their student ranking using Average Test Score and Progress Score
# Subroutine for the main program
import sys

def Progress_Academy():
    # Subroutine for the menu of the system that allows the end user to select which program to launch
    def menu():
        print("\nEnter 1 for the average score calculator\nEnter 2 for the progress score calculator\nEnter 3 for the score lookup function")
        menu_selection = input("Input: ")
        if menu_selection == '1':
            # Executes the average score calculator subroutine
            Average_Score()
        elif menu_selection == '2':
            # Executes the progress score calculator subroutine
            Progress_Score()
        elif menu_selection == '3':
            Lookup_Function()
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
            print("\nSYSTEM QUIT")
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
        # menu option that allows the user to keep on going or go back to menu
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
            print("\nSYSTEM QUIT")
            sys.exit()

    # Subroutine for added lookup feature. End user can lookup a student's number and look at either their average or progress score
    def Lookup_Function():
        student_lookup = (input("\nPlease enter a student's number you would like the scores of: "))
        if student_lookup == '':
            print("\nInvalid input")
            Lookup_Function()
        student_number_criteria = "Student " + str(student_lookup)
        # File containing all student numbers and their scores
        lookup_file = open('lookupfile.txt','r')
        # Loop that validates the existence of the student number and ensures only valid numbers are entered
        flag = 0
        criteria_index = 0
        # Loop to search through file and find location of the specific student number being looked for
        for line in lookup_file:
            criteria_index += 1
            if student_number_criteria in line:
                flag = 1
                break
        if flag == 0:
            print('Student number', student_lookup, 'is not valid')
            lookup_file.close()
            Lookup_Function()
        else:
            print('Student number', student_lookup, 'is valid')
            lookup_file.close()
        # Allows end user to pick whether they want to see the average score or the progress score of the student
        print("\nEnter 1 for the average score of student",student_lookup,"\nEnter 2 for the progress score of student",student_lookup)
        lookup_selection = input("Input: ")
        if lookup_selection == '1':
            average_line = criteria_index
            lookup_average_file = open('lookupfile.txt')
            entire_file = lookup_average_file.readlines()
            print(entire_file[average_line])
            # Subroutine that allows the user to pick their next option
            menu_option()
        elif lookup_selection == '2':
            progress_line = criteria_index + 1
            lookup_progress_file = open('lookupfile.txt')
            all_file = lookup_progress_file.readlines()
            print(all_file[progress_line])
            menu_option()
        else:
            print("\nInvalid input")
            # If they have not selected a valid option then it will loop back to the beginning of the subroutine
            Lookup_Function()

    # Subroutine designed to allow the user to pick their next action following the lookup function
    def menu_option():
        print("\nEnter 1 to lookup another student's scores\nEnter 2 to go back to the main menu\nEnter any other key to quit")
        menu_selection = input("Input: ")
        if menu_selection == '1':
            # Executes the look up subroutine that allows the user to look up a student's scores
            Lookup_Function()
        elif menu_selection == '2':

            # Executes the menu subroutine that allows the user to go back to the main menu
            menu()
        else:
            # No further subroutines are executed and the system gives the user a message to confirm their choice
            print("\nSYSTEM QUIT")
            sys.exit()

    menu()
Progress_Academy()

