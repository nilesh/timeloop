from threading import Thread, Event
from datetime import timedelta

class Job(Thread):
    def __init__(self, interval, execute, *args, **kwargs):
        Thread.__init__(self)
        self.stopped = Event()
        self.interval = interval
        self.execute = execute
        self.args = args
        self.kwargs = kwargs

    def stop(self):
        self.stopped.set()
        self.join()

    def run(self):
        while not self.stopped.wait(self.interval.total_seconds()):
            self.execute(*self.args, **self.kwargs)

def sample_func(arg1, arg2, arg3):
    print "returning {} {} {}".format(arg1, arg2, arg3)

if __name__ == "__main__":
    j = Job(timedelta(seconds=5), sample_func, **{"arg1": "sankalp", "arg2": "jonna", "arg3": "newsomething"})
    j.start()
