import datetime

class TimeOfDay:
    def get_current_time(self):
        now = datetime.datetime.now()
        return now.hour  # Return the current hour (0-23)

