import pandas
import os

class presenter:

    def __init__(self):
        pass
    
    # Input: 
    #     file_name: the file containing the data.

    # Output: 
    #     dataOut: a list of data.
    def getData(self, file_name):
        exist = self.check_file_exist(file_name)
        print(exist)


    def printData(self):
        pass

    def makeFrequency(self):
        pass


    def makeHistogram(self):
        pass



    # Inner Methods

    # Input:
    #    file_name: the file containing the data.

    # Output:
    #    resutle: true/false

    def check_file_exist(self, file_name):
        return file_name in os.listdir()


        

