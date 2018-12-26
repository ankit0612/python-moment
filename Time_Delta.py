from datetime import datetime

formt = '%a %d %b %Y %H:%M:%S %z'
for i in range(int(input())):
    print(int((datetime.strptime(input(),formt)-datetime.strptime(input(),formt)).total_seconds()))



    """Where 
    %a = Abbreviate weekday name(Sun,Mon,Tue and so on.)
    %d = Day of the month as decimal form (01,02,03,04,05 and so on)
    %b = Abbreviate months name(Jan,Feb,Mar and so on.)
    %z = UTC offset in the form +HHMM or -HHMM."""

    