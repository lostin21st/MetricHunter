from abc import ABCMeta, abstractmethod


class AbsHandler(ABCMeta):

    @abstractmethod
    def conntion(self, *args, **kw):
        pass

    @abstractmethod
    def close(self):
        pass


class AbsCollector(AbsHandler):
    @abstractmethod
    def read(self, *args, **kw):
        pass


class AbsExporter(AbsHandler):
    @abstractmethod
    def write(self, *args, **kw):
        pass
