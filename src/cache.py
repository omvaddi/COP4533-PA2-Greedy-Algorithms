from collections import deque
from collections import OrderedDict

def read_input(file_path):
    with open(file_path, 'r') as file:
        k, m = map(int, file.readline().split())
        requests = list(map(int, file.readline().split()))
    return k, m, requests


def call_caches(file_path):
    k, m, requests = read_input(file_path)
    
    fifo_misses = fifo_cache(k, requests)
    lru_misses = lru_cache(k, requests)
    
    print(f"FIFO : {fifo_misses}")
    print(f"LRU : {lru_misses}")


def fifo_cache(k, requests):
    cache = deque()
    cache_set = set()
    misses = 0
    
    for request in requests:
        if request not in cache:
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

                    
def main():
    call_caches('tests/test1.txt')

if __name__ == "__main__":
    main()