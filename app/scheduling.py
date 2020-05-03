from apscheduler.schedulers.background import BackgroundScheduler
import atexit


class Scheduling:
    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def run(self):
        self.scheduler.add_job(func=self.check_recommendations, trigger="interval",
                               seconds=2)
        self.scheduler.start()
        atexit.register(lambda: self.scheduler.shutdown())

    def check_recommendations(self):
        print("checking recommendations!")

