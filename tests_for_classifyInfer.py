import unittest
from Typewise_alert import Battery_monitoring

class Battery_Monitoring_Test(unittest.TestCase):
  def test_classify_derive(self):
    BatteryTest1 = Battery_monitoring("TO_CONTROLLER","HI_ACTIVE_COOLING",25)
    self.assertTrue(BatteryTest1.classify_and_derive()=="NORMAL")

    BatteryTest2 = Battery_monitoring("TO_EMAIL","HI_ACTIVE_COOLING",60)
    self.assertTrue(BatteryTest2.classify_and_derive()=="TOO_HIGH")

    BatteryTest3 = Battery_monitoring("TO_EMAIL","HI_ACTIVE_COOLING",-10)
    self.assertTrue(BatteryTest3.classify_and_derive()=="TOO_LOW")

    BatteryTest4 = Battery_monitoring("TO_CONTROLLER","PASSIVE_COOLING",25)
    self.assertTrue(BatteryTest4.classify_and_derive()=="NORMAL")

    BatteryTest5 = Battery_monitoring("TO_EMAIL","PASSIVE_COOLING",60)
    self.assertTrue(BatteryTest5.classify_and_derive()=="TOO_HIGH")

    BatteryTest6 = Battery_monitoring("TO_EMAIL","PASSIVE_COOLING",-10)
    self.assertTrue(BatteryTest6.classify_and_derive()=="TOO_LOW")

    BatteryTest7 = Battery_monitoring("TO_CONTROLLER","MED_ACTIVE_COOLING",25)
    self.assertTrue(BatteryTest7.classify_and_derive()=="NORMAL")

    BatteryTest8 = Battery_monitoring("TO_EMAIL","MED_ACTIVE_COOLING",60)
    self.assertTrue(BatteryTest8.classify_and_derive()=="TOO_HIGH")
    
    BatteryTest9 = Battery_monitoring("TO_EMAIL","MED_ACTIVE_COOLING",-10)
    self.assertTrue(BatteryTest9.classify_and_derive()=="TOO_LOW")

if __name__ == '__main__':
  unittest.main()