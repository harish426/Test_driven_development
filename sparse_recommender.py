class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.dict = {}

    def set(self, row, col, value):
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise ValueError("index not found")
        if value != 0:
            self.dict[(row, col)] = value
        elif (row, col) in self.dict:
            del self.dict[(row, col)]

    def get(self, row, col):
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise ValueError("index not found")
        return self.dict.get((row, col), 0)

    def recommend(self, vector):
        if len(vector) != self.cols:
            raise ValueError("vector size is not matching with matrix cols")
        result = [0] * self.rows
        for (row, col), value in self.dict.items():
            result[row] += value * vector[col]
        return result

    def add_Movie(self, matrix):
        if (matrix.rows, matrix.cols) != (self.rows, self.cols):
            raise ValueError("Matrix dimensions are not matching")

        result = SparseMatrix(self.rows, self.cols)
        for (row, col), value in self.dict.items():
            result.set(row, col, value + matrix.get(row, col))
        return result

    def to_dense(self):
        dense_matrix = [[0] * self.cols for _ in range(self.rows)]
        for (row, col), value in self.dict.items():
            dense_matrix[row][col] = value
        return dense_matrix
