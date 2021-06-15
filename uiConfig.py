from PyQt5.QtCore import QTimer, QTime
from PyQt5 import QtGui
import pyautogui
import time
import random


def current_time():
    t = QTime.currentTime().toString()
    am_pm = "pm" if 12 < int(t[:2]) < 23 else "am"
    return t + " " + am_pm


def mouse_synonym():
    return random.choice(['Laboring', 'Toiling', 'Efforting',
                          'Slogging', 'Drudging', 'Servicing',
                          'Grinding', 'Sweating', 'Operating',
                          'Functioning', 'Running', 'Muscling',
                          'Undertaking', 'Pushing', 'Striving',
                          'Stressing', 'Help me I am unwilling'])


class Presets:

    def event_log(self, message):
        t, c = current_time(), self.ui.mouseList.count()
        self.ui.mouseList.setCurrentRow(c-1)
        self.ui.mouseLastUpdate.setText('            {}'.format(t))
        if c > 100:
            self.ui.mouseList.clear()
            self.ui.mouseList.addItem("CLEARED --> {}".format(t))
        self.ui.mouseList.takeItem(c-1)
        self.ui.mouseList.addItem("{} - {}".format(t, message))
        self.ui.mouseList.addItem("")

    def init_ui(self):
        print()
        self.ui.bar.setMaximum(100)
        self.ui.bar.setValue(100)
        self.setWindowIcon(QtGui.QIcon('images/discord.png'))
        # Presets.mouse_loop(self)
        self.ui.close.clicked.connect(lambda: self.close())
        self.ui.minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.startBtn.clicked.connect(lambda: Presets.start(self))
        # self.ui.stopBtn.clicked.connect(lambda: Presets.stop_awake(self))
        # self.ui.spinBox.valueChanged.connect(lambda: Presets.frequency(self))
        # self.ui.timer = QTimer()
        # self.ui.timer.timeout.connect(lambda: Presets.mouse_loop(self))
        # self.ui.timer.start(200)
        # self.ui.stopBtn.hide()
    #
    # def frequency(self):
    #     Presets.event_log(self, "{} Mins".format(self.ui.spinBox.value()))
    #
    def progress_bar_count(self):
        self.ui.SECONDS -= 1
        self.ui.bar.setValue(self.ui.SECONDS)

    def start(self):
        if self.ui.mins.value() != 0.0 or self.ui.hrs.value() != 0.0:
            self.ui.errorMsg.setText("")
            # self.ui.start_timer = QTimer()
            # self.ui.start_timer.timeout.connect(lambda: Presets.awake_loop(self))
            hrs_to_secs, mins_to_secs = (self.ui.hrs.value()*60)*60000, self.ui.mins.value()*60000
            # self.ui.start_timer.start(hrs_to_secs + mins_to_secs)
            self.ui.SECONDS = (hrs_to_secs + mins_to_secs)/1000
            Presets.event_log(self, "Start")
            Presets.event_log(self, "Interval set to {} minutes.".format(self.ui.SECONDS/60))
            self.ui.bar.setMaximum(self.ui.SECONDS)
            self.ui.bar.setValue(self.ui.SECONDS)
            # self.ui.progress_timer = QTimer()
            # self.ui.progress_timer.timeout.connect(lambda: Presets.progress_bar_count(self))
            # self.ui.progress_timer.start(1000)
            # Presets.event_log(self, "Start")
            # self.ui.stopBtn.show()
            # self.ui.startBtn.hide()
        else:
            self.ui.errorMsg.setText("Set an interval! :)")

    def stop(self):
        self.ui.start_timer.stop()
        self.ui.progress_timer.stop()
        self.ui.bar.setMaximum(100)
        self.ui.bar.setValue(100)
        Presets.event_log(self, "Stop")
        self.ui.stopBtn.hide()
        self.ui.startBtn.show()

    def awake_loop(self):
        # nums = [1, 2, -1, -2, 0, 0]
        # for i in range(0, 2):
        #     pos = pyautogui.position()
        #     xpos, ypos = pos[0], pos[1]
        #     pyautogui.moveTo(xpos+random.choice(nums), ypos+random.choice(nums))
        #     pyautogui.moveTo(xpos+random.choice(nums), ypos+random.choice(nums))
        # for i in range(5):
        #     pyautogui.press('ctrl')
        # Presets.event_log(self, mouse_synonym())
        self.ui.SECONDS = (self.ui.spinBox.value() * 60000) / 1000
        self.ui.bar.setMaximum(self.ui.SECONDS)
        self.ui.bar.setValue(self.ui.SECONDS)
    #
    # def mouse_loop(self):
    #     self.ui.mouseTime.setText(current_time())
    #     pos = pyautogui.position()
    #     self.ui.mousexy.setText("({}, {})".format(pos[0], pos[1]))
