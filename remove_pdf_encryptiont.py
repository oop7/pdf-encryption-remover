import tkinter as tk
from tkinter import filedialog, messagebox
import fitz  # PyMuPDF

def remove_pdf_encryption(input_pdf, output_pdf):
    try:
        # Open the encrypted PDF
        pdf_document = fitz.open(input_pdf)
        
        # Create a new PDF to write the decrypted content
        output_document = fitz.open()

        # Iterate over all pages and add them to the new document
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            output_document.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)

        # Save the new PDF
        output_document.save(output_pdf)
        output_document.close()

        return True
    except Exception as e:
        print(e)
        return False

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        entry_input.delete(0, tk.END)
        entry_input.insert(0, file_path)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if file_path:
        entry_output.delete(0, tk.END)
        entry_output.insert(0, file_path)

def process_pdf():
    input_path = entry_input.get()
    output_path = entry_output.get()
    
    if not input_path or not output_path:
        messagebox.showwarning("Input Error", "Please specify both input and output file paths.")
        return
    
    success = remove_pdf_encryption(input_path, output_path)
    if success:
        messagebox.showinfo("Success", f"PDF saved as '{output_path}' without encryption.")
    else:
        messagebox.showerror("Error", "Failed to remove PDF encryption.")

# Set up the GUI
root = tk.Tk()
root.title("PDF Encryption Remover")

# Input file
tk.Label(root, text="Input PDF:").grid(row=0, column=0, padx=10, pady=10)
entry_input = tk.Entry(root, width=50)
entry_input.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse...", command=open_file).grid(row=0, column=2, padx=10, pady=10)

# Output file
tk.Label(root, text="Output PDF:").grid(row=1, column=0, padx=10, pady=10)
entry_output = tk.Entry(root, width=50)
entry_output.grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse...", command=save_file).grid(row=1, column=2, padx=10, pady=10)

# Process button
tk.Button(root, text="Remove Encryption", command=process_pdf).grid(row=2, column=0, columnspan=3, padx=10, pady=20)

root.mainloop()
