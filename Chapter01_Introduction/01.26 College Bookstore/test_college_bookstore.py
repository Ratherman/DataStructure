import unittest
import College_Bookstore as cb

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

    def test_sell_book(self):
        # 1. 建立一個 book instance
        book = cb.textbook("AI.FREE_Book")

        # 2. 從上游廠商訂 20 本書
        tic_amount = 20
        order_id = 0
        book.order_book(order_id, "Big Seller", tic_amount, 100)

        # 3. 然後拿到 20 本書
        book.receive_book(0)

        # 4. 對這個 book instance 定價，訂330元。
        book.determine_price(330)

        # 5. 販賣書本3本
        sell_amount = 3
        sell_id = 0
        book.sell_book(sell_id, "Small Buyer", sell_amount)

        # 6. 檢查資料庫中是不是真的有少3本
        self.assertEqual(book.get_book_quantity(), tic_amount - sell_amount)
        
        # 7. 檢查資料庫中是不是真的有多了3本的販賣紀錄
        check_sell_amount = book.get_record()["sales"][sell_id]["amount"]
        self.assertEqual(check_sell_amount, sell_amount)

    def test_return_book(self):
        # 1. 建立 book instance
        book = cb.textbook("AI.FREE_Book")

        # 2. 向上游廠商訂書
        order_id = 0
        book.order_book(order_id, "Big Seller", 20, 330)

        # 3. 上游廠商拿書來
        book.receive_book(order_id)

        # 4. 對書定價
        book.determine_price(350)

        # 5. 有人買書
        sell_id = 0
        book.sell_book(sell_id, "Small Buyer", 3)

        # 6. 有人退書(假設退了的書就丟掉不用，而且只能全退 ^_^)
        book.return_book(sell_id)

        # 7. 確認退書之後，資料庫的salse狀態符合預期 Return: From False to True
        check_return_book = book.get_record()["sales"][sell_id]["return_book"]
        self.assertEqual(check_return_book, True)

    def test_get_return_quantity(self):

        # 1. 建立 book instance
        book = cb.textbook("AI.FREE_Book")

        # 2. 向上游廠商訂書
        order_id = 0
        book.order_book(order_id, "Big Seller", 20, 330)

        # 3. 上游廠商拿書來
        book.receive_book(order_id)

        # 4. 對書定價
        book.determine_price(350)

        # 5. 有人買書
        sell_id = 0
        sell_amount = 3
        book.sell_book(sell_id, "Small Buyer", sell_amount)

        # 6. 有人退書(假設退了的書就丟掉不用，而且只能全退 ^_^)
        book.return_book(sell_id)

        # 7. 確認退書一共 3 本
        self.assertEqual(sell_amount, book.get_return_quantity())

if __name__ == "__main__":
    unittest.main()