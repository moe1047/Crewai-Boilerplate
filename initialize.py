import os

def initialize(name):
    # Step 2: Create variables
    crew_name = name.replace("_", " ").replace("-", " ").title().replace(" ", "")
    folder_name = name.replace(" ", "_").replace("-", "_").lower()

    # Step 3: Replace placeholders in specified files
    files_to_update = [
        "pyproject.toml",
        f"src/Crewai-Boilerplate/crew.py",
        f"src/Crewai-Boilerplate/main.py"
    ]

    for file_path in files_to_update:
        with open(file_path, 'r') as file:
            content = file.read()

        content = content.replace("{{crew_name}}", crew_name)
        content = content.replace("{{folder_name}}", folder_name)
        content = content.replace("{{name}}", name)

        with open(file_path, 'w') as file:
            file.write(content)

    # Step 4: Rename the current folder
    current_folder = os.path.basename(os.getcwd())
    parent_dir = os.path.dirname(os.getcwd())
    new_folder_path = os.path.join(parent_dir, folder_name)
    os.rename(os.getcwd(), new_folder_path)

    # Step 5: Rename the folder inside the src folder
    src_folder = os.path.join(new_folder_path, "src", "Crewai-Boilerplate")
    new_src_folder = os.path.join(new_folder_path, "src", folder_name)
    os.rename(src_folder, new_src_folder)

if __name__ == '__main__':
    # Step 6: Run an input prompt to ask user about the CrewAI project name
    project_name = input("Enter the CrewAI project name: ")

    # Step 7: Pass the name to the initialize function and run the function
    initialize(project_name)