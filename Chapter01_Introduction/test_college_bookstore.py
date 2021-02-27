import unittest
import college_bookstore as cb

class Test_College_BookStore(unittest.TestCase):
    
    def test_inner_methods(self):
        
        # 1. 建立一個 textbook instance
        book = cb.textbook('AI.FREE_Book')

        # 2. 確認書名沒錯
        self.assertEqual(book.get_book_name(), "AI.FREE_Book")

        # 3. 確認初始數量及價格為零
        self.assertEqual(book.get_current_status(), {"amount":0, "price": 0})

        # 4. 確認紀錄為空
        self.assertEqual(book.get_record(), {"orders":{}, "sales":{}})
    
    def test_determine_price(self):

        # 1. 建立一個 textbook instance
        book = cb.textbook("AI.FREE_Book")

        # 2. 使用 determine_price 方法決定該書價格
        book.determine_price(330)

        # 3. 確認價格的變動符合預期
        self.assertEqual(book.get_current_status()["price"], 330)
        

if __name__ == "__main__":
    unittest.main()