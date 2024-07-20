'''
create a python code with the following instructions:
1. create a python function named initialize with one argument, name (string type).
2. create 3 variables as the following
    a. crew_name = name.replace("_", " ").replace("-", " ").title().replace(" ", "")
    b. folder_name = name.replace(" ", "_").replace("-", "_").lower()


3. Go through all files in current folder and replace
the {{crew_name}} variable to value in the "crew_name" variable
4. Go through all files in current folder and replace {{name}} to value in the "name" argument.
5. rename the current folder to value in the "folder_name" variable


6. run an input prompt to ask user about the CrewAI project name and save it in a variable.
7. pass the name to the initialize function and run the function. 
'''

import os

def initialize(name):
    try:
        # Step 2: Create variables
        crew_name = name.replace("_", " ").replace("-", " ").title().replace(" ", "")
        folder_name = name.replace(" ", "_").replace("-", "_").lower()

        # Steps 3 & 4: Replace {{crew_name}} and {{name}} and {{folder_name}} in all files
        for root, dirs, files in os.walk("."):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r') as f:
                        file_data = f.read()
                    new_data = file_data.replace("{{crew_name}}", crew_name).replace("{{name}}", name).replace("{{folder_name}}", folder_name)
                    with open(file_path, 'w') as f:
                        f.write(new_data)
                    print(f"Updated file: {file_path}")
                except Exception as e:
                    print(f"Failed to update file: {file_path} due to {e}")

        # Step 5: Rename the current folder
        try:
            current_folder = os.path.basename(os.getcwd())
            parent_folder = os.path.dirname(os.getcwd())
            new_folder_path = os.path.join(parent_folder, folder_name)
            os.rename(os.getcwd(), new_folder_path)
            print(f"Folder renamed to {folder_name}")
        except Exception as e:
            print(f"Failed to rename folder due to {e}")

    except Exception as e:
        print(f"Initialization failed due to {e}")

if __name__ == "__main__":
    try:
        # Step 6: Prompt user for CrewAI project name, description, Author and Email
        project_name = input("Enter the CrewAI project name: ")

        # Step 7: Pass the name to the initialize function and run it
        initialize(project_name)
        print("Initialization completed successfully.")
    except Exception as e:
        print(f"Failed to complete initialization due to {e}")
