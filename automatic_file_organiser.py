import streamlit as st
import os, shutil, mimetypes

st.title("📁 Automatic File Organizer")
st.write("Upload your files and I’ll arrange them neatly for you!")

uploaded_files = st.file_uploader("Upload multiple files", accept_multiple_files=True)

if uploaded_files:
    base_path = "organized_files"
    os.makedirs(base_path, exist_ok=True)

    for file in uploaded_files:
        # Save uploaded file
        with open(file.name, "wb") as f:
            f.write(file.getbuffer())

        # Detect file type
        file_type, _ = mimetypes.guess_type(file.name)
        folder_name = "Others"

        if file_type:
            if "image" in file_type:
                folder_name = "Images"
            elif "pdf" in file_type:
                folder_name = "PDFs"
            elif "video" in file_type:
                folder_name = "Videos"
            elif "text" in file_type:
                folder_name = "TextFiles"

        # Move to respective folder
        target_folder = os.path.join(base_path, folder_name)
        os.makedirs(target_folder, exist_ok=True)
        shutil.move(file.name, os.path.join(target_folder, file.name))

    st.success("✅ Files Organized Successfully!")
    st.balloons()
