import logging
from error import MHException


class Task:
    def __init__(self, task_name, config, export):
        self.log = logging.getLogger('metricHunter')
        self.name = task_name
        self.interval = config.get('interval', 30)
        self.export = export

        else:
            raise MHException('config file has no filed "collector"')
