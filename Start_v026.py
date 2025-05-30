# Date 2024-05-30

# parameters
root_folder = "files"
line_length = 80
question_end = ": "

# import the necessary modules
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

# Recursive function to find module files
def find_module(my_module):
    # create an empty list to store the file paths
    relative_path_to_all_files = []

    # os.walk will iterate over all the directories and subdirectories
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            # Only process .py files
            if file.endswith(".py"):
                # Get the base name of the file without the .py extension
                base_name = os.path.splitext(file)[0]
                
                # Now compare the base name exactly with my_module
                if base_name == my_module:
                    relative_path_to_all_files.append(os.path.join(root, file))

    relative_path_to_all_files.sort()

    # Format the file paths and return the result
    final_results = str(relative_path_to_all_files).replace(".py", "").replace("\\\\", ".")
    print(f"{counter} Found modules: \t{final_results}")    
    return final_results



# collect all required answers
def collect_answers(questions):
    print(f"{counter} The input parameters: ")
    print()

    answer_list = input(f"\t{questions[0]}{question_end}")

    for item in range(1, len(questions)):
        answer = input(f"\t{questions[item]}{question_end}")
        answer_list = answer_list + "," + answer

    return answer_list


# interface function
def main():
    print()

    my_module = input(f"{counter} Module: \t\t").replace(" ", "")
    print()

    # importing and evaluating the module
    try:
        module_path = (find_module(my_module)).replace("/", ".").replace("['", "").replace("']", "")
        print(f"{counter} Attempting to import: {module_path}")

        if not module_path:
            print("Module not found! Exiting...")
            return

        imported_module = importlib.import_module(module_path)
        print(f"{counter} Module \t\t{module_path} imported successfully!")

    except Exception as e:
        print(f"{counter} Warning: \t\tplease be more specific in your module name!")
        print(f"Error: {e}")
        return

    # find and printing the help
    try:
        introduction = eval(f"imported_module.introduction()")
        print(f"{counter} Introduction: \t{introduction}")
        print()

    except Exception as e:
        print(f"{counter} Explanation: \tnot available!")
        print(f"Error: {e}")
        print()

    # find the questions UNDER DEVELOPMENT
    try:
        questions = eval(f"imported_module.questions()")

    except Exception as e:
        print(f"{counter} Questions: \t\tnot available!")
        print(f"Error: {e}")
        print()

    # import data
    try:
        executable = f"imported_module.perform({collect_answers(questions)})"
        start_time = time.time()
        myresult = str(eval(executable))  # important
        end_time = time.time()
        duration = str(round((end_time - start_time) * 1000, 4))

        # printing all the results
        print()
        print(f"{counter} Result: \t\t{myresult}")
        print()
        print(f"{counter} Duration: \t\t{duration} ms")
        print("_" * line_length)

    except Exception as e:
        print(f"{counter} Error during execution: \t{e}")
        print("_" * line_length)


# starting and looping the interface function, with restarting after an error
for counter in range(1, 1000000):
    try:
        main()

    except Exception as error_message:
        print()
        print(f"{counter} Advice: \t\tan existing module or parameter(s) should be specified, or the module has programming errors.")
        print()
        print("_" * line_length)

# end of file
