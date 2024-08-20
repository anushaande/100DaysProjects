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