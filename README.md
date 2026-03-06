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
