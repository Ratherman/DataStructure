class textbook:
  def __init__(self, book_name): # ok
    self.book_name = book_name,
    self.current_status = {"amount":0, "price":0}
    self.record = {"orders":{}, "sales":{}}

  # Inner Method
  def get_book_name(self): # ok
    return self.book_name[0] # It's type is tuple if there's no specify index.
  
  def get_current_status(self): # ok
    return self.current_status
  
  def get_record(self): #ok
    return self.record
  
  # Outer API
  def order_book(self, id, seller, amount, price):
    order = {"seller": seller, "amount": amount, "price": price, "order_date": (2020,11,18), "arrive_date": (1997,11,18),"arrive": False}
    self.record["orders"][id] = order
    return self.record

  def receive_book(self, id):
    self.record["orders"][id]["arrive"] = True
    amount = self.record["orders"][id]["amount"]
    self.current_status["amount"] = self.current_status["amount"] + amount
    return self.record

  def determine_price(self, price): #ok
    self.current_status["price"] = price
    return self.current_status
  
  def get_book_quantity(self):
    return self.current_status["amount"]

  def sell_book(self, id, buyer, amount):
    price = self.current_status["price"]
    sale = {"buyer": buyer, "amount": amount, "price": price, "sell_date": "2020/11/18", "return_date": "1997/11/18", "return_book": False}
    self.current_status["amount"] = self.current_status["amount"] - amount
    self.record["sales"][id] = sale
    return self.record

  def return_book(self, id):
    self.record["sales"][id]["return_book"] = True
    return self.record

  def get_return_quantity(self):
    total = 0
    for sale in self.record["sales"].values():
      if sale["return_book"] == True:
        total = total + sale["amount"]
    return total