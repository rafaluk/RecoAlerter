from apscheduler.schedulers.background import BackgroundScheduler
import atexit
from app.reco_fetcher import RecoFetcher
from app.history_manager import HistoryManager
from pprint import pprint


class Scheduling:
    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def run(self):
        self.scheduler.add_job(func=self.check_recommendations, trigger="interval",
                               seconds=15)
        self.scheduler.start()
        atexit.register(lambda: self.scheduler.shutdown())

    def check_recommendations(self):
        print("checking recommendations!")
        rf = RecoFetcher()
        www = rf.get_www()
        reco_list_new = rf.get_reco_list(www)

        # history
        hm = HistoryManager()
        # get from file
        history = hm.get_from_file()
        print('history:')
        print(history)
        new_only = hm.compare_lists_and_choose_unseen(history, reco_list_new)
        print('new_only:')
        print(new_only)
        hm.save_new_reco_to_file(new_only)

        # send email
        if len(new_only) > 0:
            pass

        # update history
        # check if new -> send email



