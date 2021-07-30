from datetime import datetime

x=input()
date=x+" 2009"

x=datetime.strptime(date, '%d %m %Y').weekday()

days=["Monday", 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
print(days[x])
