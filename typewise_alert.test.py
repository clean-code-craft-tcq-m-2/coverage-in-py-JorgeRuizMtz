import unittest
from Typewise_alert import Battery_monitoring

class Battery_Monitoring_Test(unittest.TestCase):
  def test_classify_Monitorin_battery(self):
    BatteryTest10 = Battery_monitoring("TO_CONTROLLER","HI_ACTIVE_COOLING",25)
    self.assertTrue(BatteryTest10.classify_and_derive_send_alert())

    BatteryTest11 = Battery_monitoring("TO_EMAIL","HI_ACTIVE_COOLING",60)
    self.assertTrue(BatteryTest11.classify_and_derive_send_alert())

    BatteryTest12 = Battery_monitoring("TO_CONTROLLER","HI_ACTIVE_COOLING",-10)
    self.assertTrue(BatteryTest12.classify_and_derive_send_alert())

    BatteryTest13 = Battery_monitoring("TO_EMAIL","PASSIVE_COOLING",25)
    self.assertTrue(BatteryTest13.classify_and_derive_send_alert())

    BatteryTest14 = Battery_monitoring("TO_CONTROLLER","PASSIVE_COOLING",60)
    self.assertTrue(BatteryTest14.classify_and_derive_send_alert())

    BatteryTest15 = Battery_monitoring("TO_EMAIL","PASSIVE_COOLING",-10)
    self.assertTrue(BatteryTest15.classify_and_derive_send_alert())

    BatteryTest16 = Battery_monitoring("TO_CONTROLLER","MED_ACTIVE_COOLING",25)
    self.assertTrue(BatteryTest16.classify_and_derive_send_alert())

    BatteryTest17 = Battery_monitoring("TO_CONTROLLER","MED_ACTIVE_COOLING",60)
    self.assertTrue(BatteryTest17.classify_and_derive_send_alert())
    
    BatteryTest18 = Battery_monitoring("TO_EMAIL","MED_ACTIVE_COOLING",-10)
    self.assertTrue(BatteryTest18.classify_and_derive_send_alert())

if __name__ == '__main__':
  unittest.main()
