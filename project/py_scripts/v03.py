from machine import Pin
from time import sleep

Class Led_Light(Pin):
def __init__(self, pin, flashing=False, debug=False):
    super().__init__(pin, Pin.OUT)
    self.led_light_state


@property
def led_light_state(self):
    # Getter method
    return self.value()


@led_light_state.setter
def led_light_state(self, value):
    # Setter method
    if value == 1:
        self.off()
    elif value == 0:
        self.on()


red_light = Led_Light(3, False, False)

while True:
    print(red_light.led_light_state)
    red_light.led_light_state = 1
    sleep(0.25)
    print(red_light.led_light_state)
    red_light.led_light_state = 0
    sleep(0.25)
