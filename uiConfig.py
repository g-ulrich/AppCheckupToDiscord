from PyQt5.QtCore import QTimer, QTime
from PyQt5 import QtGui, QtWidgets
import time
import random
import os
import datetime
import requests
import sqlite3 as sql
import database_impl as db
from date_tools import dt


def datetime_diff(old_datetime, new_datetime, dates_are_strings=True):
    """
    String dates should be in this format "%Y-%m-%d %H:%M:%S"
    """
    seconds_in_day = 24 * 60 * 60
    if dates_are_strings:
        d1 = datetime.datetime.strptime(old_datetime, "%Y-%m-%d %H:%M:%S")
        d2 = datetime.datetime.strptime(new_datetime, "%Y-%m-%d %H:%M:%S")
    else:
        d1, d2 = old_datetime, new_datetime
    difference = d1 - d2
    x = divmod(difference.days * seconds_in_day + difference.seconds, 60)
    minutes, seconds = x[0], x[1]
    return minutes, seconds


def current_time():
    t = QTime.currentTime().toString()
    am_pm = "pm" if 12 < int(t[:2]) < 23 else "am"
    return t + " " + am_pm


def message_discord_server(message, user_data={}):
    try:
        discord_webhook_url = user_data['discordwebhook']
        Message = {
            "content": str(message)
        }
        requests.post(discord_webhook_url, data=Message)
    except Exception as e:
        print("ERROR discord", e)


class Presets:

    def event_log(self, message):
        t, c = current_time(), self.ui.mouseList.count()
        self.ui.mouseList.setCurrentRow(c-1)
        self.ui.mouseLastUpdate.setText('            {}'.format(t))
        if c > 100:
            self.ui.mouseList.clear()
            self.ui.mouseList.addItem("CLEARED --> {}".format(t))
        self.ui.mouseList.takeItem(c-1)
        self.ui.mouseList.addItem("[{}] {}".format(t, message))
        self.ui.mouseList.addItem("")

    def init_ui(self):
        self.ui.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.bar.setMaximum(100)
        self.ui.bar.setValue(100)
        self.setWindowIcon(QtGui.QIcon('images/discord.png'))
        # Presets.mouse_loop(self)
        self.ui.close.clicked.connect(lambda: self.close())
        self.ui.minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.startBtn.clicked.connect(lambda: Presets.start(self))
        self.ui.stopBtn.clicked.connect(lambda: Presets.stop(self))
        self.ui.password.returnPressed.connect(lambda: Presets.start(self))
        self.ui.stopBtn.hide()

    def progress_bar_count(self):
        self.ui.SECONDS -= 1
        self.ui.bar.setValue(self.ui.SECONDS)

    def start(self):
        CON = sql.connect('userData/user.db')
        if db.valid_login_password(CON, self.ui.password.text(), commit=False) and not db.select_stop_session_status(CON, commit=False):
            self.ui.user_data = db.user_data_by_password(CON, self.ui.password.text(), commit=False)
            if self.ui.mins.value() != 0.0 or self.ui.hrs.value() != 0.0:
                self.ui.start_timer = QTimer()
                self.ui.start_timer.timeout.connect(lambda: Presets.awake_loop(self))
                hrs_to_secs, mins_to_secs = (self.ui.hrs.value() * 60) * 60000, self.ui.mins.value() * 60000
                self.ui.start_timer.start(hrs_to_secs + mins_to_secs)
                self.ui.SECONDS = (hrs_to_secs + mins_to_secs) / 1000
                Presets.event_log(self, "Start")
                Presets.event_log(self, "Interval set to {} minute(s).".format(self.ui.SECONDS / 60))
                self.ui.bar.setMaximum(self.ui.SECONDS)
                self.ui.bar.setValue(self.ui.SECONDS)
                self.ui.progress_timer = QTimer()
                self.ui.progress_timer.timeout.connect(lambda: Presets.progress_bar_count(self))
                self.ui.progress_timer.start(1000)
                self.ui.stopBtn.show()
                self.ui.startBtn.hide()
            else:
                Presets.event_log(self, "Set an interval! :)")
        else:
            if not db.valid_login_password(CON, self.ui.password.text(), commit=False):
                Presets.event_log(self, "Enter an application password. :)")
            if db.select_stop_session_status(CON, commit=False):
                Presets.event_log(self, "Start live trading session. :)")

    def stop(self):
        self.ui.start_timer.stop()
        self.ui.progress_timer.stop()
        self.ui.bar.setMaximum(100)
        self.ui.bar.setValue(100)
        Presets.event_log(self, "Stop")
        self.ui.stopBtn.hide()
        self.ui.startBtn.show()

    def awake_loop(self):
        CON = sql.connect('userData/user.db')
        data = db.get_timestamps_from_livetrade(CON, commit=False)
        # current set
        current_min_diff, sec1 = datetime_diff(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), data[-1])
        # last set
        previous_min_diff, sec2 = datetime_diff(data[-1], data[-2])
        #second to last set
        min3, sec3 = datetime_diff(data[-2], data[-3])
        message = ""
        """
        if interval check is greater than min diff then success
        """
        checkup_interval = self.ui.mins.value() + (self.ui.hrs.value() * 60)
        livetrade_loop_rate = min3 if previous_min_diff == min3 else "unknown"

        if data[-1] != "2000-01-01 00:00:00":
            if checkup_interval < current_min_diff:
                message = "```diff\n-Error! Application stopped live trading!\n-Stoppage occurred after: {}\n``` ".format(data[-1])

            elif current_min_diff > previous_min_diff:
                message = "```ini\n[Warning! Application either slowed down or stopped live trading.]\n[Last loop occurrence: {}]\n``` ".format(data[-1])

            else:
                message = "```diff\n+Success! Application is live trading.\n+Last loop occurrence: {}\n+Live Trade Loop Rate: {} minute(s)``` ".format(data[-1], livetrade_loop_rate)
        else:
            lastItem = self.ui.mouseList.currentItem()
            if "check." != lastItem:
                db.drop_table(CON, "live_trade_timestamps", commit=True)
                db.insert_timestamp_livetrade(CON, data=("2000-01-01 00:00:00", ""), commit=False)
                db.insert_timestamp_livetrade(CON, data=("2000-01-01 00:00:00", ""), commit=False)
                db.insert_timestamp_livetrade(CON, data=("2000-01-01 00:00:00", ""), commit=True)
                Presets.event_log(self, "Market Closed: bypassing check.")
                message = "Market Closed: bypassing check."

        if message != "":
            message_discord_server(message, self.ui.user_data)

        Presets.event_log(self, "\n"+message.replace("'''", "").replace("diff", "").replace("ini"))
        hrs_to_secs, mins_to_secs = (self.ui.hrs.value() * 60) * 60000, self.ui.mins.value() * 60000
        self.ui.SECONDS = (hrs_to_secs + mins_to_secs)/1000
        self.ui.bar.setMaximum(self.ui.SECONDS)
        self.ui.bar.setValue(self.ui.SECONDS)


