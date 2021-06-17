import datetime


class dt:
    def weekend(n=999):
        """
        :return bool:
        n = 0, 1, 2, 3, 4, 5, 6
        """
        n = datetime.datetime.today().weekday() if n == 999 else n
        return True if n in [5, 6] else False

    def choose_format(choice="%m/%d/%Y, %H:%M:%S"):
        return datetime.datetime.today().strftime(choice)

    def datetime_yyyymmdd(num_of_days=0, future=False):
        if num_of_days != 0 and not future:
            return datetime.datetime.today() - datetime.timedelta(days=num_of_days)
        elif future and num_of_days != 0:
            return datetime.datetime.today() + datetime.timedelta(days=num_of_days)
        else:
            return datetime.datetime.today()

    def convert_yyyymmdd_to_datetime(date=""):
        return datetime.datetime.strptime(date, '%Y-%m-%d')

    def yyyymmdd(days_ago=0):
        if days_ago == 0:
            return dt.choose_format('%Y-%m-%d')
        else:
            x = datetime.datetime.today() - datetime.timedelta(days=days_ago)
            return x.strftime("%Y-%m-%d")

    def mmddyyyyhhmmss(string=True):
        x = dt.choose_format('%m/%d/%Y, %H:%M:%S')
        return x if string else int(x.replace("/", "").replace(",", "").replace(" ", "").replace(":", ""))

    def time_now(floater=True):
        x = dt.choose_format("%H:%M")
        return float(x.replace(":", ".")) if floater else x

    def timestamp_now(string=True):
        x = datetime.datetime.today().timestamp()
        return str(x).replace(".", "")[:10] + "000" if string else x

    def date_now(string=False):
        x = datetime.datetime.today()
        return str(x) if string else x

    def date_n_days_ago(n=1, string=False):
        x = datetime.datetime.today() - datetime.timedelta(days=n)
        return str(x) if string else x

    def date_n_years_ago(n=1, string=False):
        x = datetime.datetime.today() - datetime.timedelta(days=n * 365)
        return str(x) if string else x

    def timestamp_n_days_ago(n=1, string=True):
        x = datetime.datetime.today() - datetime.timedelta(days=n)
        return str(x.timestamp()).replace(".", "")[:10] + "000" if string else x.timestamp()

    def timestamp_n_years_ago(n=1, string=True):
        x = datetime.datetime.today() - datetime.timedelta(days=n * 365)
        return str(x.timestamp()).replace(".", "")[:10] + "000" if string else x.timestamp()

    def expires_in_n_minutes(n=25):
        return datetime.datetime.now() + datetime.timedelta(minutes=n)

    def expires_in_n_days(n=85):
        return datetime.datetime.now() + datetime.timedelta(days=n)

    def convert_timestamps_to_datetimes(ts=[]):
        if isinstance(ts, list):
            result = []
            for i in ts:
                result.append(dt.convert_timestamps_to_datetimes(i))
            return result
        if isinstance(ts, str):
            return datetime.datetime.fromtimestamp(int(ts[:10])).isoformat()
        else:
            return datetime.datetime.fromtimestamp(int(str(ts)[:10])).isoformat()

    def datetime_str_day_difference(past, present):
        past = datetime.datetime.strptime(past[:10], '%Y-%m-%d')
        present = datetime.datetime.strptime(present[:10], '%Y-%m-%d')
        return (past - present).days