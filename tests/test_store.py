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
        self.assertFalse(can_checkout(0))

    def test_loyalty_starts_at_zero(self):
        self.assertEqual(loyalty_discount(0), 0)
    def test_loyalty_discount_tiers(self):
        self.assertEqual(loyalty_discount(499), 0)
        self.assertEqual(loyalty_discount(500), 5)
        self.assertEqual(loyalty_discount(999), 5)
        self.assertEqual(loyalty_discount(1000), 10)

    def test_free_shipping_over_threshold(self):
        self.assertEqual(shipping_cost(1000), 0.00)
        self.assertEqual(shipping_cost(1500), 0.00)
        self.assertEqual(shipping_cost(1000.01), 0.00)

    def test_apply_discount_percent_invalid(self):
        with self.assertRaises(ValueError):
            apply_discount(1000, 200)
        with self.assertRaises(ValueError):
            apply_discount(1000, -100)


if __name__ == "__main__":
    unittest.main()
