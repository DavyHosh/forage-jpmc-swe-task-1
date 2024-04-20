import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
  def test_getRatio_nonzero_prices(self):
      # Test case with non-zero prices for both price_a and price_b
      price_a = 10
      price_b = 5
      expected_ratio = 2
      self.assertEqual(getRatio(price_a, price_b), expected_ratio)

  def test_getRatio_price_b_zero(self):
    # Test case with price_b being 0
    price_a = 10
    price_b = 0
    self.assertIsNone(getRatio(price_a, price_b))

  def test_getRatio_both_prices_zero(self):
    # Test case with both price_a and price_b being 0
    price_a = 0
    price_b = 0
    self.assertEqual(getRatio(price_a, price_b), 0)

  def test_getRatio_price_a_zero(self):
    # Test case with price_a being 0
    price_a = 0
    price_b = 5
    self.assertEqual(getRatio(price_a, price_b), 0)
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """


  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()
