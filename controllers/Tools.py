import os
import math


class Tools:

    @staticmethod
    def number_to_time(num):
        hours = 0
        mins = 0
        seconds = 0

        if num > 60:
            mins = math.floor(num/60)
            num -= 60 * mins
            seconds = num
        else:
            mins = 0
            hours = 0
            seconds = num

        if mins >= 60:
            hours = math.floor(mins / 60)
            mins -= 60 * hours

        hours = str(hours)
        mins = str(mins)
        seconds = str(seconds)

        if len(hours) == 1:
            hours = '0' + hours
        if len(mins) == 1:
            mins = '0' + mins
        if len(seconds) == 1:
            seconds = '0' + seconds

        result = hours + ':' + mins + ':' + seconds

        return result
