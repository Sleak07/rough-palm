import os
import img2pdf
from PyPDF2 import PdfReader, PdfWriter

def check_images_exist(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print("Folder not found.")
        return False
    
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    # Check if there are any files with common image extensions
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    images_exist = any(file.lower().endswith(tuple(image_extensions)) for file in files)
    
    return images_exist

def convert_images_to_pdf(image_files, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for image_file in image_files:
        with open(image_file, 'rb') as f:
            pdf_bytes = img2pdf.convert(f)
            if pdf_bytes is not None:
                output_pdf = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(image_file))[0]}.pdf")
                with open(output_pdf, "wb") as pdf_file:
                    pdf_file.write(pdf_bytes)

def compress_pdf(input_pdf, output_pdf):
    with open(input_pdf, 'rb') as input_file:
        pdf_reader = PdfReader(input_file)
        pdf_writer = PdfWriter()

        # Add all pages to the writer object
        for page_num in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_num))

        # Create a new PDF with compressed content
        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)
