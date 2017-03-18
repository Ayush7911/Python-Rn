dob=input(('enter your DOB (yyyy-mm-dd): '))
date_parts=dob.split('-')
[year,month,day]=date_parts
dob_timestamp=float(year)+float(month)/12+float(day)/365
#calcuta toidays timestamp in yeaars
#instead of nenglish date, we can write nepali date....
[today_year,today_month,today_day]=['2017','03','18']
today_timestamp=float(today_year)+float(today_month)/12+float(today_day)/365

#copute the difference

years=today_timestamp - dob_timestamp
months=(years-int(years))*12

print('Your name is %d years %d months' %(years , months))