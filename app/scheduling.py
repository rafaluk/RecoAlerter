from apscheduler.schedulers.background import BackgroundScheduler
import atexit
from app.reco_fetcher import RecoFetcher
from app.history_manager import HistoryManager
from app.email_manager import EmailManager
from app.utils import Constants


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
        history = hm.get_from_file()
        new_only = hm.compare_lists_and_choose_unseen(history, reco_list_new)
        hm.save_new_reco_to_file(new_only)

        # send email
        if len(new_only) > 0:
            em = EmailManager()
            message = em.prepare(new_only)
            subject = '[MDM] New note!'
            em.send(login=Constants.LOGIN, password=Constants.PASSWORD,
                    recipient=Constants.MY_EMAIL, subject=subject, message=message)



