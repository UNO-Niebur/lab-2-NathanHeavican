#FutureTime.py
#Name: Nathan Heavican
#Date: 1/31/26
#Assignment: Lab 2
#Purpose: Create a program that asks the user for a number of hours and minutes, calculates what the time will be after that amount of time passes, and displays the result in HH:MM format

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 12
  currentMinute = now.minute


  #TODO:
  #Ask user for hours
  moreHour = int(input("Enter a number of hours: "))
  #Ask user for minutes
  moreMinute = int(input("Enter a number of minutes: "))
  #Calculate the time after the user-supplied time has passed.
  futureMinute = (currentMinute + moreMinute) % 60
  extraHour = (currentMinute + moreMinute) // 60
  futureHour = (currentHour + moreHour + extraHour) % 12
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  print(f"The future time is {futureHour:02d}:{futureMinute:02d}")
if __name__ == '__main__':
  main()
