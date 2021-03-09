import pandas as pd
import os

# Note:
# This program could be more flexible, like it can detect the min and max of the data to decide the boundary of the RANGE.

class presenter:

    def __init__(self): 
        pass
    
    # Input: file_name <string> the file containing the data.
    # Output: dataOut <list> a list of data.
    def getData(self, file_name):
        # Check the file is exist
        exist = self.check_file_exist(file_name)
        if exist:
            # The dataType is DataFrame.
            data = pd.read_csv("data.csv")

            # The dataType is transformed to List
            data_list = []
            for datum in data["1"]: data_list.append(datum)
            return data_list
        else:
            print(f"{file_name} doesn't exist.")
            exit()
    # Input: data_list <list> It contains data.
    # Output: None
    def printData(self, data_list):
        print(data_list)

    # Input: data_list <list> It contains data.
    # Output: data_freq <dict> It contains statistic info - frequency of data.
    def makeFrequency(self, data_list):
        data_freq = {ele: data_list.count(ele) for ele in data_list}
        return data_freq

    # Input: dataFreq <dict> It contains statistic info - frequency of data.
    # Output: None
    def makeHistogram(self, data_freq, file_name):
        print("The following is the frequency of the data in {file_name}.")
        for i in range(1,21): print(f"{i}: {data_freq[i]*'*'}")

    # Input: file_name <String> It contains data in csv form.
    # Output: result <Boolean> It checks whether the file exist.
    def check_file_exist(self, file_name): return file_name in os.listdir()