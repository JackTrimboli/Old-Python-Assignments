def matrixReshape(mat, r, c):
        helperList = []
        for row in mat:
            for val in row:
                helperList.append(val)
        #all values should be contained in helperList
        if (len(helperList)) / r == c:
            res = []
            row = []
            counter = 0
            for x in helperList:
                if counter == c: #if we've reach the necessary num values in a row, reset and add the row to the matrix
                    counter = 0
                    res.append(row)
                    row = []
                row.append(x)
                counter += 1
            return res
        else:
            return mat

testcase = [[1,2],[3,4]]
print(matrixReshape(testcase, 1, 4))