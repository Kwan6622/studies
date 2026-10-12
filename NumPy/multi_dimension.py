import numpy as np

array = np.array([
                [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]
            ])

print(array.ndim)
print(array.shape)

print(array[0][0][0]) #chain indexing
print(array[2,2,1]) #multidimesional indexing

word = array[0,0,0] + " " +  array[1,1,0] + array[1,1,2] + array[1,1,1] + array[2,0,0] + array[2,0,1] + array[0,1,1] + array[1,2,2]
print(word)