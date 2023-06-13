# Date 2023-05-02



# parameters

root_folder = "files"
line_length = 80



# import the neccesary modules

import importlib
import os
import time



# introduction

print()
print("**************************************************")
print("**************************************************")
print("**  Welcome to                                  **")
print("**                                              **")
print("**  ****  *   * ***** *   * *****  ***   ***    **")
print("**  *   * *   *   *   *   * *     *   * *   *   **")
print("**  *   *  * *    *   *   * *     *     *   *   **")
print("**  ****    *     *   ***** ***** *     *****   **")
print("**  *       *     *   *   * *     *     *   *   **")
print("**  *       *     *   *   * *     *   * *   *   **")
print("**  *       *     *   *   * *****  ***  *   *   **")
print("**                                              **")
print("**  The world smallest Python Operating System  **")
print("**************************************************")
print("**************************************************")
print()



# find module

def find_module(my_module):    

    # creating a modules list from the package folder
    directory_folder_list = os.listdir(root_folder)


    fullpaths = map(lambda name: os.path.join(root_folder, name), directory_folder_list)

    path_of_directory_folder = []
    relative_path_to_all_files = []

    for item in fullpaths:
        if os.path.isdir(item): path_of_directory_folder.append(item)

    path_of_directory_folder.sort()

    for category in path_of_directory_folder:
        directory_folder_list_2 = os.listdir(category)
        fullpaths2 = map(lambda name: os.path.join(category, name), directory_folder_list_2)
        for item in fullpaths2:
            if os.path.isfile(item): relative_path_to_all_files.append(item)

    relative_path_to_all_files.sort()

    relative_path_to_found_files = [string for string in relative_path_to_all_files if (my_module in string and "._" not in string)]

    final_results = str(relative_path_to_found_files).replace(".py", "").replace("\\\\", ".")
    
    print(str(counter) + " Found modules: \t" + str(final_results))
    print()
    

    return (final_results)



# collect all required answers

