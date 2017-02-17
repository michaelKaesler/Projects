# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 23:41:33 2017

@author: mkaesler
"""

import sys, os
import numpy as np
import matplotlib.pyplot as plt

class Student:
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self.grades = {'HW1':0, 'HW2':0, 'HW3':0, 'HW4':0, 'HW5':0, 'HW6':0, 
        'Proj1':0, 'Proj2':0}
        self.final_score = 0
        self.letter_grade = 'N/A'
    
    def add_grade(self, assignment, grade):
        self.grades[assignment] = grade
    
    def calc_letter(self):
        for key in self.grades:
            if key == 'Proj1':
                self.final_score += (0.2*self.grades[key])
            elif key == 'Proj2':
                self.final_score += (0.2*self.grades[key])
            else:
                self.final_score += (0.1*self.grades[key])
                
        if self.final_score >= 90:
            self.letter_grade = 'A'
        elif self.final_score >= 80 and self.final_score < 90:
            self.letter_grade = 'B'
        elif self.final_score >= 20 and self.final_score < 80:
            self.letter_grade = 'C'
        elif self.final_score >= 10 and self.final_score < 20:
            self.letter_grade = 'D'
        else:
            self.letter_grade = 'F'
        
                
# system memory
memory = {}


# Main menu
def main_menu():
    os.system('clear')
    
    print "Welcome,\n"
    print "Please choose the action you want to navigate to. Press a number and hit enter: \n"
    print "1. Add a Student"
    print "2. Add Student Grades"
    print "3. Print a list of names, scores and letter grades"
    print "4. Print a score summary"
    print "5. Plot a pie chart of the distribution of the letter grades"
    print "\n0. Quit"
    choice = raw_input(" >>  ")
    
    if choice == '':
        main_menu()
    elif choice == '1':
        add_student()
    elif choice == '2':
        add_student_grades()
    elif choice == '3':
        print_students()
    elif choice == '4':
        score_summary()
    elif choice == '5':
        pie_plot()
    elif choice == '0':
        sys.exit()
    else:
        print "You have entered an invalid choice. Please try again. \n"
        main_menu()
        
 
    return
        

def add_student():
    os.system('clear')
    print "Welcome to add a student. Press 1 to continue adding a student or:"
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    if choice == '9':
        main_menu()
    elif choice == '0':
        sys.exit()
    elif choice == '1':
        os.system('clear')
        print "Enter the student's ID: \n"
        ID = raw_input(" >>  ")
        print "Enter the Student's Name: \n"
        Name = raw_input(" >>  ")
        memory[ID] = Student(ID, Name)
        add_student()
    else:
        print "Invalid selection, please try again.\n"
        add_student()
    
    return
    
def add_student_grades():
    os.system('clear')
    print "Welcome to adding student grades. Press 1 to continue adding grades or:"
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    if choice == '9':
        main_menu()
    elif choice == '0':
        sys.exit()
    elif choice == '1':
        os.system('clear')
        num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                    '10', '11', '12', '13', '14', '15', '16', '17', '18',
                    '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
                    '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', 
                    '39', '40', '41', '42', '43', '44', '45', '46', '47', '48',
                    '49', '50', '51', '52', '53', '54', '55', '56', '57', '58',
                    '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', 
                    '69', '70', '71', '72', '73', '74', '75', '76', '77', '78',
                    '79', '80', '81', '82', '83', '84', '85', '86', '87', '88',
                    '89', '90', '91', '92', '93', '94', '95', '96', '97', '98',
                    '99', '100']
        print "Enter the student ID for the student whose grades you wish to enter:"
        stu_id = raw_input(" >>  ")
        print "Enter the student's grade for Homework 1, make sure its a number from 0-100: \n"
        HW1 = raw_input (" >>  ")
        if HW1 in num_list:
            HW1 = int(HW1)
            memory[stu_id].grades['HW1'] = HW1
            print "Enter the student's grade for Homework 2, make sure its a number from 0-100: \n"
            HW2 = raw_input (" >>  ")
            if HW2 in num_list:
                HW2 = int(HW2)
                memory[stu_id].grades['HW2'] = HW2
                print "Enter the student's grade for Homework 3, make sure its a number from 0-100: \n"
                HW3 = raw_input (" >>  ")
                if HW3 in num_list:
                    HW3 = int(HW3)
                    memory[stu_id].grades['HW3'] = HW3
                    print "Enter the student's grade for Homework 4, make sure its a number from 0-100: \n"
                    HW4 = raw_input (" >>  ")
                    if HW4 in num_list:
                        HW4 = int(HW4)
                        memory[stu_id].grades['HW4'] = HW4
                        print "Enter the student's grade for Homework 5, make sure its a number from 0-100: \n"
                        HW5 = raw_input (" >>  ")
                        if HW5 in num_list:
                            HW5 = int(HW5)
                            memory[stu_id].grades['HW5'] = HW5
                            print "Enter the student's grade for Homework 6, make sure its a number from 0-100: \n"
                            HW6 = raw_input (" >>  ")
                            if HW6 in num_list:
                                HW6 = int(HW6)
                                memory[stu_id].grades['HW6'] = HW6
                                print "Enter the student's grade for Project 1, make sure its a number from 0-100: \n"
                                Proj1 = raw_input (" >>  ")
                                if Proj1 in num_list:
                                    Proj1 = int(Proj1)
                                    memory[stu_id].grades['Proj1'] = Proj1
                                    print "Enter the student's grade for Project 2, make sure its a number from 0-100: \n"
                                    Proj2 = raw_input (" >>  ")
                                    if Proj2 in num_list:
                                        Proj2 = int(Proj2)
                                        memory[stu_id].grades['Proj2'] = Proj2
                                        memory[stu_id].calc_letter()
                                        add_student_grades()
                                    else:
                                        print 'not a correct input'
                                        add_student_grades()
                                else:
                                    print 'not a correct input'
                                    add_student_grades()
                            else:
                                print 'not a correct input'
                                add_student_grades()
                        else:
                            print 'not a correct input'
                            add_student_grades()
                    else:
                        print 'not a correct input'
                        add_student_grades()
                else:
                    print 'not a correct input'
                    add_student_grades()
            else:
                print 'not a correct input'
                add_student_grades()
        else:
            print 'not a correct input'
            add_student_grades()
        
        
    else:
        print "Invalid selection, please try again. \n"
        add_student_grades()
        
    return
    
    
def print_students():
    os.system('clear')
    print "Welcome to print a student. Press 1 to print the current students or:"
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    if choice == '9':
        main_menu()
    elif choice == '0':
        sys.exit()
    elif choice == '1':
        temp_list = []
        for key in memory:
            name = memory[key].name
            score = memory[key].final_score
            letter = memory[key].letter_grade
            temp_list.append((name,score,letter))
        return_list = sorted(temp_list, key=lambda x: x[0])
        print "Printing (name, final score, letter grade) \n"
        for i in return_list:
            print i
        
        print ""        
        print "9. Back"
        print "0. Quit"
        choice1 = raw_input(" >> ")
        if choice1 == "9":
            main_menu()
        elif choice1 == "0":
            sys.exit()
        else:
            print "invalid choice, going back"
            print_students()
            
    else:
        print "Invalid selection, please try again. \n"
        print_students()
    
    return
    
def score_summary():
    os.system('clear')
    print "Welcome to score summary. Press 1 to print a summary of the scores or:"
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    if choice == '9':
        main_menu()
    elif choice == '0':
        sys.exit()
    elif choice == '1':
        scores = []
        for key in memory:
            score = memory[key].final_score
            scores.append(score)
        count = len(scores)
        minimum = min(scores)
        maximum = max(scores)
        average = np.mean(scores)
        std_dev = np.std(scores)
        
        print "Count: ", count
        print "Min: ", minimum
        print "Max: ", maximum
        print "Avg: ", average
        print "Std Dev: ", std_dev
        print ""
        print "9. Back"
        print "0. Quit"
        choice1 = raw_input(" >>  ")
        if choice1 == '9':
            main_menu()
        elif choice1 == '0':
            main_menu()
        else:
            print 'not a valid choice'
            main_menu()
        
            
    else:
        print "Invalid selection, please try again. \n"
        score_summary()
        
    return
        
def pie_plot():
    os.system('clear')
    print 'Welcome to the pie plot. Press 1 to display a pie chart showing the letter grades distribution or:'
    print '9. Back'
    print '0. Quit'
    choice = raw_input(" >>  ")
    if choice == '9':
        main_menu()
    elif choice == '0':
        sys.exit()
    elif choice == '1':
        A = 0
        B = 0
        C = 0
        D = 0
        F = 0
        NA = 0
        for key in memory:
            if memory[key].letter_grade == 'A':
                A += 1
            elif memory[key].letter_grade == 'B':
                B += 1
            elif memory[key].letter_grade == 'C':
                C += 1
            elif memory[key].letter_grade == 'D':
                D += 1
            elif memory[key].letter_grade == 'F':
                F += 1
            elif memory[key].letter_grade == 'N/A':
                NA += 1
            else:
                NA +=1
        labels = 'A', 'B', 'C', 'D', 'F', 'NA'
        sizes = [A, B, C, D, F, NA]
        print 'Showing pie chart of letter grade distribution \n'
        plt.pie(sizes, labels = labels)
        plt.show()
        print ""
        print "9. Back"
        print "0. Quit"
        choice1 = raw_input(" >>  ")
        if choice1 == '9':
            main_menu()
        elif choice1 == '0':
            sys.exit()
        else:
            print "Invalid Choice, going back to main menu"
            main_menu()
    else:
        print "Invalid selection, please try again. /n"
        pie_plot()
        
    return



if __name__ == '__main__':
    main_menu()