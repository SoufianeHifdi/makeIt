import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog


class FileGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.input_rows = []  # List to hold all rows of inputs
        self.selected_path = tk.StringVar()  # Variable to hold the selected path

        self.file_types = ['msg', 'csv', 'xml', 'html', 'png', 'pptx', 'xltx', 'eml',
                           'jpeg', 'jpg', 'xlsx', 'xls', 'docx', 'pdf']  # List of file types
        self.setup_ui()


    def setup_ui(self):
        # Setting the window title and larger initial size
        self.root.title("File Generator App")
        self.root.geometry("1200x600")  # Increased window size for better visibility

        # Scrollable Frame to hold input fields
        self.canvas = tk.Canvas(self.root)
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Path selection
        path_frame = ttk.Frame(self.root)
        path_frame.pack(fill='x', padx=10, pady=5)
        ttk.Label(path_frame, text="Path:").pack(side="left", padx=5, pady=5)
        self.path_entry = ttk.Entry(path_frame, textvariable=self.selected_path, state='readonly')
        self.path_entry.pack(side="left", padx=5, pady=5, fill="x", expand=True)
        self.select_path_btn = ttk.Button(path_frame, text="Select Path", command=self.select_path)
        self.select_path_btn.pack(side="left", padx=10)

        # "+" Button on a new line by itself to add another set of inputs
        self.add_line_btn_frame = ttk.Frame(self.scrollable_frame)
        self.add_line_btn = ttk.Button(self.add_line_btn_frame, text="+", command=self.add_input_line)

        self.add_input_line()  # Initialize the first row of inputs
        self.add_line_btn_frame.pack(fill='x', expand=True, padx=10)
        self.add_line_btn.pack(side="left", pady=10)

        # "Generate" Button to create the files
        self.generate_btn = ttk.Button(self.root, text="Generate", command=self.generate_files)
        self.generate_btn.pack(pady=20)

    def add_input_line(self):
        # Function to add another line of input fields for additional file specifications
        row_frame = ttk.Frame(self.scrollable_frame)
        row_frame.pack(pady=5, padx=10, fill='x', expand=True)

        labels = ["Number of Files", "Size of Files (MB)"]
        entries = []  # to hold entry widgets for this row

        for i, label in enumerate(labels):
            ttk.Label(row_frame, text=label).pack(side="left", padx=5, pady=5)
            entry = ttk.Entry(row_frame)
            entry.pack(side="left", padx=5, pady=5, fill="x", expand=True)
            entries.append(entry)


        # File Type as a Dropdown Menu
        file_type_var = tk.StringVar()
        ttk.Label(row_frame, text="Type of File").pack(side="left", padx=5, pady=5)
        file_type_dropdown = ttk.Combobox(row_frame, textvariable=file_type_var, values=self.file_types, state="readonly")
        file_type_dropdown.pack(side="left", padx=5, pady=5, fill="x", expand=True)
        file_type_dropdown.set(self.file_types[0])  # Set default value

        self.input_rows.append(entries)  # Add the entries of this row to the list

        # Check if the "+" button frame is already packed, unpack it
        if self.add_line_btn_frame.winfo_manager():
            self.add_line_btn_frame.pack_forget()

        # Repack the "+" button frame at the end
        self.add_line_btn_frame.pack(fill='x', expand=True, padx=10)

    def generate_files(self):
        # Function to process user input and generate the specified files
        pass  # Placeholder for functionality

    def select_path(self):
        # Function to open a file dialog and update the selected path
        path = filedialog.askdirectory()
        if path:
            self.selected_path.set(path)
def main():
    root = tk.Tk()
    app = FileGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
