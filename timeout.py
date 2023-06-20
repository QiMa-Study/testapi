# testapi
import sched, time

s = sched.scheduler(time.time, time.sleep)

def print_time():
    print("时间到了！")

s.enter(5, 1, print_time, ())

s.run()
