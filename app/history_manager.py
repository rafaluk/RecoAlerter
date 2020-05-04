import os


class HistoryManager:
    def __init__(self, filename='biba.txt'):
        self._filename = filename
        self._encoding = 'utf-8'

        if not os.path.exists(self._filename):
            open(self._filename, 'w', encoding=self._encoding)

    def get_from_file(self):
        with open(self._filename, 'r', encoding=self._encoding) as file:
            content = file.readlines()
        return [x.strip() for x in content]

    # move to utils
    def compare_lists_and_choose_unseen(self, previous_history: list, new_history: list) -> list:
        return [element for element in new_history if element not in previous_history]

    def save_new_reco_to_file(self, new_history: list):
        with open(self._filename, 'r+', encoding=self._encoding) as file:
            content = file.read()
            file.seek(0, 0)
            for line in new_history:
                file.write(line.rstrip('\r\n') + '\n' + content)