def collect_answers(questions):

    question_total = len(questions)-1
 

    answer0 = []
    answer1 = []
    answer2 = []
    answer3 = []
    answer4 = []
    answer5 = []
    answer6 = []
    answer7 = []
    answer8 = []
    answer9 = []
    answer10 = []
    answer11 = []
    answer12 = []
    answer13 = []
    answer14 = []
    answer15 = []
    answer16 = []
     
    print(str(counter) + " The input parameters: ")
    print()
    
    if question_total >= 0:
        answer0 = input(questions[0])
        answer_list = answer0

    if question_total >= 1:
        answer1 = input(questions[1])
        answer_list = answer0 + "," + answer1
        
    if question_total >= 2:
        answer2 = input(questions[2])
        
        answer_list = answer0 + "," + answer1 + "," + answer2
        
    if question_total >= 3:
        answer3 = input(questions[3])
        answer_list = answer0 + "," + answer1 + "," + answer2 + "," + answer3

    if question_total >= 4:
        answer4 = input(questions[4])
        answer_list = answer0 + "," + answer1 + "," + answer2 + "," + answer3 + "," + answer4

    if question_total >= 5:
        answer5 = input(questions[5])
        answer_list = answer0 + "," + answer1 + "," + answer2 + "," + answer3 + "," + answer4 + "," + answer5

    if question_total >= 6:
        answer6 = input(questions[6])
        answer_list = answer0 + "," + answer1 + "," + answer2 + "," + answer3 + "," + answer4 + "," + answer5 + "," + answer6

    if question_total >= 7:
        answer7 = input(questions[7])
        answer_list = answer0 + "," + answer1 + "," + answer2 + "," + answer3 + "," + answer4 + "," + answer5 + "," + answer6 + "," + answer7

    if question_total >= 8:
        answer8 = input(questions[8])
        answer_list = answer0 + "," + answer1 + "," + answer2 + "," + answer3 + "," + answer4 + "," + answer5 + "," + answer6 + "," + answer7 + "," + answer8

    if question_total >= 9:
        answer9 = input(questions[9])
        answer_list = answer0 + "," + answer1 + "," + answer2 + "," + answer3 + "," + answer4 + "," + answer5 + "," + answer6 + "," + answer7 + "," + answer8 + "," + answer9

    if question_total >= 10:
        answer10 = input(questions[10])
        answer_list = answer0 + "," + answer1 + "," + answer2 + "," + answer3 + "," + answer4 + "," + answer5 + "," + answer6 + "," + answer7 + "," + answer8 + "," + answer9 + "," + answer10

    if question_total >= 11:
        answer11 = input(questions[11])
        answer_list = answer0 + "," + answer1 + "," + answer2 + "," + answer3 + "," + answer4 + "," + answer5 + "," + answer6 + "," + answer7 + "," + answer8 + "," + answer9 + "," + answer10 + "," + answer11

    if question_total >= 12:
        answer12 = input(questions[12])
        answer_list = answer0 + "," + answer1 + "," + answer2 + "," + answer3 + "," + answer4 + "," + answer5 + "," + answer6 + "," + answer7 + "," + answer8 + "," + answer9 + "," + answer10 + "," + answer11 + "," + answer12

    if question_total >= 13:
        answer13 = input(questions[13])
        answer_list = answer0 + "," + answer1 + "," + answer2 + "," + answer3 + "," + answer4 + "," + answer5 + "," + answer6 + "," + answer7 + "," + answer8 + "," + answer9 + "," + answer10 + "," + answer11 + "," + answer12 + "," + answer13

    if question_total >= 14:
        answer14 = input(questions[14])
        answer_list = answer0 + "," + answer1 + "," + answer2 + "," + answer3 + "," + answer4 + "," + answer5 + "," + answer6 + "," + answer7 + "," + answer8 + "," + answer9 + "," + answer10 + "," + answer11 + "," + answer12 + "," + answer13 + "," + answer14

    if question_total >= 15:
        answer15 = input(questions[15])
        answer_list = answer0 + "," + answer1 + "," + answer2 + "," + answer3 + "," + answer4 + "," + answer5 + "," + answer6 + "," + answer7 + "," + answer8 + "," + answer9 + "," + answer10 + "," + answer11 + "," + answer12 + "," + answer13 + "," + answer14 + "," + answer15

    if question_total >= 16:
        answer16 = input(questions[16])
        answer_list = answer0 + "," + answer1 + "," + answer2 + "," + answer3 + "," + answer4 + "," + answer5 + "," + answer6 + "," + answer7 + "," + answer8 + "," + answer9 + "," + answer10 + "," + answer11 + "," + answer12 + "," + answer13 + "," + answer14 + "," + answer15 + "," + answer16

    return(answer_list)



# interface function

def main():

    rootfolder = "files"
    
    print()
    
    my_module = input(str(counter) + " Module: \t\t\t").replace(" ", "")
    print()


    # importing and evaluating the module
    
    try:
        
        module_path = (find_module(my_module)).replace("/", ".").replace("['", "").replace("']", "")

        imported_module = importlib.import_module(module_path)

    except:
        print(str(counter) + " Warning: \t\t\tplease be more specific in your module name!")
        print()


    # find and printing the help

    try:
        explain = eval("imported_module" + ".Explain()")
        print(str(counter) + " Explaination: \t\t" + explain)
        print()

    except:
        print(str(counter) + " Explaination: \t\t" + "not available!")
        print()


    # find the questions UNDER DEVELOPMENT

    try:
        questions = eval("imported_module" + ".Questions()")

    except:
        print(str(counter) + " Questions: \t\t" + "not available!")


    # import data
    
    executable = "imported_module" + ".Execute(" + collect_answers(questions) + ")"

    start = time.time()
    
    myresult = str(eval(executable)) # important

    end = time.time()

    duration = str(round((end - start)*1000, 4))
    

    # printing all the results
    
    print()
    print(str(counter) + " Result: \t\t\t" + myresult)

    print()
    print(str(counter) + " Duration: \t\t\t" + duration + " ms")
    print("_" * line_length)



# starting and looping the interface function, with restarting after an error

for counter in range(1, 1000000):
    try:
        main()
        
    except Exception as error_message :
        print()
        print(str(counter) + " Error message: \t" + str(error_message) + ".")
        print()
        print(str(counter) + " Advice: \t\t\tan existing module or parameter should be specified.")
        print()
        print("_" * line_length)








# end of file
