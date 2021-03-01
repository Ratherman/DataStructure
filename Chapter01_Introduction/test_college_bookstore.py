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
    
    def test_order_book(self):
        # 1. 建立一個 textbook instance
        book = cb.textbook("AI.FREE_Book") # 這個動作表示我確定上游廠商有這本書。

        # 2. 確認以下資訊: 上游廠商是誰、要買幾本、買一本書花了多少錢、下訂的時間點、抵達的時間點、是否抵達
        order = {
            "seller": "Test Upstream Seller",
            "amount": 10,
            "price": 330,
            "order_date": (2020,11,18),
            "arrive_date": (2000,10,20),
            "arrive": False,
        }

        # 3. 圖書系統將給定一個 id 儲存這筆 order
        id = 0
        book.record["orders"][id] = order

        # 4. 檢查 Database 裡面是不是有發生符合我們預期的事情
        # 4.1 檢查 seller 是不是 Test Upstream Seller
        self.assertEqual(book.record["orders"][id]["seller"], "Test Upstream Seller")

        # 4.2 檢查數量是否為 10
        self.assertEqual(book.record["orders"][id]["amount"], 10)

        # 4.3 檢查價格是否為 330
        self.assertEqual(book.record["orders"][id]["price"], 330)

        # 4.4 檢查訂購日期是否為 (2020,11,18)
        self.assertEqual(book.record["orders"][id]["order_date"], (2020,11,18))

        # 4.5 檢查是否為 尚未抵達
        self.assertEqual(book.record["orders"][id]["arrive"], False)

    def test_determine_price(self):

        # 1. 建立一個 textbook instance
        book = cb.textbook("AI.FREE_Book")

        # 2. 使用 determine_price 方法決定該書價格
        book.determine_price(330)

        # 3. 確認價格的變動符合預期
        self.assertEqual(book.get_current_status()["price"], 330)
        

if __name__ == "__main__":
    unittest.main()