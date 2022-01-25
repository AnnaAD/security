from Pyfhel import Pyfhel, PyPtxt, PyCtxt

print("==============================================================")
print("===================== Pyfhel ENCRYPTING ======================")
print("==============================================================")


print("1. Creating Context and KeyGen in a Pyfhel Object ")
HE = Pyfhel()                                       # Creating empty Pyfhel object
HE.contextGen(p=65537, m=2048, base=3, flagBatching=True)   # Generating context. 
# The values of p and m are chosen to enable batching (see Demo_Batching_SIMD.py)
HE.keyGen()                                         # Key Generation.

print("2. Encrypting integers with encryptInt")
integer1 = 94
integer2 = -235
ctxt_i1 = HE.encryptInt(integer1)   # Encrypting integer1 in a new PyCtxt with encryptInt
ctxt_i2 = PyCtxt()                  # Empty ciphertexts have no encoding type.
print("    Empty created ctxt_i2: ",   str(ctxt_i2))
HE.encryptInt(integer2, ctxt_i2)    # Encrypting integer2 in an existing PyCtxt
print("    int ",integer1,'-> ctxt_i1 ', str(ctxt_i1))
print("    int ",integer2,'-> ctxt_i2 ', str(ctxt_i2))
