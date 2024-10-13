import os


def return_file_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)
    return file_path


file_name = "../.venv/files/json.json"
print(return_file_path(file_name))
