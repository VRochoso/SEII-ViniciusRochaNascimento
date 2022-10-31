import threading
import concurrent.futures
import time


start = time.perf_counter()

def do_some(seconds):
    print(f'Sleeping {seconds} sec...')
    time.sleep(seconds)
    return 'Done Sleeping...'

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 =executor.submit(do_some, 1)
    f2 =executor.submit(do_some, 1)
    print(f1.result())
    print(f2.result())

finish = time.perf_counter()

print(f'finished in {round(finish-start,2)} seconds')