"""
improt adalah keyword di dalam python yang digunakan untuk memangil modul atau mengakses sebgaigan modul supaya bisa diguanakan di progam kita
bisa juga digunakan untuk menases varibel di vile ekternal

"""

#import seluruh module

import math
print(math.pi)

#import fungsi tertentu saja

from math import sqrt
print(sqrt(16))

# import dengan nama alias pendek
import numpy as num
print(np.array([1, 2, 3]))