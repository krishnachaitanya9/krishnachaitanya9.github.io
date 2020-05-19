---
title: "Getting my custom algorithm to work"
date: 2020-01-15 00:26:00 +0800
featured-img: python-logo
categories: [Math]
tags: [Math]
---

So I had this strange problem. I was reading a paper: Open-loop Self-calibration of Articulated Robots with Artificial Skins by Mittendorfer. In page-3 Fig 2 Matrix III: Sort Merged Activity matrix, how do we get the matrix from Matrix II in the same Fig?

To convert the Matrix II in fig (From here on let's just call it Matrix II) you can interchange rows all you want, interchange columns all you want. Nothing other operations are allowed. Finally you have to output the row numbers and column numbers each of them start from 1.

So basically you will be given a matrix, you gotta convert that to a lower triangular matrix. The hints here are that you will be given a binary matrix. So if it's a binary matrix, the sum of all elements of a lower triangular Binary matrix should be less than or equal to $$\frac{n(n+1)}{2}$$ . Good one clue here.

Second if it's a lower triangular matrix, the column sum should be in descending order and the row sum should be ascending order. That's the trick you can use to convert the Matrix II to Matrix III. But there is one problem here. Matrix III is a (n+1$$\times$$n) matrix. One extra row can be anywhere. That will change the row numbers arbitrarily. To counter that we use a small snippet I made:

So for example we have this matrix:

```bash
[1, 1, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 0, 0],
[1, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 0, 1],
[0, 0, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0]
```

And we want to convert it to:

```bash
[0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0],
[1, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[1, 1, 1, 1, 0, 0],
[1, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1]
```



Algorithm:

1) Find the zero'th index and save it. For our application, there can be only one zero array row.

2) Let's assume we found the zero row index. 

3) Now we sort the array, according to row sums and keep them

4) We subtract the index from the array. For example if we have an array

```bash
[3, 0, 5, 2, 4, 1]
```

The zero row index we obtained is 5, we do 

```bash
[3, 0, 5, 2, 4, 1] - 5 = [-2, -5, 0, -3, -1, -4]
```

5) Now imagine if we had this array in it's original place, we would be adding one to some of the indices. Right now we don't know who those indices are, so let's add 1 to all of them. So our example would become:

```bash
[-2, -5, 0, -3, -1, -4] + 1 = [-1, -4, 1, -2, 0, -3]
```

So from this indices matrix we can say that the indices which are greater than 1 are the indices which are above the zero row array in the original array passed. So in the above array anything less than 1 is made zero and add them to the original array [3, 0, 5, 2, 4, 1]. Which would then result in:

```bash
[3, 0, 5, 2, 4, 1] + [0, 0, 1, 0, 0, 0] = [3, 0, 6, 2, 4, 1]
```

As the indices start from 1 we add 1 to elements in above array:

```bash
[3, 0, 6, 2, 4, 1] + 1 = [4, 1, 7, 3, 5, 2]
```

And we add row row array at the top. Mission accomplished!