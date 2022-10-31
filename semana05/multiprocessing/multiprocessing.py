import time


start = time.perf_counter()

def do_some():
    print('Sleeping in 1 sec...')
    time.sleep(1)
    print('Done Sleeping...')

do_some()
do_some()

finish = time.perf_counter()

print(f'finished in {round(finish-start,2)} seconds')