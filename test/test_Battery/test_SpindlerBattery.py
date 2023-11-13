import unittest
from car_module.components.battery import SpliderBattery
from datetime import date

class TestSplinderBattery (unittest.TestCase):
    def test_check_needs_service_true_case(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year - 3)
        nubbin = SpliderBattery(current_date,last_service_date)
        self.assertTrue(nubbin.needs_service())

    def test_check_needs_service_false_case(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year-1)
        nubbin = SpliderBattery(current_date,last_service_date)
        self.assertFalse(nubbin.needs_service())