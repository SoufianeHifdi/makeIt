from reportlab.pdfgen import canvas
import os

repetitions_for_1kb = 1024 * 17.5

repetition_for_1kb = 4800


def generate_file(size_of_files_kb, path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)  # Ensure directory exists

    # Constants for PDF creation
    text_block = "This is sample text. " * 4  # Adjust text block size for better file size approximation
    lines_per_page = 50  # Approximate number of lines per page
    bytes_per_line = len(text_block) * 2  # Rough approximation of bytes per line (assuming 2 bytes per character)

    file_path = os.path.join(path, f"pdf_{size_of_files_kb}KB_{1}.pdf")
    c = canvas.Canvas(file_path)
    text = c.beginText(40, 800)  # Start position for the text
    text.setFont("Helvetica", 10)  # Set font and size

    # Calculate the total bytes needed and convert to lines
    total_bytes_needed = size_of_files_kb * repetitions_for_1kb  # Convert MB to bytes
    total_lines_needed = total_bytes_needed // bytes_per_line
    lines_per_file = total_lines_needed // 1

    # Add text to the PDF to approximate desired file size
    for _ in range(int(lines_per_file)):
        text.textLine(text_block)
        if text.getY() < 40:  # Check if we are at the bottom of the page
            c.drawText(text)
            c.showPage()  # Add a new page
            text = c.beginText(40, 800)  # Reset text position for the new page
    c.drawText(text)
    c.save()
    print(f"Generated PDF: {file_path}")
    return file_path

# generate(1, 1, "C:\\Users\\Ahmed\\Desktop")
