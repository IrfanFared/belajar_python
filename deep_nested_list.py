# deep copy adalah sebuah prosen untuk membuat salinan dari sebuah objek
# yang mencakup semua objek yang ada di dalamnya, termasuk objek yang ada di dalam objek tersebut.
import copy
import copy

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

deep[0][0] = 99

print("Original:", original)  # [[1, 2], [3, 4]]
print("Deep Copy:", deep)     # [[99, 2], [3, 4]]
