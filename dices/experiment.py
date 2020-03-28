from dices import Player
from logger import Logger

from datetime import datetime as dt

class Experiment:

    def __init__(self, event_criteria,
                 experiments_count=100,
                 dices_count=2):

        self.__count = experiments_count
        self.__criteria = event_criteria
        self.__criteria_count = 0
        self.__player = Player(dices_count)

    def run(self):
        self.__criteria_count = 0

        log_file_name = f'experiment_{self.__cur_ts()}'
        with Logger(log_file_name) as log:
            for i in range(0, self.__count):
                self.__player.throw_dices()
                is_criteria_met = \
                        self.__criteria(self.__player.dices_sum())

                if is_criteria_met:
                    self.__criteria_count += 1

                log.info(f'Experiment number {i}:')
                [log.info(report_str) \
                        for report_str in self.__player.throw_info()]
                log.info(f'Is criteria met: {is_criteria_met}\n')

            log.info(f'Frequency probability is: {self.get_probabily()}')

    def get_probabily(self):
        return self.__criteria_count / self.__count

    def __cur_ts(self):
        format_pattern = '%Y_%m_%d_%H_%M_%S'
        return dt.now().strftime(format_pattern)
