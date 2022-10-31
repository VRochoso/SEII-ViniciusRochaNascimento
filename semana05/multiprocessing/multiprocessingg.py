from concurrent.futures
import time

start = time.perf_counter()

def do_some(seconds):
    print(f'Sleeping {seconds} sec...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = executor.map(do_some, secs)
    for result in results:
        print(result)

finish = time.perf_counter()

print(f'finished in {round(finish-start,2)} seconds')