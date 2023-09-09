import calendar
yr=int(input("enter year"))
if calendar.isleap(yr):
  print(yr,"Is a leep year")
else:
  print(yr,"Is not a leep year")