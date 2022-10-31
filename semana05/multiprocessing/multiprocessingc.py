from concurrent.futures import process
import time
import multiprocessing

start = time.perf_counter()

def do_some():
    print('Sleeping in 1 sec...')
    time.sleep(1)
    print('Done Sleeping...')

processes = []

for _ in range(10):
    p = multiprocessing.Process(targe=do_some)
    p.start()
    processes.append(p)

for process in processes:
    process.join()

finish = time.perf_counter()

print(f'finished in {round(finish-start,2)} seconds')