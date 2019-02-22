# Algorithm

Let M={m1,m2,m3,......,m(n)} denote set of n men and W={w1,w2,w3,.......,w(n)} denote set of n women. M x W denotes the set of all ordered pairs (m,w) such that m belongs to M and w belongs to W. 
Find a stable matching in M x W.
A stable matching is defined as a matching:
    i) which is perfect (every member of M and W is paired with exactly one member of opposite gender).
    ii) is not instable 
A matching is instable if it contains two pairs (m1,w1) and (m2,w2) such that m1 prefers w2 over w1  and w2 prefers m1 over m2.

Algorithm:-
1) initialize each person to be free
2) while some men is free and hasn't proposed to every women
       Choose such a man m
       let pref=1st women on m's preference list to whom m has not yet proposed
       if w is free
              set (m,w) as engaged
       else if w prefers m over her current partner m1
              set (m,w) as engaged
              m1 is made free
       else
              w rejects m

Input:
The first line denotes the number of member in M and W, followed by preference list of all n men and n women.
Example 1):-
3
2 1 0
0 1 2
1 0 2
1 2 0
0 2 1
1 0 2
Output: 
Pairs:
[0,2] [1,0] [2,1]

Example 2):-
2
0 1
1 0
0 1
1 0
Output:
Pairs:
[0,0] [1,1]
