Title: MAW Chapter 7: Sorting writing questions
Date: 2017-03-26 12:01
Category: Data Struct & Algo
Tags: sorting, proof, math, maw
Summary: My solutions to selected problems in MAW Chapter 7

## Solutions

including: MAW 7.1, 7.2

### MAW 7.1

> Sort the sequence 3,1,4,1,5,9,2,6,5 using insertion sort.

| index    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|----------|---|---|---|---|---|---|---|---|---|
| original | 3 | 1 | 4 | 1 | 5 | 9 | 2 | 6 | 5 |
|----------|---|---|---|---|---|---|---|---|---|
| pass 1   | 1 | 3 | 4 | 1 | 5 | 9 | 2 | 6 | 5 |
| pass 2   | 1 | 3 | 4 | 1 | 5 | 9 | 2 | 6 | 5 |
| pass 3   | 1 | 1 | 3 | 4 | 5 | 9 | 2 | 6 | 5 |
| pass 4   | 1 | 1 | 3 | 4 | 5 | 9 | 2 | 6 | 5 |
| pass 5   | 1 | 1 | 3 | 4 | 5 | 9 | 2 | 6 | 5 |
| pass 6   | 1 | 1 | 2 | 3 | 4 | 5 | 9 | 6 | 5 |
| pass 7   | 1 | 1 | 2 | 3 | 4 | 5 | 6 | 9 | 5 |
| pass 8   | 1 | 1 | 2 | 3 | 4 | 5 | 5 | 6 | 9 |

### MAW 7.2

> What is the running time of insertion sort if all keys are equal?

If you take a look at the code on p. 220, you can see that inner for loop checks
`A[j-1] > tmp` and it will fail immediately. Thus, the running time is $O(N)$.