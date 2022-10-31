import threading
import time


start = time.perf_counter()

def do_some():
    print('Sleeping in 1 sec...')
    time.sleep(1)
    print('Done Sleeping...')

t1 = threading.Thread(target=do_some)
t2 = threading.Thread(target=do_some)

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print(f'finished in {round(finish-start,2)} seconds')