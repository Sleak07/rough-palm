import streamlit as st
import os
from fold import check_images_exist, convert_images_to_pdf

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
            output_folder = 'pdf_output'
            convert_images_to_pdf(image_files, output_folder)

            # Prompt to delete the output folder
            if st.checkbox("Delete output folder"):
                delete_output_folder(output_folder)

            st.success("Conversion completed successfully.")
        else:
            st.warning("Please upload at least one file.")

# Function to delete the output folder
def delete_output_folder(output_folder):
    try:
        os.rmdir(output_folder)
        st.info("Output folder deleted successfully.")
    except OSError as e:
        st.error(f"Error deleting output folder: {e}")

if __name__ == "__main__":
    main()
