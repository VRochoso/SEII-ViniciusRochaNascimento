import time
import multiprocessing

start = time.perf_counter()

def do_some():
    print('Sleeping in 1 sec...')
    time.sleep(1)
    print('Done Sleeping...')

p1 = multiprocessing.Process(targe=do_some)
p2 = multiprocessing.Process(targe=do_some)

p1.start()
p2.start()

p1.join()
p2.join()

finish = time.perf_counter()

print(f'finished in {round(finish-start,2)} seconds')