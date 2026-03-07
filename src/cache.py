from collections import deque
from collections import OrderedDict
import random

def read_input(file_path):
    with open(file_path, 'r') as file:
        k, m = map(int, file.readline().split())
        requests = list(map(int, file.readline().split()))
    return k, m, requests


def call_caches(file_path):
    k, m, requests = read_input(file_path)
    
    fifo_misses = fifo_cache(k, requests)
    lru_misses = lru_cache(k, requests)
    optff_misses = optff_cache(k, m, requests)
    
    print(f"FIFO : {fifo_misses}")
    print(f"LRU : {lru_misses}")
    print(f"OPTFF : {optff_misses}")


def fifo_cache(k, requests):
    cache = deque()
    cache_set = set()
    misses = 0
    
    for request in requests:
        if request not in cache_set:
            if len(cache) == k:
                oldest = cache.popleft()
                cache_set.remove(oldest)
            
            cache.append(request)
            cache_set.add(request)
            misses += 1
    
    return misses


def lru_cache(k, requests):
    cache = OrderedDict()
    misses = 0

    for request in requests:
        if request in cache:
            cache.move_to_end(request)
        else:
            if(len(cache) == k):
                cache.popitem(last = False)
            cache[request] = True
            misses += 1

    return misses        

def optff_cache(k, m, requests):
    cache = dict()
    misses = 0
    
    for i in range(m):
        request = requests[i]
        next_index = m
        for j in range(i + 1, m):
            if request == requests[j]:
                next_index = j
                break
        if request not in cache:
            if(len(cache) == k):
                max_req = -1
                for req in cache:
                    if max_req == -1:
                        max_req = req
                    else:
                        if cache[req] > cache[max_req]:
                            max_req = req
                del cache[max_req]
            misses += 1
        cache[request] = next_index
    
    return misses

def generate_input(filename, k, m):
    with open(filename, "w") as f:
        f.write(str(k) + " " + str(m) + "\n")
        for i in range(m):
            f.write(str(random.randint(1, 20)))
            if i != m - 1:
                f.write(" ")

def main():
    filename = input("Enter input filename: ")
    call_caches(filename)
if __name__ == "__main__":
    main()