#Q5

matrix = eval(input('enter matrix: '))
rows = int(input('enter r: '))
columns = int(input('enter c: '))
   
def reshape(mat,r,c):
    ro = len(mat)
    co = len(mat[0])
    if ro*co != r*c:
        return 'Invalid Dimensions'

    new_mat = []
    flat = []
    for i in range(len(mat)):
        for j in mat[i]:
            flat.append(j)
    index = 0
    for i in range(r):
        new_mat.append([])
        for j in range(c):
            new_mat[i].append(flat[index])
            index += 1

    return new_mat


print(reshape(matrix,rows,columns))

'''
ojasmittal@pop-os ~/D/Code> python3 q5.py
enter matrix: [[13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24]]
enter r: 2
enter c: 6
[[13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24]]
ojasmittal@pop-os ~/D/Code> python3 q5.py
enter matrix: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
enter r: 39
enter c: 2
Invalid Dimensions
'''
    




