import os

UPLOAD_FOLDER = './uploads/'


def save_file(file):
    """Save the file to the upload directory."""
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    return file_path


def delete_file(filename):
    """Delete the file from the upload directory."""
    file_path = os.path.join(filename)
    if os.path.exists(file_path):
        os.remove(file_path)
