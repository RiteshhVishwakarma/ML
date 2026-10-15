import numpy as np

# =============================================================================
#  NUMPY CHEATSHEET — Most Important & Commonly Used
# =============================================================================


# -----------------------------------------------------------------------------
# 0. WHY NUMPY? — Python List vs NumPy Array
# -----------------------------------------------------------------------------
#
#  Python List                          NumPy Array
#  ─────────────────────────────────    ──────────────────────────────────────
#  Can store mixed types                Homogeneous — all elements same type
#  Slower (Python interpreter)          Faster — optimized in C under the hood
#  Scattered memory locations           Continuous memory blocks (cache friendly)
#  More memory usage                    Less memory — optimized storage
#  No built-in math functions           Built-in mathematical functions
#  No vectorized ops (need loops)       Supports direct vectorized operations
#
#  Example:
#  py_list = [1, 2, 3]
#  py_list * 2  →  [1, 2, 3, 1, 2, 3]   (repeats the list)
#
#  np_arr = np.array([1, 2, 3])
#  np_arr * 2  →  [2, 4, 6]             (multiplies each element)
#
#  Memory layout visual:
#  List  →  [*] [*] [*]   each pointer stored at random memory address
#  NumPy →  [1][2][3][4]  all values stored back-to-back in memory (contiguous)
#
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# 1. CREATING ARRAYS
# -----------------------------------------------------------------------------

a = np.array([1, 2, 3])                  # 1D array
b = np.array([[1, 2], [3, 4]])           # 2D array

np.zeros((3, 3))                         # 3x3 matrix of 0s
np.ones((2, 4))                          # 2x4 matrix of 1s
np.full((3, 3), 7)                       # 3x3 matrix filled with 7
np.eye(3)                                # 3x3 identity matrix
np.arange(0, 10, 2)                      # [0, 2, 4, 6, 8]  (start, stop, step)
np.linspace(0, 1, 5)                     # [0, 0.25, 0.5, 0.75, 1.0] — 5 evenly spaced
np.random.rand(3, 3)                     # 3x3 random floats (0 to 1)
np.random.randint(0, 10, (3, 3))         # 3x3 random integers (0 to 9)


# -----------------------------------------------------------------------------
# 2. ARRAY INFO / ATTRIBUTES
# -----------------------------------------------------------------------------

a = np.array([[1, 2, 3], [4, 5, 6]])

a.shape       # (2, 3) — rows x cols
a.ndim        # 2      — number of dimensions
a.size        # 6      — total elements
a.dtype       # dtype('int64') — data type


# -----------------------------------------------------------------------------
# 3. RESHAPING & FLATTENING
# -----------------------------------------------------------------------------

a = np.arange(12)

a.reshape(3, 4)      # reshape to 3 rows, 4 cols (total elements must match)
a.reshape(3, -1)     # -1 means numpy figures out that dimension automatically
a.flatten()          # always returns a copy as 1D
a.ravel()            # returns 1D view (faster, no copy)
a.T                  # transpose — swap rows and cols


# -----------------------------------------------------------------------------
# 4. INDEXING & SLICING
# -----------------------------------------------------------------------------

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

a[0]          # first row  → [1, 2, 3]
a[0][2]       # row 0, col 2 → 3
a[0, 2]       # same, cleaner syntax → 3

a[:, 1]       # all rows, col 1 → [2, 5, 8]
a[1, :]       # row 1, all cols → [4, 5, 6]
a[0:2, 1:3]   # rows 0-1, cols 1-2 → [[2,3],[5,6]]

# Boolean indexing
a[a > 5]      # all elements greater than 5 → [6, 7, 8, 9]


# -----------------------------------------------------------------------------
# 5. MATH OPERATIONS (element-wise)
# -----------------------------------------------------------------------------

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b         # [5, 7, 9]
a - b         # [-3, -3, -3]
a * b         # [4, 10, 18]
a / b         # [0.25, 0.4, 0.5]
a ** 2        # [1, 4, 9]
a + 10        # [11, 12, 13]  — broadcasting scalar


# -----------------------------------------------------------------------------
# 6. AGGREGATE / STATISTICAL FUNCTIONS
# -----------------------------------------------------------------------------

a = np.array([[1, 2, 3],
              [4, 5, 6]])

np.sum(a)           # 21  — sum of all
np.sum(a, axis=0)   # [5, 7, 9]  — column-wise sum
np.sum(a, axis=1)   # [6, 15]    — row-wise sum

np.min(a)           # 1
np.max(a)           # 6
np.mean(a)          # 3.5
np.median(a)        # 3.5
np.std(a)           # standard deviation
np.var(a)           # variance

np.argmin(a)        # index of min element (flattened)
np.argmax(a)        # index of max element (flattened)


# -----------------------------------------------------------------------------
# 7. LINEAR ALGEBRA
# -----------------------------------------------------------------------------

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

np.dot(A, B)          # matrix multiplication (dot product)
A @ B                 # same as np.dot — cleaner syntax (preferred)

np.linalg.det(A)      # determinant
np.linalg.inv(A)      # inverse of matrix
np.linalg.eig(A)      # eigenvalues and eigenvectors


# -----------------------------------------------------------------------------
# 8. STACKING & SPLITTING
# -----------------------------------------------------------------------------

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.hstack([a, b])          # [1, 2, 3, 4, 5, 6] — horizontal stack
np.vstack([a, b])          # [[1,2,3],[4,5,6]]  — vertical stack
np.concatenate([a, b])     # same as hstack for 1D

np.split(a, 3)             # split into 3 equal parts
np.hsplit(a, 3)            # split horizontally
np.vsplit(np.vstack([a,b]), 2)  # split vertically


# -----------------------------------------------------------------------------
# 9. USEFUL UTILITY FUNCTIONS
# -----------------------------------------------------------------------------

np.sort(a)                   # sort ascending
np.argsort(a)                # indices that would sort the array
np.unique(a)                 # unique elements
np.where(a > 2, a, 0)       # if condition true → a, else → 0
np.clip(a, 2, 5)             # clamp values between 2 and 5
np.zeros_like(a)             # zeros with same shape as a
np.ones_like(a)              # ones with same shape as a
np.copy(a)                   # explicit copy of array


# -----------------------------------------------------------------------------
# 10. TYPE CASTING
# -----------------------------------------------------------------------------

a = np.array([1.7, 2.5, 3.9])

a.astype(int)        # [1, 2, 3] — truncates, doesn't round
a.astype(float)      # explicit float
a.astype(str)        # string array


# -----------------------------------------------------------------------------
# QUICK REFERENCE — axis explained
# -----------------------------------------------------------------------------
#
#   axis=0  →  operates DOWN the rows (column-wise)
#   axis=1  →  operates ACROSS the columns (row-wise)
#
#   array:        [[1, 2, 3],
#                  [4, 5, 6]]
#
#   sum(axis=0) → [5, 7, 9]     (each column summed)
#   sum(axis=1) → [6, 15]       (each row summed)
#
# =============================================================================
