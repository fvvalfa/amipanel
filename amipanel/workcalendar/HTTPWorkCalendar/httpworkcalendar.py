from calendar import Calendar, HTMLCalendar, monthrange, _nextmonth, _prevmonth, _monthlen, day_abbr
import datetime

from ..models import CalendarDays


class HTTPWorkCalendar(HTMLCalendar):
    # CSS classes for the day <th>s
    cssclasses_weekday_head = ["mon_head", "tue_head", "wed_head", "thu_head", "fri_head", "sat_head", "sun_head"]

    def itermonthdays3(self, year, month):
        """
        Like itermonthdates(), but will yield (year, month, day) tuples.  Can be
        used for dates outside of datetime.date range.
        """
        day1, ndays = monthrange(year, month)
        days_before = (day1 - self.firstweekday) % 7
        if days_before == 0:
            days_before = 7
        days_after = (self.firstweekday - day1 - ndays) % 7
        if days_before+ndays+days_after < 42:
            days_after = days_after+7
        if days_after == 0:
            days_after = 7
        y, m = _prevmonth(year, month)
        end = _monthlen(y, m) + 1
        for d in range(end-days_before, end):
            yield y, m, d
        for d in range(1, ndays + 1):
            yield year, month, d
        y, m = _nextmonth(year, month)
        for d in range(1, days_after + 1):
            yield y, m, d

    # def itermonthdays4(self, year, month):
    #     """
    #     Like itermonthdates(), but will yield (year, month, day, day_of_week) tuples.
    #     Can be used for dates outside of datetime.date range.
    #     """
    #     for i, (y, m, d) in enumerate(self.itermonthdays3(year, month)):
    #         yield y, m, d, (self.firstweekday + i) % 7

    def formatweek(self, theweek):
        """
        Return a complete week as a table row.
        """
        s = ''.join(self.formatday(y, m, d, wd, montstatus)
                    for (y, m, d, wd, montstatus) in theweek)
        return '<tr>%s</tr>' % s

    def formatday(self, year, month, day, weekday, montstatus):
        """
        Return a day as a table cell.
        """
        a = CalendarDays().getday(year=year, month=month, day=day)
        daystatus = 0
        if a is not None:
            daystatus = 2
        
        # print( datetime.date(2012, 13, 14) )
        # d = datetime.date(2022,12, 12 )
     
        
        if montstatus == 0 or daystatus == 0:
            # day outside month
            return '<td class="%s">%d</td>' % (self.cssclass_noday, day)
        else:
            if a.hours == 7:
                return '<td class="%s">%d</td>' % ('preholiday', day)
            if datetime.date.today()==datetime.date(year,month, day ):
                return '<td class="%s %s">%d</td>' % ('currentday', self.cssclasses[weekday], day)
            return '<td class="%s">%d</td>' % (self.cssclasses[weekday], day)

    def monthdays2calendar(self, year, month):
        """
        Return a matrix representing a month's calendar.
        Each row represents a week; week entries are
        (day number, weekday number) tuples. Day numbers outside this month
        are zero.
        """
        dayswithoutzero = list(self.itermonthdays4(year, month))
        dayswithzero = list()
        for item in dayswithoutzero:
            if item[1] == month:
                mothstatus = 1
            else:
                mothstatus = 0
            dayswithzero.append(
                (item[0], item[1], item[2], item[3], mothstatus,))
        #days = list(self.itermonthdays2(year, month))
        a = [dayswithzero[i:i+7] for i in range(0, len(dayswithzero), 7)]
        return a
        # return [ days[i:i+7] for i in range(0, len(days), 7) ]


    def formatmonth(self, theyear, themonth, withyear=True):
        """
        Return a formatted month as a table.
        """
        v = []
        a = v.append
        a('<table  class="%s">' % (
            super().cssclass_month))
        a('\n')
        a(super().formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(super().formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)
