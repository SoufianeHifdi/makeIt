from Generators.PDFGenerator import generate_file as generate_pdf
from Generators.DocxGenerator import generate as generate_docx
from shutil import copy2
import os


def generate(inputs):
    for input_dict in inputs:
        # inputs is a list of dictionnaries.
        # each line added in the UI is an element of the list
        # each element of the list consists of a dict with the input values

        number_of_files = int(input_dict['number_of_files'])
        size_of_files = int(input_dict['size_of_files']);
        path = input_dict['path']
        file_type = input_dict['file_type']

        if file_type == 'pdf':
            base_name = "generated_pdf"
            extension = ".pdf"
            initial_file_path = generate_pdf(size_of_files, path)

        elif file_type == 'docx':
            generate_docx(number_of_files, size_of_files, path)

        else:
            continue  # Skip unsupported file types

        # Copy it number_of_files - 1 times (since one file is already generated)

        for i in range(2, number_of_files + 1):
            new_file_path = os.path.join(path, f"{base_name}_{i}{extension}")
            copy2(initial_file_path, new_file_path)
            print(f"Copied PDF: {new_file_path}")
        print(file_type)