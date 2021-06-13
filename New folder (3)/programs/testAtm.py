import sys
from atmmainpro import atm as AtmProcess
print("***********************************************************")
print("              BANK OF BARODA                                ")
print("              REGISTRATION                    ")
print()

class Atm:

    class InvalidPinException(Exception):
        pass

    def __init__(self):
        self.name = input("Enter name: ")
        self.pin = input("Enter pin: ")
        self.max_retry_count = 3

    def update_pin(self, old_pin):
        try:
            new_pin = int(input("Enter new pin: \n"))
            if old_pin != new_pin:
                raise self.InvalidPinException("Pin not matched")
            self.pin = new_pin
            atm_process = AtmProcess()
            atm_process.amtp()
            atm_process.withdraw()
        except self.InvalidPinException:
            self.max_retry_count -= 1
            if self.max_retry_count == 0:
                print("maximum pin attempt reached... Existing the process")
                sys.exit(1)
            self.update_pin(old_pin)

atm = Atm()
atm.update_pin(atm.pin)

