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



array1 = np.array([[1,2],[3,4]])
array2 = np.array([[1,2],[3,4]])
array3 = np.array([[1,2],[3,4]])


enc = lambda x: HE.encryptInt(x)

enc_vec = np.vectorize(enc)
a1 = enc_vec(array1)
a2 = enc_vec(array2)
a3 = enc_vec(array3)


ctxtA1A2 = np.matmul(a1, a2)         # `ctxt1 *= ctxt2` for quicker inplace operation

#relinKeySize=5
#HE.relinKeyGen(bitCount=1, size=relinKeySize)
#print("   We can now relinearize!")
#assert relinKeySize >= ctxtA1A2.size

#ctxtA1A2 = ~ ctxtA1A2 # Equivalent to HE.relinearize(ctxtMul)
                      # and equivalent to  ~ctxtMul1 (without assignment)
                      
ctxtOutput = np.matmul(ctxtA1A2, a3)

dec = lambda x: HE.decryptInt(x)
dec_vec = np.vectorize(dec)

print("a3 matrix: expected == ", array3, "actual === ", dec_vec(a3))
print("a1 X a2 ==  ", dec_vec(ctxtA1A2))
print(" (a1 X a2) X a3 === ", dec_vec(ctxtOutput))
print("manual calculation [dec(a1 X a2 ) X dec(a3)] === ", np.matmul(dec_vec(ctxtA1A2), dec_vec(a3)))


print("-----------------------")

print(dec_vec(np.matmul(ctxtA1A2, array3)))
