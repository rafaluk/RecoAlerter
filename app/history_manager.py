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

    # todo: move to utils
    def compare_lists_and_choose_unseen(self, previous_history: list, new_history: list) -> list:
        return [element for element in new_history if element not in previous_history]

    def save_new_reco_to_file(self, new_history: list):
        # save at the end of the file - the order is not significant
        with open(self._filename, 'a', encoding=self._encoding) as file:
            for line in new_history:
                file.write(line.rstrip('\r\n') + '\n')