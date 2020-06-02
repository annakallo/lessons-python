# import time
#
# def foo():
#   print(time.ctime())
#
# while True:
#   foo()
#   time.sleep(1)


# import time, threading
#
# WAIT_SECONDS = 1
#
#
# def foo():
#     print(time.ctime())
#     threading.Timer(WAIT_SECONDS, foo).start()
#
# foo()


#---------------------------------------------------------
#
# import threading, time
#
#
# def foo():
#     print(time.ctime())
#
# WAIT_TIME_SECONDS = 2
#
# ticker = threading.Event()
# while not ticker.wait(WAIT_TIME_SECONDS):
#     foo()

#-------------------------------------------------------

# import threading, time, signal
#
# from datetime import timedelta
#
# WAIT_TIME_SECONDS = 1
#
#
# class ProgramKilled(Exception):
#     pass
#
#
# def foo():
#     print(time.ctime())
#
#
# def signal_handler(signum, frame):
#     raise ProgramKilled
#
#
# class Job(threading.Thread):
#     def __init__(self, interval, execute, *args, **kwargs):
#         threading.Thread.__init__(self)
#         self.daemon = False
#         self.stopped = threading.Event()
#         self.interval = interval
#         self.execute = execute
#         self.args = args
#         self.kwargs = kwargs
#
#     def stop(self):
#         self.stopped.set()
#         self.join()
#
#     def run(self):
#         while not self.stopped.wait(self.interval.total_seconds()):
#             self.execute(*self.args, **self.kwargs)
#
#
# if __name__ == "__main__":
#     signal.signal(signal.SIGTERM, signal_handler)
#     signal.signal(signal.SIGINT, signal_handler)
#     job = Job(interval=timedelta(seconds=WAIT_TIME_SECONDS), execute=foo)
#     job.start()
#
#     while True:
#         try:
#             time.sleep(1)
#         except ProgramKilled:
#             print
#             "Program killed: running cleanup code"
#             job.stop()
#             break
#
#----------------------------------------------------------------------------


import time
# from timeloop import Timeloop
from datetime import timedelta

# tl = Timeloop()

print(help(timedelta))


# @tl.job(interval=timedelta(seconds=2))
# def sample_job_every_2s():
#     print
#     "2s job current time : {}".format(time.ctime())
#
#
# @tl.job(interval=timedelta(seconds=5))
# def sample_job_every_5s():
#     print
#     "5s job current time : {}".format(time.ctime())
#
#
# @tl.job(interval=timedelta(seconds=10))
# def sample_job_every_10s():
#     print
#     "10s job current time : {}".format(time.ctime())
#
#
# if __name__ == "__main__":
#     tl.start(block=True)