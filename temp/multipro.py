import process
import zulipPy
import messenger
from multiprocessing import Process
arr_p = []
p = Process(target=process.ini)
arr_p.append(p)
p = Process(target=zulipPy.runzulip)
arr_p.append(p)
p = Process(target=messenger.start)
arr_p.append(p)
for p in arr_p:
    p.start()
for p in arr_p:
    p.join()