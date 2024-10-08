#!/usr/bin/env python3

import numpy as np
x = [2, 8, 9, 48, 8, 22, -12, 2]
y = np.array(x)

print ("Original array:",x)
print ("New array: " + "[" + ", ".join(map(str, y + 2)) + "]")
