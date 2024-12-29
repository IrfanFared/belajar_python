# date and time 

import datetime
hari_ini = datetime.date.today()
print(hari_ini)

import datetime as dt
hari_ini = dt.date.today()
print(hari_ini)

print(f"hari ini adalaha hari{hari_ini:%A}") # maksu dari %A adalah nama hari dalam seminggu
#output = hari ini adalaha hari Monday
