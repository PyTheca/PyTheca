# Date 2023-12-02




# parameters

root_folder = "files"
line_length = 80
question_end = ": "




# import the neccesary modules

import files.introduction.random_sentence_generator as introduction_sentence
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




# say hello to customer

print("_" * line_length)
print(introduction_sentence.generate())
print("_" * line_length)




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
    
    return (str(final_results))




# collect all required answers

def collect_answers(questions):

    print(str(counter) + " The input parameters: ")
    print()

    answer_list = input("\t" + questions[0]+ question_end)

    for item in range (1, len(questions)):
        answer = input("\t" + questions[item]+ question_end)
        answer_list = answer_list + "," + answer

    return(answer_list)




# interface function

def main():

    #### rootfolder = "files"
    
    print()
    
    my_module = "/" + input(str(counter) + " Module: \t\t").replace(" ", "") + "." ### added "/" and "."
    print()

    # importing and evaluating the module
    
    try:
        
        module_path = (find_module(my_module)).replace("/", ".").replace("['", "").replace("']", "")

        imported_module = importlib.import_module(module_path)

    except:
        print(str(counter) + " Warning: \t\tplease be more specific in your module name!")
        print()

    # find and printing the help

    try:
        explain = eval("imported_module" + ".Explain()")
        print(str(counter) + " Explaination: \t" + explain)
        print()

    except:
        print(str(counter) + " Explaination: \t" + "not available!")
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
    print(str(counter) + " Result: \t\t" + myresult)

    print()
    print(str(counter) + " Duration: \t\t" + duration + " ms")
    print("_" * line_length)




# starting and looping the interface function, with restarting after an error

for counter in range(1, 1000000):
    try:
        main()
        
    except Exception as error_message :
        print()
        ### print(str(counter) + " Error message: \t" + str(error_message) + ".")
        ### print()
        print(str(counter) + " Advice: \t\tan existing module or parameter(s) should be specified, or the module has programming errors.")
        print()
        print("_" * line_length)




# end of file
