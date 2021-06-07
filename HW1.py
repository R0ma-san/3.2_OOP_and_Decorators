from datetime import date

class MyCustomDate:

    def __init__(self, day, month, year):
        self.date = date(year, month, day)

    def __str__(self):
        return f'Date: {str(self.date)}'

    def __eq__(self, other):
        return self.date == other

    def __ne__(self, other):
        return self.date != other

    def __lt__(self, other):
        return self.date < other

    def __gt__(self, other):
        return self.date > other

    def __le__(self, other):
        return self.date <= other

    def __ge__(self, other):
        return self.date >= other

    def __add__(self, other):
        day = self.date.day + other.date.day
        month = self.date.month + other.date.month
        year = self.date.year + other.date.year
        if day>30:
            month+=1
            day = day - 30
        if month>12:
            year+=1
            month = month-12
        return date(year, month, day)

    def __sub__(self, other):
        day = self.date.day - other.date.day
        month = self.date.month - other.date.month
        year = self.date.year - other.date.year
        if day<=0:
            month-=1
            day = self.date.day + 30 - other.date.day
        if month<=0:
            year-=1
            month = self.date.month + 12 - other.date.month
        if year<0:
            return f'{year}BC-{month}-{day}'
        else:
            return date(year, month, day)

m1 = MyCustomDate(4, 11, 2004)
m2 = MyCustomDate(24, 1, 2001)
m3 = MyCustomDate(12, 4, 1999)
m4 = MyCustomDate(29, 2, 1976)
m5 = MyCustomDate(19, 10, 1989)

print(m1>m2)
print(m2<m3)
print(m3<=m4)
print(m4>=m5)
print(m5==m1)
print(m3!=m5)
print(m1+m2)
print(m5-m1)