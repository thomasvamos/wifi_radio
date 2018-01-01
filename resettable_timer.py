#!/usr/bin/python
from threading import Thread, Event
import time
from time import sleep

class ResettableTimer(Thread):
    """Call a function after a specified number of seconds:
            t = Timer(30.0, f, args=None, kwargs=None)
            t.start()
            t.cancel()     # stop the timer's action if it's still waiting
    """

    def __init__(self, interval, function, args=None, kwargs=None):
        Thread.__init__(self)
        self.interval = interval
        self.function = function
        self.args = args if args is not None else []
        self.kwargs = kwargs if kwargs is not None else {}
        self.finished = Event()
        self.resetted = True

    def cancel(self):
        """Stop the timer if it hasn't finished yet."""
        self.finished.set()

    def reset(self):
        self.resetted = True
        self.finished.set()
        self.finished.clear()

    def run(self):

        while self.resetted:
            self.resetted = False
            self.finished.wait(self.interval)

        self.finished.wait(self.interval)
        if not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
        self.finished.set()


def foo():
    print 'Hello!'

if __name__ == '__main__':
    print "Starting timer"

    timer = InterruptableTimer(5, foo)
    timer.start()
    sleep(4)
    print "resetting timer"
    timer.reset()
    sleep(4)
    print "resetting timer again"
    timer.reset()

    raw_input("Press Enter to continue...")

