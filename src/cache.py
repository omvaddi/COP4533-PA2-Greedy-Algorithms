from collections import deque

def read_input(file_path):
    with open(file_path, 'r') as file:
        k, m = map(int, file.readline().split())
        requests = list(map(int, file.readline().split()))
    return k, m, requests

def fifo_cache(file_path):
    k, m, requests = read_input(file_path)

    cache = deque()
    misses = 0
    
    for request in requests:
        if request not in cache:
            if len(cache) < k:
                cache.append(request)
            else:
                cache.popleft()
                cache.append(request)
            misses += 1
    
    return misses


def main():
    print(fifo_cache('tests/test1.txt'))

if __name__ == "__main__":
    main()