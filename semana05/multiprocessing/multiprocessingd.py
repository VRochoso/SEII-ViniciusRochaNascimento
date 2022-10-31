import time
import multiprocessing

start = time.perf_counter()

def do_some(seconds):
    print(f'Sleeping {seconds} sec...')
    time.sleep(seconds)
    print('Done Sleeping...')

processes = []

for _ in range(10):
    p = multiprocessing.Process(targe=do_some, args=[1.5])
    p.start()
    processes.append(p)

for process in processes:
    process.join()

finish = time.perf_counter()

print(f'finished in {round(finish-start,2)} seconds')