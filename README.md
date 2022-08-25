# bahas_bananas

Baha went to San Francisco because he wanted to buy a cheap banana. There are N stores in San Francisco. A store i has a banana price ar_i. Some stores can be closed time to time. 

Baha will give you Q queries and typ_i, type of each query. 

If a query i has a typ_i=1, Baha gives you a_i, telling the status of the store indexed at a_i changes. If it was open before, it closes. Otherwise, it opens. 

If a query i has a typ_i=2, Baha will give you a_i and b_i. He wants you to tell him the average banana price in the given interval. If the average isn't an integer, you will round it down to the closest integer. If a store is closed in the interval, you won't include that store to average. 

For example, if the store 5 and 7 are closed, the average of interval between indexes 4 and 7 is equal to average(a_4, a_6).

Baha wants you to answer for each query with typ_i=2. If there isn't any open store in the interval, print -1.



Input Format
The first line contains N. Next line contains N integers: ar_1, ar_2, ..., ar_N. 3rd line contains Q, the cumber of queries. The next Q lines contains queries.

Output Format
Average of interval for each query with typ=2. If average isn't an integer, you will round it down to the closest integer.

Constraints
1 ≤ N≤ 10^5
1 ≤ ar_i≤ 10^5
1 ≤ Q ≤ 10^5
1 ≤ a ≤ b ≤ N


Sample Input 1
5
1 5 2 1 4
6
2 1 5
2 2 3
1 3
2 2 3
1 3
2 1 4


Sample Output 1
2
3
5
2
