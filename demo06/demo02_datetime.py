#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 练习: 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，
#      以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):

    # 创建时区
    tz = re.match(r'^(UTC)([\+\-]\d{1,2})(\:)(\d{2})$', tz_str)

    tz_num = int(tz.group(2))  # String to number.

    tz_utc = timezone(timedelta(hours=tz_num))

    # 轻质设置时区
    dt_format = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    # print('str -> datetime: ', str(dt_format))

    new_dt = dt_format.replace(tzinfo=tz_utc)
    # print(new_dt)

    return new_dt.timestamp()
    
    

if __name__ == '__main__':
    
    t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
    assert t1 == 1433121030.0, t1

    t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
    assert t2 == 1433121030.0, t2

    print('Pass')
