---
title: "Python Decorators"
date: 2019-12-20 00:26:00 +0800
categories: [Python3, OOPs]
tags: [Python3]
---
Python Decorators are useful. They help encapsulate the code and it's a good OOP's concept. But you have to use it carefully. For example let's start with simple python. 

```python
import time

class Solution:
    def test_deco(func):
        def wrapper(*args, **kwargs):
            print("test deco start")
            return_things != func(*args, **kwargs)
            print("test deco end")
            return return_things

        return wrapper

    @test_deco
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