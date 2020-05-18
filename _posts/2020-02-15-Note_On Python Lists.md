---
title: "Why you shouldn't use python list multiplied with an int"
date: 2020-02-15 00:26:00 +0800
categories: [Python]
tags: [Python]
---

Why shouldn't I write 

```python
lst = [[]] * 3
```

Now do

```python
lst[0].append(1)
print(lst)
# Out: [[1], [1], [1]]
```

You appended 1 to just zero'th index list and it got appended to all. That's why. Reason?

Let's id them all

```bash
>>> id(lst[0])
140318149332096
>>> id(lst[1])
140318149332096
>>> id(lst[2])
140318149332096
```

Everyone has same ID. So you append to one, it will append to rest of them. Spooky?

But this is the fastest way to get a list. Alternatives?

Use

```python
lst = [[] for _ in range(3)]
```

Now let's id them all:

```bash
>>> id(lst[0])
140318149414816
>>> id(lst[1])
140318149469040
>>> id(lst[2])
140318149468960
```

Different ID, so our previous problem wouldn't be repeated.

Chill and enjoy the weekend!

