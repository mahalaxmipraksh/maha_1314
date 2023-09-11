# leap year 

"""
year %4==0&
year %100!=0/
year %100==0

"""
def is leap year(year):
if(year%4==0and year% 100 !=0)or year %400==0
return true
else:
return false

year =int(input("enter a year:"))

if is( leap year /year):
  print('{} is a leap year: foramt(year))
        else:
  print('{}is bot a leap year:'format(year))
        