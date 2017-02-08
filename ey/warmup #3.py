user = raw_input("Welcome to the Days-In-A-Month thing. Type in a month and I'll give you the number of days cause you're lasy :)")

def days_in_month(month, year):

    if month in ['September', 'April', 'June', 'November']:
        print 30

    elif month in ['January', 'March', 'May', 'July', 'August','October','December']:
        print 31

    elif month == 'February' and is_leap_year(year) == True:
        print 29

    elif month == 'February' and is_leap_year(year) == False:
        print 28

def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

print(user + "has" + days_in_month(user,2017))
