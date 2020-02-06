import unittest

from models import Car

class CarTest(unittest.TestCase):
    def test_distance_driven_is_number(self):
        test_car = Car("red", 120, "auto", "85", 100)
        res = test_car.get_distance_driven()

        # Test that the result is a number
        self.assertIsInstance(res, int, "Result should be a number")

        # Test that the result is the correct number (8500)
        self.assertEqual(res, 8500, "Result should be 8500 (85 x 100)")

    def test_serialization_returns_correct_string(self):
        target_json = '{"average_speed": 85, "color": "red", "gear_box": "auto", "hours_driven": 100, "top_speed": 120}'

        test_car = Car("red", 120, "auto", "85", "100")
        res = test_car.get_json()

        self.assertEqual(res, target_json, "Target json should look like this: {}".format(target_json))

if __name__ == "__main__":
    unittest.main()
