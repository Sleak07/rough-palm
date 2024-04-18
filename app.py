import streamlit as st
from fold import check_images_exist

# Streamlit UI
def main():
    st.title("Image Checker")

    # File uploader to accept multiple files
    uploaded_files = st.file_uploader("Upload image files", accept_multiple_files=True)

    # Button to trigger image check
    if st.button("Check Images"):
        if uploaded_files:
            # Save uploaded files to a temporary directory
            for uploaded_file in uploaded_files:
                with open(uploaded_file.name, 'wb') as f:
                    f.write(uploaded_file.getvalue())

            # Check if images exist in the uploaded files
            images_exist = check_images_exist('.')
            if images_exist:
                st.success("Images exist.")
            else:
                st.error("No images found.")
        else:
            st.warning("Please upload at least one file.")

if __name__ == "__main__":
    main()
    
