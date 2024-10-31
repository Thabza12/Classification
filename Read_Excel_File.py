import pandas as pd

class excel:
    
    def __init__(self, excel_file):
        self.file_path = excel_file
    

    def read_excel_file(self):
        # Load the Excel file
        df = pd.read_excel(self.file_path)
        return df
