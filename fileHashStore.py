import csv
import tempfile
import os

import pandas

class FileHashStore:
    """
        A class for storing the file hashes

        Attributes
        ----------
        csvFilePath : str
            A generated csv file in a temporary location

    """
    def __init__(self):
        tempFolder = tempfile.gettempdir()
        self.csvFilePath = os.path.join(tempFolder, "TestOutput.csv")
        print("temp file = " + self.csvFilePath)
        self.createCsv()
        

    def createCsv(self):
        """
            Create empty csv with the field names
        """
        with open(self.csvFilePath, 'w', newline='') as csvfile:
            fieldnames = ['name', 'path', 'hash']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            csvfile.close()

    def writeToCsv(self, csvData):
        """
            Write to Csv file

            Parameters
            ----------
            csvData : dict
                {'File Name': str, 'File Path' : str, 'MD5 Hash' : str}
        """
        with open(self.csvFilePath, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csvData.keys())
            writer.writerow(csvData)
        csvfile.close()

    def readCsv(self):
        rawData = pandas.read_csv(self.csvFilePath)
        photoList = pandas.DataFrame(rawData).sort_values(by='hash')
        photoList = photoList[photoList.duplicated('hash', keep=False)]
        return photoList


  