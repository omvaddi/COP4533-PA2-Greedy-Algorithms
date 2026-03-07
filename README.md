#Programming Assignment 2: Greedy Algorithms 

Om Vaddi (15302285)  
Thomas Alvarado (65211333)

##Instructions:
- After cloning, run "cd COP4533-PA2-Greedy-Algorithms"
- Create an input file in the files folder.
- See assumptions section for file formatting.
- Run "python src/cache.py".
- Enter the file path when prompted. ex: files/file1.txt
- Read output.

Example input (files/example.txt):  
3 9  
9 1 8 2 3 7 8 6 1

Example output (files/example_output.txt):  
FIFO : 9  
LRU : 9  
OPTFF : 7

Assumptions:
- The first line of the file should be two integers, separated by a space. The first integer represents k, an integer that is greater than
or equal to 1 and represents the cache capacity, and the second integer is m which represents the number of requests. The second line of the file should be a sequence of m numbers, with a space separating each number.
- cache.py includes a generate_input function, which randomly generates an input file that has random requests 1-20. To run it, call
generate_input(filename, k, m) in the main function, where filename is "files/<name>.txt", k is the cache capacity, and m is the number of requests.

Question 1: Empirical Comparison  
Use at least three nontrivial input files (each containing 50 or more requests).

For each file, report the number of cache misses for each policy.  
Input File	    |k	|m	 |FIFO |LRU |OPTFF  
files/file1.txt	|5	|84	 |66   |67  |43  
files/file2.txt |8  |64  |36   |40  |26  
files/file3.txt |10 |66  |33   |31  |22

Briefly comment:
- Does OPTFF have the fewest misses?
Yes, OPTFF had the lowest number of misses for all three input files.  

- How does FIFO compare to LRU?  
FIFO and LRU have very similar number of misses. The differences are small (1-4 misses per file). FIFO had fewer misses than LRU in the first two files, whereas in the third file, LRU had fewer misses than FIFO.

Question 2: Bad Sequence for LRU or FIFO  
For ( k = 3 ), investigate whether there exists a request sequence for which OPTFF incurs strictly fewer misses than LRU (or FIFO).

If such a sequence exists:  
- Construct one.  
Sequence:  
3 9  
9 1 8 2 3 7 8 6 1

Compute and report the miss counts for both policies.  
LRU: 9  
OPTFF: 7

In either case, briefly explain your reasoning.  
OPTFF is the theoretically optimal algorithm because it looks into the future and always makes the best possible eviction, so it will always have the minimum number of misses for any sequence. LRU evicts the least recently used page without knowledge of the future. With a smaller cache size, the difference between OPTFF and LRU (or FIFO) becomes more noticeable because the cache will fill up quicker, leading to more evictions from LRU and FIFO.

Question 3: Prove OPTFF is Optimal  
Let OPTFF be Belady’s Farthest-in-Future algorithm.  
Let ( A ) be any offline algorithm that knows the full request sequence.  
Prove that the number of misses of OPTFF is no larger than that of ( A ) on any fixed sequence.

Let the request sequence r1, r2, …, rn be used on both A and OPTFF simultaneously.  
Let t be the first time when both A and OPTFF have the same cache contents, a cache miss occurs, and OPTFF and A evict different pages.  
Let OPTFF evict page x and A evict page y where x != y

By definition of OPTFF either page x will be evicted no earlier than page y, or x will never be requested again.

Modify A to become A’ which is an algorithm that is the same as A, except at time t instead of evicting y, A’ evicts x. In the future whenever A would evict or load x or y, A’ swaps their roles.

For future requests, since y is requested no later than x, keeping y in cache cannot cause more misses than keeping x in cache.
This means A’ has no more misses than A would, and A’ is the same as OPTFF for another eviction step.

If this is repeated for every disagreement between A and OPTFF then A will be transformed into OPTFF and the number of cache misses will never increase.

Since any offline algorithm that knows the full request sequence can be transformed into OPTFF without increasing the number of misses, OPTFF causes the minimum possible number of misses. Therefore, OPTFF is optimal.
