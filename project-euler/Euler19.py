#Author DownToSky
#Euler Problem 19

#Returns True if the input year is a leap year
def isLeapYear(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
#Accepts a day and a list of days. Returns the next day
def NextDay(day,days):
    for i in range(0,len(days)-1):
        if days[i]==day:
            return days[i+1]
    return days[0]
#Accepts a month and a list of months. Returns the name of the next month
def NextMonth(month,months):
    for i in range(0,len(months)-1):
        if months[i]==month:
            return months[i+1]
    return months[0]
#List of days:
days=["Sunday","Monday","Tuesday","Wednesday","Thursday",
    "Friday","Saturday"]
#List of months
months=["January","February","March","April",
        "May","June","July","Agust","September",
        "October","November","December"]
#We need full information for 1 of the days at a time:
#"1 Jan 1900 was a Monday."
dayOfMonth=1        
currentDay=days[1]
currentMonth=months[0]
currentYear=1900
#when StartCounting is True we start looking for sundays at the first day of the month. This is due to the fact that we have to
#reach the year 1901 first from the known day(which its info was above)
StartCounting=False
#Contains the count of sundays at the first day of the month
answer=0
#Traversing all the days from the initial day and counting such sundays
while True:
    if currentYear==1901:#Start counting from 1901
        StartCounting=True
    
    if StartCounting==True and currentDay==days[0] and dayOfMonth==1:
        answer+=1
    
    if dayOfMonth==31 and currentMonth==months[11] and currentYear==2000:#Stop counting at 2001
        break
    
    #If at the end of the month, change dayOfMonth to 1 and if at the end of the year, increase the year by one
    if ( (dayOfMonth==30 and (currentMonth=="September" or currentMonth=="April" or currentMonth=="June" or currentMonth=="November")) or
         (isLeapYear(currentYear)==True and currentMonth=="February" and dayOfMonth==29) or
         (isLeapYear(currentYear)==False and currentMonth=="February" and dayOfMonth==28)or
         (dayOfMonth==31)):
        dayOfMonth=1
        if currentMonth=="December":
            currentYear+=1
        currentMonth=NextMonth(currentMonth,months)
        
    else:
        dayOfMonth+=1
    
    currentDay=NextDay(currentDay,days)
    

print(str(answer))