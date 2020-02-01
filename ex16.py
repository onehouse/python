'''输出指定格式的日期。'''

import datetime
print(datetime.date.today().strftime("%Y-%m-%d"))
date_a = datetime.date(1941, 1, 5)
print(date_a.strftime("%Y-%m-%d"))
date_a_next_month = date_a + datetime.timedelta(days=31)
print(date_a_next_month.strftime("%m/%d/%Y"))
date_a_replaced = date_a.replace(year=date_a.year+1)
print(date_a_replaced.strftime("%m/%d/%Y"))

