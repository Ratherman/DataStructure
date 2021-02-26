import unittest
import college_bookstore as cb

class Test_College_BookStore(unittest.TestCase):
    def test_init(self):
        
        # 1. 建立一個 textbook instance
        book = cb.textbook('AI.FREE_Book')

        # 2. 確認書名沒錯
        self.assertEqual(book.book_name[0], "AI.FREE_Book")

if __name__ == "__main__":
    unittest.main()