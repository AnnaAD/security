"""
Pyfhel with Numpy and Pickle
==============================
This demo shows how to leverage on the np.ndarray container to perform
encrypted operations over vectors of ciphertexts. We will use pickle
to simulate data tramsnission by serializing it.
"""

import numpy as np

from Pyfhel import Pyfhel, PyPtxt, PyCtxt
# Pyfhel class contains most of the functions.
# PyPtxt is the plaintext class
# PyCtxt is the ciphertext class


print("==============================================================")
print("================ Pyfhel with Numpy and Pickle ================")
print("==============================================================")



HE = Pyfhel()           # Creating empty Pyfhel object
HE.contextGen(p=63, m = 8192)  # Generating context. The value of p is important.
                        #  There are many configurable parameters on this step
                        #  More info in Demo_ContextParameters.py, and
                        #  in the docs of the function (link to docs in README)
HE.keyGen()             # Key Generation.
print(HE)



array1 = np.array([[1,2,3,4,5],
                    [6,7,8,9,10],
                    [11,12,13,14,15],
                    [16,17,18,19,20],
                    [21,22,23,24,25]])
col_select = np.array([[0],[1],[0],[0],[0]])
row_select = np.array([0,1,0,0,0])

enc = lambda x: HE.encryptInt(x)

enc_vec = np.vectorize(enc)
arr_gen = enc_vec(array1)
col_gen = enc_vec(col_select)
row_gen = enc_vec(row_select)

ctxtRow = np.matmul(row_gen, arr_gen)         # `ctxt1 *= ctxt2` for quicker inplace operation
ctxtItem = np.matmul(ctxtRow, col_gen)

dec = lambda x: HE.decryptInt(x)
dec_vec = np.vectorize(dec)

print("row select vector: expected == ", row_select, "actual === ", dec_vec(row_gen))
print(" row extracted ==  ", dec_vec(ctxtRow))
print("item extracted === ", dec_vec(ctxtItem))
print("manual calculation [row X col_select_vec] === ", np.matmul(dec_vec(ctxtRow), dec_vec(col_gen)))
