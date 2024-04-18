import streamlit as st
import os
from fold import check_images_exist, convert_images_to_pdf, compress_pdf

# Streamlit UI
def main():
    st.title("Image to PDF Converter")

    # File uploader to accept multiple files
    uploaded_files = st.file_uploader("Upload image files", accept_multiple_files=True)

    # Button to trigger image conversion
    if st.button("Convert to PDF"):
        if uploaded_files:
            # Save uploaded files to a temporary directory
            temp_folder = 'temp_images'
            os.makedirs(temp_folder, exist_ok=True)
            image_files = []
            for uploaded_file in uploaded_files:
                with open(os.path.join(temp_folder, uploaded_file.name), 'wb') as f:
                    f.write(uploaded_file.getvalue())
                image_files.append(os.path.join(temp_folder, uploaded_file.name))

            # Convert images to PDF
            output_pdf = 'output.pdf'
            convert_images_to_pdf(image_files, output_pdf)

            # Check PDF size and compress if necessary
            pdf_size = os.path.getsize(output_pdf)
            if pdf_size > 250 * 1024:  # 250 KB threshold
                compressed_output_pdf = 'compressed_output.pdf'
                compress_pdf(output_pdf, compressed_output_pdf)
                st.success(f"PDF converted and compressed successfully. Download compressed PDF: [compressed_output.pdf](./{compressed_output_pdf})")
            else:
                st.success(f"PDF converted successfully. Download PDF: [output.pdf](./{output_pdf})")
        else:
            st.warning("Please upload at least one file.")

if __name__ == "__main__":
    main()
