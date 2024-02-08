from docx import Document
import os

repetitions_for_1kb = 1024 * 17.5


def generate_file(size_of_files_kb, path):
    # Initialize a new Document
    doc = Document()
    file_path = os.path.join(path, f"docx_{size_of_files_kb}KB_1.docx")

    # Constants for DOCX creation
    text_block = "This is sample text. " * 4
    bytes_per_block = len(text_block.encode('utf-8'))

    # Calculate the total bytes needed
    total_bytes_needed = size_of_files_kb * 1024 * 240  # Convert KB to bytes
    blocks_needed = total_bytes_needed // bytes_per_block

    # Construct a larger text chunk to add to the document
    large_text_chunk = text_block * int(blocks_needed)
    doc.add_paragraph(large_text_chunk)

    # Save the document
    doc.save(file_path)
    print(f"Generated DOCX: {file_path}")
    return file_path
