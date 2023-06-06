import datetime

#获取当前北京时间
utc_dt = datetime.datetime.utcnow()
beijing_dt = utc_dt.astimezone(datetime.timezone(datetime.timedelta(hours=16)))
formatted = beijing_dt.strftime("%Y-%m-%d_%H")
print(f"北京时间: {beijing_dt.year}年{beijing_dt.month}月{beijing_dt.day}日 "
      f"{beijing_dt.hour}时{beijing_dt.minute}分{beijing_dt.second}秒")
