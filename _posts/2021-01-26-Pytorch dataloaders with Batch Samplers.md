---
title: "PyTorch Batch Samplers Example"
date: 2020-09-28 00:26:00 +0800
featured-img: pytorch-logo
categories: [PyTorch]
tags: [PyTorch]
---
This is a series of learn code by comments where I try to explain myself by writing a small dummy code that's easy to understand
and then apply in real deep learning problems

In this code Batch Samplers in PyTorch are explained:

```python
from torch.utils.data import Dataset
import numpy as np
from torch.utils.data import DataLoader
from torch.utils.data.sampler import Sampler


class SampleDatset(Dataset):
    """This is a simple datset, to show how to construct a sampler for better understanding how the samplers work in
    Pytorch

    Parameters
    ----------
    Dataset : [type]
        [description]
    """

    def __init__(self):
        self.x = np.arange(100)

    def __len__(self):
        return len(self.x)

    def __getitem__(self, idx):
        return self.x[idx]


class SamplerTest(Sampler):
    def __init__(self, dataset: Dataset):
        self.dataset = dataset
        self.output_indices = [
            [30, 3, 51, 95, 39, 68, 89, 12, 38, 10, 31, 72, 36, 50, 93, 90],
            [44, 13, 70, 49, 61, 57, 34, 45, 24, 32, 40, 21, 92, 27, 94, 67],
            [81, 43, 1, 54, 23, 66, 16, 58, 8, 18, 98, 60, 53, 56, 59, 48],
            [64, 46, 91, 19, 7, 11, 42, 41, 71, 5, 4, 26, 97, 33, 84, 79],
            [47, 28, 0, 87, 37, 78, 88, 82, 35, 75, 15, 63, 76, 80, 99, 22],
            [65, 29, 6, 86],
        ]

    def __iter__(self):
        # Assume we do some mumbo jumbo vodoo here
        # I am gonna fix the output of each batch, but somebody else can write some code here
        # tensor([30,  3, 51, 95, 39, 68, 89, 12, 38, 10, 31, 72, 36, 50, 93, 90])
        # tensor([ 9, 83, 62, 85, 14, 73, 96, 20, 17, 25, 74, 55, 69,  2, 77, 52])
        # tensor([44, 13, 70, 49, 61, 57, 34, 45, 24, 32, 40, 21, 92, 27, 94, 67])
        # tensor([81, 43,  1, 54, 23, 66, 16, 58,  8, 18, 98, 60, 53, 56, 59, 48])
        # tensor([64, 46, 91, 19,  7, 11, 42, 41, 71,  5,  4, 26, 97, 33, 84, 79])
        # tensor([47, 28,  0, 87, 37, 78, 88, 82, 35, 75, 15, 63, 76, 80, 99, 22])
        # tensor([65, 29,  6, 86])
        return iter(self.output_indices)

    def __len__(self):
        return len(self.dataset)


if __name__ == "__main__":
    test_sampledataset = SampleDatset()
    test_sampledataloader = DataLoader(
        test_sampledataset, batch_size=16, shuffle=True, num_workers=2, pin_memory=True, drop_last=False
    )
    for x in test_sampledataloader:
        # This will print in shuffled format tensors
        # Making shuffle=True automatically activates in inner sampler. In PyTorch's own words:
        # A sequential or shuffled sampler will be automatically constructed based on the shuffle argument to a DataLoader.
        print(x)
        # The above print statement is as follows:
        # tensor([66, 83, 38, 70, 69, 39, 65,  9, 52, 51, 93, 19, 60, 84,  6, 25])
        # tensor([92, 50, 81, 73, 17, 15,  0, 58,  2, 77, 27, 18, 13, 68, 49, 64])
        # tensor([85, 80, 24, 36, 33, 91, 76,  8, 82, 11, 96, 46, 48, 47, 72, 41])
        # tensor([20, 56, 23, 90, 10, 61, 37, 53, 74,  1, 26,  3, 42, 79, 75, 97])
        # tensor([21,  7,  4, 95, 34, 28, 98, 40, 12, 59, 87, 94, 14, 22, 30, 62])
        # tensor([86, 89, 31,  5, 88, 45, 43, 54, 71, 55, 29, 67, 63, 57, 78, 32])
        # tensor([44, 16, 99, 35])
        # the data set is a list of numbers from 0 to 99, the numbers are coming in jumbled form because we
        # have passed shuffle=True
    # Now let's look at Batch Sampler. What is Batch Sampler:
    # A custom Sampler that yields a list of batch indices at a time can be passed as the batch_sampler argument.
    # Automatic batching can also be enabled via batch_size and drop_last arguments.
    # Ohhh, does that mean we can pass over our own Batch Sampler?
    # torch.utils.data.BatchSampler takes indices from your Sampler() instance and
    # returns it as list so those can be used in your SampleDatset __getitem__ method
    # batch_sampler option is mutually exclusive with batch_size, shuffle, sampler, and drop_last, so don't pass
    # aforementioned arguments to dataloader as discussed if you pass these arguments, pytorch makes own batch sampler for us
    my_sampler = SamplerTest(test_sampledataset)
    print("Testing Sampler ....")
    test_samplesampler = DataLoader(test_sampledataset, batch_sampler=my_sampler)
    for x in test_samplesampler:
        print(x)
        # Below will print
        # [30, 3, 51, 95, 39, 68, 89, 12, 38, 10, 31, 72, 36, 50, 93, 90],
        # [44, 13, 70, 49, 61, 57, 34, 45, 24, 32, 40, 21, 92, 27, 94, 67],
        # [81, 43, 1, 54, 23, 66, 16, 58, 8, 18, 98, 60, 53, 56, 59, 48],
        # [64, 46, 91, 19, 7, 11, 42, 41, 71, 5, 4, 26, 97, 33, 84, 79],
        # [47, 28, 0, 87, 37, 78, 88, 82, 35, 75, 15, 63, 76, 80, 99, 22],
        # [65, 29, 6, 86]
        # Which is exactly same as SamplerTest 's output_indices, because the original dataset is a list of
        # numbers from 0 to 99. so test_sampledataset[31] = 31, test_sampledataset[64] = 64. . But when you shuffle your
        # dataset, and they aren't uniform numbers from 0 to 99, then you will get output as different random numbers

```

