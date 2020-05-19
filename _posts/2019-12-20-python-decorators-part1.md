---
title: "Python Decorators"
date: 2019-12-20 00:26:00 +0800
featured-img: python-logo
categories: [Python3, OOPs]
tags: [Python3]
---
Python Decorators are useful. They help encapsulate the code and it's a good OOP's concept.

```python
import time

class Solution:
    def time_me(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            indice_list = func(*args, **kwargs)
            print("Time taken: ", time.time() - start_time)
            return indice_list
        return wrapper

    @time_me
    def twoSum(self, nums, target):
        for ind1, x in enumerate(nums):
            for ind2, y in enumerate(nums):
                if x + y == target:
                    if ind1 != ind2:
                        return [ind1, ind2]


# People Have used Hash map for this
# Learn more about it

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([1, 2, 3, 4], 6))

```
For example you have to time your function. Would you write that in the same function? Wouldn't it be clumsy? Is it according to OOP's principles? Hell No.

But now if you encapsulate the function with time_me function, you can time your function, without needing to write extra code in the main twoSum function itself. Isn't that cool?

A very good reference for this post is: https://www.python-course.eu/python3_decorators.php

Rest whatever I found don't explain the concept well!

Lemme know your comments below.
