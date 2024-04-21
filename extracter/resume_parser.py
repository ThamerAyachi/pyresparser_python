from pyresparser import ResumeParser


def parser_resume(file_path: str):
    data = ResumeParser(file_path).get_extracted_data()
    return data
