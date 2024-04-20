import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock = quote['stock']
      top_bid = quote['top_bid']['price']
      top_ask = quote['top_ask']['price']
      price = (quote['top_bid']['price'] + quote['top_ask']['price'])/2
      self.assertEqual(getDataPoint(quote), (stock, top_bid, top_ask, price))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 115.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock = quote['stock']
      top_bid = quote['top_bid']['price']
      top_ask = quote['top_ask']['price']
      price = (quote['top_bid']['price'] + quote['top_ask']['price'])/2
      self.assertEqual(getDataPoint(quote), (stock, top_bid, top_ask, price))

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_CalculateRatio(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 123.4, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 118.9, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    prices = {}
    for quote in quotes:
      stock = quote['stock']
      price = (quote['top_bid']['price'] + quote['top_ask']['price'])/2
      prices[stock] = price
    self.assertEqual(getRatio(prices['ABC'], prices['DEF']), (prices['ABC']/ prices['DEF']))    

  def test_getRatio_PriceA_Zero(self):
    quotes = [
      {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 123.4, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 118.9, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    prices = {}
    for quote in quotes:
      stock = quote['stock']
      price = (quote['top_bid']['price'] + quote['top_ask']['price'])/2
      prices[stock] = price
    self.assertEqual(getRatio(prices['ABC'], prices['DEF']), (prices['ABC']/ prices['DEF']))

  def test_getRatio_PriceB_Zero(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    prices = {}
    for quote in quotes:
      stock = quote['stock']
      price = (quote['top_bid']['price'] + quote['top_ask']['price'])/2
      prices[stock] = price
    if prices['DEF'] == 0:
      self.assertIsNone(getRatio(prices['ABC'], prices['DEF']))
    else:
      self.assertEqual(getRatio(prices['ABC'], prices['DEF']), (prices['ABC']/ prices['DEF']))
    
if __name__ == '__main__':
    unittest.main()
