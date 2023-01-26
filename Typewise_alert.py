from Notification import Notification

COOLING_TYPE = {
  "PASSIVE_COOLING": (0,35)
, "HI_ACTIVE_COOLING": (0,45)
, "MED_ACTIVE_COOLING": (0,40)
}

class Battery_monitoring:

  def __init__(self, send_alert_to, Cooling, temperature):
    self.send_alert_to = send_alert_to
    self.Cooling = Cooling
    self.temperature = temperature

  def classify_and_derive(self):
    lowerLimit, upperLimit = COOLING_TYPE[self.Cooling]
    if self.temperature < lowerLimit: 
      return 'TOO_LOW'
    elif self.temperature > upperLimit: 
      return 'TOO_HIGH'
    else: 
      return 'NORMAL'

  def classify_and_derive_send_alert(self):
    temp_limit = self.classify_and_derive()
    NotifyBatteryStatus = Notification(self.send_alert_to,temp_limit)
    return NotifyBatteryStatus.notify()