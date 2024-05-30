
# Sparse Matrix Operations

This project provides a Python implementation for performing operations on sparse matrices. It supports addition, subtraction, and multiplication of sparse matrices, and reading from and writing to files.

## Features

- **Sparse Matrix Representation**: Efficiently stores non-zero elements of a matrix.
- **Matrix Operations**: Supports addition, subtraction, and multiplication.
- **File I/O**: Reads matrix data from files and writes results to files.

## File Format

Matrix data is stored in text files with the following format:

rows=<number_of_rows>
cols=<number_of_columns>
(row, col, value)
(row, col, value)
...

makefile


Example:
rows=3
cols=3
(0, 0, 1)
(0, 2, 2)
(1, 1, 3)
(2, 0, 4)

perl
Copy code

## Usage

### Command Line

Run the script with the desired operation (`add`, `subtract`, `multiply`):

```sh
python Matrix.py <operation>
Example
Ensure the input files are correctly formatted and placed in the specified directory:

sample_input_01.txt (matrix1):

scss
Copy code
rows=2
cols=3
(0, 0, 1)
(0, 1, 2)
(1, 0, 3)
(1, 2, 4)
sample_input_02.txt (matrix2):

scss
Copy code
rows=3
cols=2
(0, 0, 5)
(1, 1, 6)
(2, 0, 7)
(2, 1, 8)
Run the script:

sh
python Matrix.py multiply
Output:
The result will be written to the output file, e.g., sample_results_multiply.txt.

##Code Overview
SparseMatrix Class
__init__(self, rows=0, cols=0): Initializes a sparse matrix.
from_file(file_path): Creates a sparse matrix from a file.
set_element(self, row, col, value): Sets an element in the matrix.
get_element(self, row, col): Gets an element from the matrix.
add(self, other): Adds two sparse matrices.
subtract(self, other): Subtracts one sparse matrix from another.
multiply(self, other): Multiplies two sparse matrices.
to_file(self, file_path): Writes the sparse matrix to a file.
##Main Function
main(): Handles command-line arguments and performs the specified matrix operation.
##Debugging
Debug statements are included to print matrix dimensions and data before performing operations.

##Directories
Input Directory: C:\Users\HP\Desktop\Matrix\Sparse-Matrix\sample_inputs
Output Directory: C:\Users\HP\Desktop\Matrix\Sparse-Matrix\sample_results
##Dependencies
Python 3.x
##Contact
For any questions or issues, please contact [k.thiak@alustudent.com].

##typescript

This `README.md` file provides an overview of the project, instructions for usage, and details about the implementation. Adjust the paths, email, and any other specific details as necessary.





