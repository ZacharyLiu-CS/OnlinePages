import schedule
import time


def schedule_job(record_obj):
    if(len(record_obj.usetimes) < 7):
        record_obj.usetimes.append(0)
        record_obj.falsetimes.append(0)
    else:
        record_obj.usetimes.append(0)
        record_obj.usetimes.pop(0)
        record_obj.falsetimes.append(0)
        record_obj.falsetimes.pop(0)

class Records:
    def __init__(self):
        self.use_total_times = 0
        self.false_total_times = 0
        self.usetimes=[0]*7
        self.falsetimes=[0]*7
        self.falserate=[0.0]*7

    def do_schedule_job(self):
        schedule.every().day.at("23:59").do(schedule_job, self)
        while True:
            schedule.run_pending()
            time.sleep(10)
    def add_use_times(self,time):
        self.usetimes[-1] += time
        self.use_total_times += time

    def add_false_times(self,time):
        self.falsetimes[-1] += time
        self.false_total_times += time


    def get_all_data(self):
        self.falserate =[0.0]*7
        for i in range(len(self.falsetimes)):
            if self.usetimes[i] != 0:
                self.falserate[i]=self.falsetimes[i]*100/self.usetimes[i]
        print(self.__dict__)
        return self.__dict__




