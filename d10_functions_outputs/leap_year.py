# - on every year that is divisible by 4 with no reminder
# - except every year that is evenly divisible by 100 with no reminder
# - unless the year is also divisible by 400 with no reminder

def is_leap_year(year):
    if int(year)%4 == 0:
        if int(year)%100 == 0:
            if int(year)%400 == 0:
                print("leap")
            else:
                print("not leap")
        else:
            print("not leap")
    else:
        print("not leap")

is_leap_year(2000)

#2100
#2000
#2400
#1989
