from Typewise_alert import Battery_monitoring

if __name__ == '__main__':
  BatteryTest1 = Battery_monitoring("TO_CONTROLLER","HI_ACTIVE_COOLING",32)
  BatteryTest1.classify_and_derive_send_alert()
  BatteryTest2 = Battery_monitoring("TO_EMAIL","HI_ACTIVE_COOLING",32)
  BatteryTest2.classify_and_derive_send_alert()
  BatteryTest3 = Battery_monitoring("TO_CONTROLLER","HI_ACTIVE_COOLING",60)
  BatteryTest3.classify_and_derive_send_alert()
  BatteryTest3 = Battery_monitoring("TO_EMAIL","HI_ACTIVE_COOLING",60)
  BatteryTest3.classify_and_derive_send_alert()
  BatteryTest4 = Battery_monitoring("TO_CONTROLLER","HI_ACTIVE_COOLING",-10)
  BatteryTest4.classify_and_derive_send_alert()
  BatteryTest5 = Battery_monitoring("TO_EMAIL","HI_ACTIVE_COOLING",-10)
  BatteryTest5.classify_and_derive_send_alert()