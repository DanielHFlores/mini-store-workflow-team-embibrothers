import unittest

from store import apply_discount, can_checkout, loyalty_discount, shipping_cost


class StoreTests(unittest.TestCase):
    def test_regular_shipping(self):
        self.assertEqual(shipping_cost(500), 99.0)

    def test_negative_subtotal_is_invalid(self):
        with self.assertRaises(ValueError):
            shipping_cost(-1)

    def test_apply_discount(self):
        self.assertEqual(apply_discount(1000, 10), 900.0)

    def test_checkout_with_items(self):
        self.assertTrue(can_checkout(1))

    def test_loyalty_starts_at_zero(self):
        self.assertEqual(loyalty_discount(0), 0)


if __name__ == "__main__":
    unittest.main()
