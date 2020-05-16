---
title: "PyTorch Explain with code"
date: 2020-05-15 00:26:00 +0800
categories: [Deep_Learning]
tags: [Deep_Learning]
---
In the below snippet we will learn basic tensor attributes using the code

```python
import torch
import numpy as np

if __name__ == "__main__":
    # Ways to make an empty tensor
    t = torch.Tensor()
    print(f"Type of t: {t.type()}")
    # There are also 3 attributes
    print(t.dtype)
    # Prints torch.float32 means it contains float32 values
    print(t.device)
    # Prints what device the tensor is on. Like on CPU or GPU along with their number
    print(t.layout)
    # Prints torch.strided. stride means stride is a tuple indicating the number of elements in the storage
    # that have to be skipped when the index is increased by 1 in each dimension.
    ########################################
    t1 = torch.tensor([1, 2, 3])
    # t1.dtype is torch.int64
    t2 = torch.tensor([1.0, 2.0, 3.0])
    # t2.dtype is torch.float32
    # If you add both of them t1 + t2 it will result in exception as both are of different data type.
    #########################################
    t1 = torch.tensor([1, 2, 3])
    # t1.dtype is torch.int64
    t2 = t1.cuda()
    # t2.dtype is torch.float32
    # If you add both of them t1 + t2 it will result in exception as both are in different device
    ##########################################
    # Constructing Tensors from numpy
    # There are 4 ways
    data = np.array([1, 2, 3])  # A numpy array of type int32
    test_type = torch.Tensor(data)  # Type: Tensor, no dtype specified
    print(test_type.dtype)  # <class 'torch.Tensor'> type: Float32
    test_type = torch.tensor(data)
    print(test_type.dtype)  # <class 'torch.Tensor'> type: Int64
    test_type = torch.as_tensor(data)
    print(test_type.dtype)  # <class 'torch.Tensor'> type: Int64
    test_type = torch.from_numpy(data)
    print(test_type.dtype)  # <class 'torch.Tensor'> type: Int64
    # In conclusion don't use Tensor with capital T. use small t tensor to appropriately convert your data along with
    # data type
    ##########################################
    # Options to creating tensor without data
    print(torch.eye(2))
    # Print identity matrix
    # tensor([[1., 0.],
    #         [0., 1.]])
    print(torch.zeros(2, 2))
    # Makes a zero array of given shape
    # tensor([[0., 0.],
    #         [0., 0.]])
    print(torch.ones(2, 2))
    # Makes a ones array of given shape
    # tensor([[1., 1.],
    #         [1., 1.]])
    print(torch.rand(2, 2))
    # Makes a array of random elements within 0 and 1 in given shape
    # tensor([[0.8905, 0.8360],
    #         [0.8074, 0.8040]])
    ##########################################
    # Adding two Tensors
    x = torch.tensor([5, 3])
    y = torch.tensor([2, 1])
    out = x * y
    out = out.cuda()
    print(out)

```

The stride is explained well by the below image:

![PyTorch Stride](/assets/img/pytorch_explained/stride_and_size.png)
Reference: https://medium.com/@duyanhnguyen_38925/deep-learning-meets-pytorch-part-2-1524a4345aa9

