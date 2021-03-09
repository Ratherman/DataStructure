import unittest
import Frequency_Histogram as FH

class Test_Frequency_Histogram(unittest.TestCase):

    def test_getData(self):
        # 1. 需要一個 presenter 來幫我們 call function
        presenter = FH.presenter()

        # 2. 讀檔案
        data = presenter.getData("data.csv")

        # 3. 確認讀出來的檔案型別是 <list>
        self.assertEqual(type(data), type([1,2,3]))

    def test_makeFrequency(self):
        # 1. 需要一個 presenter 來幫我們 call function
        presenter = FH.presenter()

        # 2. 讀檔案
        data = presenter.getData("data.csv")

        # 3. 製作 Frequency of data
        data_freq = presenter.makeFrequency(data)

        # 4. 確認 data_freq 的型別是 dict
        self.assertEqual(type(data_freq), type({"key":"value"}))

    def test_check_file_exist(self):
        # 1. 需要一個 presenter 來幫我們 call function
        presenter = FH.presenter()

        # 2. 確認是不是能真的檢查路徑中真的有該檔案
        self.assertEqual(presenter.check_file_exist("data.csv"), True)
        self.assertEqual(presenter.check_file_exist("datum.csv"), False)

if __name__ == "__main__":
    unittest.main()