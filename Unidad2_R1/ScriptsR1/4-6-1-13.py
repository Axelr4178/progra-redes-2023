"""
    Autor:Axel Alejandro Almaguer Rodriguez
    Descripcion: Problemas Python Institute
"""

import calendar

class Calendar:
    pass


class MyCalendar(Calendar):
    def __init__(self):
        Calendar.__init__(self)


    def __str__(self, result):
        print(str(result))


    def count_weekday_in_year(self, year, weekday):
        y = year
        wd = weekday
        cal = calendar.Calendar()
        weekday_counter = 0


        for month in range(12):
            month += 1
            for week in cal.monthdays2calendar(y, month):
                for day in week:
                    if day[1] == wd and day[0] != 0:
                        weekday_counter += 1


        self.__str__(weekday_counter)


obj = MyCalendar()
obj.count_weekday_in_year(2000, 6)
