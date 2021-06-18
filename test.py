# # from date_tools import *
# # import time
# #
# # for i in range(5):
# #     date = datetime.datetime.now()
# #     string_date = date.strftime("%Y-%m-%d %H:%M:%S")
# #     time.sleep(1)
# #     print(string_date)
# # # string_to_date = datetime.datetime.strptime(string_date, "%Y-%m-%d %H:%M:%S")
# # # time.sleep(100)
# # # date2 = datetime.datetime.now()
# # #
# # # seconds_in_day = 24 * 60 * 60
# # # difference = date2 - date
# # # x = divmod(difference.days * seconds_in_day + difference.seconds, 60)
# # # print("Minutes {} seconds {}".format(x[0], x[1]))
# #
# #
# import datetime
#
#
# def datetime_diff(old_datetime, new_datetime, dates_are_strings=True):
#     """
#     String dates should be in this format "%Y-%m-%d %H:%M:%S"
#     """
#     seconds_in_day = 24 * 60 * 60
#     if dates_are_strings:
#         d1 = datetime.datetime.strptime(old_datetime, "%Y-%m-%d %H:%M:%S")
#         d2 = datetime.datetime.strptime(new_datetime, "%Y-%m-%d %H:%M:%S")
#     else:
#         d1, d2 = old_datetime, new_datetime
#     difference = d1 - d2
#     x = divmod(difference.days * seconds_in_day + difference.seconds, 60)
#     minutes, seconds = x[0], x[1]
#     return minutes, seconds
# #
# #
# # d = datetime.datetime.now()
# # time.sleep(2.99999)
# # c = datetime.datetime.now()
# #
# # print(datetime_diff(c, d, False))
#
# def livetrade_timestamp():
#     return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# #
# import datetime
# import database_impl as db
# import sqlite3 as sql
# # CON = sql.connect('userData/user.db')
# # x = db.get_timestamps_from_livetrade(CON, commit=False)
# # date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# # current_date = date.strftime("%Y-%m-%d %H:%M:%S")
# # current_difference = datetime_diff(current_date, x[-1])
# # print(current_difference)
# # previous_difference = datetime_diff(x[-1], x[-2])
# # print(previous_difference)
#
# print(livetrade_timestamp(), type(livetrade_timestamp()))
#
# import time
# CON = sql.connect('userData/user.db')
# # db.drop_table(CON, table="live_trade_timestamps", commit=True)
# time.sleep(10)
# while True:
#     t = livetrade_timestamp()
#     db.insert_timestamp_livetrade(CON, data=(t, ""), commit=True)
#     print(t)
#     time.sleep(70)


