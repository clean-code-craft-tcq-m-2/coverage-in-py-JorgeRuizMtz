class Notification:

  def __init__(self,send_to, temp_limit):
    self.send_to = send_to
    self.temp_limit = temp_limit

  def notify_mail(self, user_email):

    user = user_email
    print(f'\n To: {user}')

    if self.temp_limit == 'TOO_LOW':
      print('\n Hello, the temperature is getting too low. \n')
    elif self.temp_limit == 'TOO_HIGH':
      print('\n Hello, the temperature is getting too high. \n')
    else:
      print('\n Hello, temperature is Normal. All is good. \n')

  def notify_controller(self):
    print(f'{self.temp_limit}')

  def notify(self):
    if self.send_to == "TO_CONTROLLER":
      self.notify_controller()
      return True
    elif self.send_to == "TO_EMAIL":
      self.notify_mail("user01@bosch.com")
      return True
    else:
      return False