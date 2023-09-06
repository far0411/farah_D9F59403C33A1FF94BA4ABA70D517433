def isleapyear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
     return True
  else:
     return False

print("TO FIND IF A YEAR IS A LEAP YEAR OR NOT.")
year = int(input("Enter a year:"))
if isleapyear(year):
  print(year,' is a leap year')
else:
  print(year,' is not a leap year')