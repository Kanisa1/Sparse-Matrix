import os
import sys

class SparseMatrix:
    def __init__(self, rows=0, cols=0):
        self.rows = rows
        self.cols = cols
        self.data = {}  # Dictionary to store non-zero values {(row, col): value}

    @staticmethod
    def from_file(file_path):
        try:
            with open(file_path, 'r') as f:
                lines = f.readlines()
                rows = int(lines[0].strip().split('=')[1])
                cols = int(lines[1].strip().split('=')[1])
                matrix = SparseMatrix(rows, cols)
                for line in lines[2:]:
                    line = line.strip()
                    if not line:
                        continue
                    if line[0] != '(' or line[-1] != ')':
                        raise ValueError("Input file has wrong format")
                    row, col, value = map(int, line[1:-1].split(','))
                    matrix.set_element(row, col, value)
                return matrix
        except Exception as e:
            raise ValueError(f"Error processing file {file_path}: {e}")

    def set_element(self, row, col, value):
        if value != 0:
            self.data[(row, col)] = value
        elif (row, col) in self.data:
            del self.data[(row, col)]

    def get_element(self, row, col):
        return self.data.get((row, col), 0)

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for addition")
        result = SparseMatrix(self.rows, self.cols)
        for (row, col), value in self.data.items():
            result.set_element(row, col, value + other.get_element(row, col))
        for (row, col), value in other.data.items():
            if (row, col) not in self.data:
                result.set_element(row, col, value)
        return result

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for subtraction")
        result = SparseMatrix(self.rows, self.cols)
        for (row, col), value in self.data.items():
            result.set_element(row, col, value - other.get_element(row, col))
        for (row, col), value in other.data.items():
            if (row, col) not in self.data:
                result.set_element(row, col, -value)
        return result

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError(f"Matrix dimensions must match for multiplication: {self.cols} (cols) != {other.rows} (rows)")
        result = SparseMatrix(self.rows, other.cols)
        for (row, col), value in self.data.items():
            for k in range(other.cols):
                if (col, k) in other.data:
                    result.set_element(row, k, result.get_element(row, k) + value * other.get_element(col, k))
        return result

    def to_file(self, file_path):
        with open(file_path, 'w') as f:
            f.write(f"rows={self.rows}\n")
            f.write(f"cols={self.cols}\n")
            for (row, col), value in sorted(self.data.items()):
                f.write(f"({row}, {col}, {value})\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: python Matrix.py <operation>")
        print("Available operations: add, subtract, multiply")
        return

    operation = sys.argv[1]

    os.makedirs(r'/dsa/sparse_matrix/sample_inputs', exist_ok=True)
    os.makedirs(r'/dsa/sparse_matrix/sample_results', exist_ok=True)

    input_file1 = r'C:\Users\HP\Desktop\Matrix\Sparse-Matrix\sample_inputs\sample_input_01.txt'
    input_file2 = r'C:\Users\HP\Desktop\Matrix\Sparse-Matrix\sample_inputs\sample_input_02.txt'

    matrix1 = SparseMatrix.from_file(input_file1)
    matrix2 = SparseMatrix.from_file(input_file2)

    # Debug statements to check matrix dimensions and data
    print(f"Matrix 1 dimensions: {matrix1.rows}x{matrix1.cols}")
    print(f"Matrix 1 data: {matrix1.data}")
    print(f"Matrix 2 dimensions: {matrix2.rows}x{matrix2.cols}")
    print(f"Matrix 2 data: {matrix2.data}")

    if operation == 'add':
        result = matrix1.add(matrix2)
    elif operation == 'subtract':
        result = matrix1.subtract(matrix2)
    elif operation == 'multiply':
        result = matrix1.multiply(matrix2)
    else:
        print("Invalid operation")
        return

    output_file = rf'C:\Users\HP\Desktop\Matrix\Sparse-Matrix\sample_results\sample_results_{operation}.txt'
    result.to_file(output_file)
    print(f"Result written to {output_file}")

if __name__ == "__main__":
    main()
