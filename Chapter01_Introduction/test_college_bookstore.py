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
        book.order_book(id,order["seller"],order["amount"],order["price"])

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

    def test_receive_book(self):
        
        # 1. 要先 order 才能 receive
        book = cb.textbook("AI.FREE_Book") # 這個動作表示我確定上游廠商有這本書。

        order = {
            "seller": "Test Upstream Seller",
            "amount": 10,
            "price": 330,
            "order_date": (2020,11,18),
            "arrive_date": (2000,10,20),
            "arrive": False,
        }

        id = 0
        book.order_book(id, order["seller"], order["amount"], order["price"])

        # 2. 確認 Receive 之前的狀態，然後再 Receive
        pre_amount = book.get_book_quantity()
        pre_arrive = book.record["orders"][id]["arrive"]
        self.assertEqual(pre_amount, 0)
        self.assertEqual(pre_arrive, False)
        book.receive_book(0)

        # 3.1 檢查 amount 是不是有增加 10
        self.assertEqual(pre_amount+order["amount"], book.get_book_quantity())

        # 3.2 檢查 arrive 是不是有變成 True
        self.assertEqual(book.record["orders"][id]["arrive"], True)

    def test_determine_price(self):

        # 1. 建立一個 textbook instance
        book = cb.textbook("AI.FREE_Book")

        # 2. 使用 determine_price 方法決定該書價格
        book.determine_price(330)

        # 3. 確認價格的變動符合預期
        self.assertEqual(book.get_current_status()["price"], 330)
        

    def test_get_book_quantity(self):
                
                
        # 1. 建立一個 textbook instance
        book = cb.textbook("AI.FREE_Book")

        # 2. order 20 本書
        amount = 20
        id = 0
        book.order_book(id, "AI.FREE Team", amount, 100)

        # 3. receive 20 本書
        book.receive_book(0)

        # 4. 確認資料庫中確實有 20 本書
        self.assertEqual(book.get_book_quantity(), amount)

if __name__ == "__main__":
    unittest.main()