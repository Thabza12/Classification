# from pathlib import Path

class text:
    
    def __init__(self, text_file):
        self.file_path = text_file
    

    def read_text_file(self):
    # Read the text file into a list of field names
    with open(self.file_path, 'r') as file:
        field_names = [line.strip() for line in file.readlines()]
    return field_names
