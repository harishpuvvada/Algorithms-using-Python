''' This question from AKuna Capital'''


# a simple orderbook class    
import operator
class OrderBook:
    def __init__(self):
        self.order_book = {}

    def buy(self, order_id, price):
        self.order_book[order_id] = price
        
    def sell(self, order_id):
        if order_id in self.order_book:
            del self.order_book[order_id]

    def get_high_price(self):
        if not self.order_book:
            return -1
        sorted_prices = sorted(self.order_book.items(),key=operator.itemgetter(1))
        ret_val = "%g" % float(sorted_prices[-1][1])  #This line is to drop trailing ".0" from floats
        return ret_val


book = OrderBook()
for line in sys.stdin:
    elements = line.split(' ')
    time_order = int(elements[0])
    type_order = elements[1]
    id_order = int(elements[2])
    price_order = None
    if len(elements) == 4:
        price_order = float(elements[3])
        
    if type_order == 'B':
        book.buy(id_order,price_order)
        
    elif type_order == 'S':
        book.sell(id_order)
        
    print(time_order, book.get_high_price())




#Sample Input
# 0 B 1 10.0
# 10 B 2 20.5
# 30 B 3 15.0
# 60 S 2
# 100 S 1
# 200 S 3
# 250 B 4 10.5
# 300 S 4