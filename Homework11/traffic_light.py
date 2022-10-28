import time

RED_COLOR = 'red'
YELLOW_COLOR = 'yellow'
GREEN_COLOR = 'green'

RED_SWITCH_TIME_SEC = 7
YELLOW_SWITCH_TIME_SEC = 2
GREEN_SWITCH_TIME_SEC = 5


class TrafficLight:
    __color = RED_COLOR

    def __init__(self):
        self.__color = RED_COLOR

    def run(self):
        while True:
            time.sleep(RED_SWITCH_TIME_SEC)
            self._change_color(YELLOW_COLOR)
            print('switched to yellow')
            time.sleep(YELLOW_SWITCH_TIME_SEC)
            self._change_color(GREEN_COLOR)
            print('switched to green')
            time.sleep(GREEN_SWITCH_TIME_SEC)
            self._change_color(RED_COLOR)
            print('switched to red')

    def _change_color(self, color):
        self.__color = color