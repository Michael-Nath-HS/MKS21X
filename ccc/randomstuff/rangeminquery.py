class rangeMinQuery:
    def trivialAlgo(self, arr, i1, i2):
        record = [[] for x in range(len(arr))]
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                record[i].append(j)
        print(record)
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[record[i][j - 1]] < arr[j]:
                    # print(j)
                    record[i][j].append(record[i][j - 1])
                else:
                    record[i][j].append(j)
        return record[i1][i2]


query = [2, 4, 3, 1, 6, 7, 8, 9, 1, 7]
helper = rangeMinQuery()
helper.trivialAlgo(query, 1, 5)
