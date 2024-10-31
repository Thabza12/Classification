# from pathlib import Path

class write:
    
    def __init__(self, file_path, results):
        self.file_path = file_path
        self.results = results
    

    def write_results_to_text_file(self.file_path, self.results):
    # Write the results to a new text file
    with open(self.file_path, 'w') as file:
        for result in self.results:
            file.write(f"{result['ElementName']}\t{result['ElementFieldName']}\t{result['Classification']}\n")