import threading
import concurrent.futures
import time


start = time.perf_counter()

def do_some(seconds):
    print(f'Sleeping {seconds} sec...')
    time.sleep(seconds)
    return 'Done Sleeping...'

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = [executor.submit(do_some, sec) for sec in secs]
    
    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(f'finished in {round(finish-start,2)} seconds')