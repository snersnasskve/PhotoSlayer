import csv
import tempfile
import os

class FileHashStore:
    def __init__(self):
        tempFolder = tempfile.gettempdir()
        self.csvFilePath = os.path.join(tempFolder, "TestOutput.csv")
        print("temp file = " + self.csvFilePath)
        self.createCsv()
        

    def createCsv(self):
        with open(self.csvFilePath, 'w', newline='') as csvfile:
            fieldnames = ['name', 'path', 'hash']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            csvfile.close()

    def write_to_csv(self, csv_data):
        with open(self.csvFilePath, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_data.keys())
            writer.writerow(csv_data)
        csvfile.close()

  