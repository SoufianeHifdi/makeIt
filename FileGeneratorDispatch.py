from Generators.PDFGenerator import generate_file as generate_pdf
from Generators.DocxGenerator import generate_file as generate_docx
from shutil import copy2
import os


def generate(inputs):
    for input_dict in inputs:
        # inputs is a list of dictionnaries.
        # each line added in the UI is an element of the list
        # each element of the list consists of a dict with the input values

        number_of_files = int(input_dict['number_of_files'])
        size_of_files = int(input_dict['size_of_files'])
        path = input_dict['path']
        file_type = input_dict['file_type']
        base_name = f"{file_type}_{size_of_files}KB"
        extension = f".{file_type}"

        # Ensure directory exists
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)

        if file_type == 'pdf':
            initial_file_path = generate_pdf(size_of_files, path)

        elif file_type == 'docx':
            initial_file_path = generate_docx(size_of_files, path)

        else:
            continue  # Skip unsupported file types

        # Copy it number_of_files - 1 times (since one file is already generated)
        multiple_copy(number_of_files, base_name, extension, initial_file_path, path)


def multiple_copy(number_of_files, base_name, extension, initial_file_path, path):
    for i in range(2, number_of_files + 1):
        new_file_path = os.path.join(path, f"{base_name}_{i}{extension}")
        copy2(initial_file_path, new_file_path)
        print(f"Copied {extension} file:    {new_file_path}")
