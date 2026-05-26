from machine import Pin
from time import ticks_ms, ticks_diff


class Pedestrian_Button(Pin):
    """Sub class inherits the super "pin" class implements pedestrian__button which gets input, displaying pedestrian status

    This class provides methods to control an LED including on, off, toggle, and non-blocking flashing.
    It extends the machine.Pin class functionality, overriding and adding methods specific to LED control.

    Args:
        pin (int): The GPIO pin number the LED is connected to.
        flashing (bool, optional): Whether to enable flashing capability. Defaults to False.
        debug (bool, optional): Whether to print debug statements. Defaults to False.
    """

    def __init__(self, pin, debug):
        """Initialise the Led_Light object.

        Args:
            pin (int): The GPIO pin number the LED is connected to.
            flashing (bool, optional): Whether to enable flashing capability. Defaults to False.
            debug (bool, optional): Whether to print debug statements. Defaults to False.
        """
        super().__init__(pin, Pin.IN, Pin.PULL_DOWN)
        self.__debug = debug
        self.__pin = pin
        self.__last_pressed = 0  # Track the last time the button was pressed
        self.__pedestrian_waiting = False
        # Set up interrupt on rising edge
        self.irq(trigger=Pin.IRQ_RISING, handler=self._callback)

    def button_state(self, value=None):
        if value is None:
            # Getter
            if self.__debug:
                print(
                    f"Button connected to Pin {self.__pin} is {'WAITING' if self.__pedestrian_waiting else 'NOT WAITING'}"
                )
            return self.__pedestrian_waiting
        else:
            # Setter
            self.__pedestrian_waiting = bool(
                value
            )  # Convert to boolean to ensure proper type
            if self.__debug:
                print(
                    f"Button state on Pin{self.__pin} set to {self.__pedestrian_waiting}"
                )

    def callback(self, pin):
        current_time = ticks_ms()  # Get the current time in milliseconds
        if ticks_diff(current_time, self.__last_pressed) > 200:  # 200ms debounce delay
            self.__last_pressed = current_time
            self.__pedestrian_waiting = True
            if self.__debug:
                print(f"Button pressed on Pin {self.__pin} at {current_time}ms")
