import sqlite3 as sql
import pandas as pd


# BASIC STATEMENTS
def drop_table(connect, table="", commit=True):
    try:
        if table_exist(connect, table):
            cursor = connect.cursor()
            cursor.execute("DROP TABLE " + table)
            if commit:
                connect.commit()
    except Exception as e:
        print("drop_table() - ", e)


def create_table(connect, table="", columns=(), commit=True):
    """
    :param: table
    :param: columns = ()
    """
    if table != "" and columns != ():
        try:
            cursor = connect.cursor()
            cursor.execute("CREATE TABLE " + table + " " + str(columns))
            if commit:
                connect.commit()
        except Exception as e:
            print("create_table() - ", e)
    else:
        print("create_table() - enter params correctly.")


def table_exist(connect, table=""):
    try:
        cursor = connect.cursor()
        try:
            cursor.execute("SELECT count(*) FROM {}".format(table))
            return True
        except:
            return False
    except Exception as e:
        print("table_exist() - ", e)


# TIMESTAMPS for Live Trade
def get_timestamps_from_livetrade(connect, commit=True):
    try:
        cursor = connect.cursor()
        data = cursor.execute("SELECT timestamp FROM live_trade_timestamps").fetchall()
        result = []
        for i in data:
            result.append(i[0])
        if commit:
            connect.commit()
        return result
    except Exception as e:
        print("ERROR get_timestamps_from_livetrade()", e)
        return []


def insert_timestamp_livetrade(connect, data=(), commit=True):
    try:
        if not table_exist(connect, "live_trade_timestamps"):
            cols = ("timestamp", "")
            create_table(connect, table="live_trade_timestamps", columns=cols, commit=False)
        cursor = connect.cursor()
        cursor.execute("INSERT INTO live_trade_timestamps VALUES" + str(data))
        if commit:
            connect.commit()
    except Exception as e:
        print("insert_timestamp_livetrade() - ", e)


# USER PROCEDURES
def valid_login_password(connect, password="", commit=True):
    try:
        cursor = connect.cursor()
        valid = False
        pws = cursor.execute("SELECT password FROM users").fetchall()
        for i in pws:
            if i[0] == password:
                valid = True
                break
        if commit:
            connect.commit()
        return valid
    except Exception as e:
        print("ERROR valid_user_password()", e)
        return False


def user_data_by_password(connect, password="", commit=True):
    try:
        cursor = connect.cursor()
        x = cursor.execute(
            "SELECT username, tdaccountype, tdaccountid, tdaapi, callback, twiliosid, twilioauth, twiliophone, phone, discordwebhook FROM users WHERE password ='{}'".format(
                password)).fetchall()
        keys = ["username", "tdaccountype", "tdaccountid", "tdaapi",
                "callback", "twiliosid", "twilioauth", "twiliophone",
                "phone", "discordwebhook"]
        obj = {}
        for i, v in enumerate(keys, 0):
            obj[v] = x[0][i]
        if commit:
            connect.commit()
        return obj
    except Exception as e:
        print("ERROR valid_user_password()", e)
        return {'username': '', 'tdaccountype': '', 'tdaccountid': '',
                'tdaapi': '', 'callback': '', 'twiliosid': '',
                'twilioauth': '', 'twiliophone': '', 'phone': '', 'discordwebhook': ''}





