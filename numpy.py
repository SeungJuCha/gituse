import numpy as np
import torch

a = torch.FloatTensor([[[1,2,3],
[4,5,6]],[[1,2,3],[4,5,6]]])

print(a.shape)
print(a.ndim)