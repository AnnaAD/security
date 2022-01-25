import numpy as np
verbose = False

class Server:

    def __init__(self, size):

        if(verbose):
            print("Initializing server data:")
        
        self.size = size
        arr = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(i+j)
            arr.append(row)

            if(verbose):
                print(row)
            
        self.data_arr = np.array(arr)

    def get_data(self, enc_row, enc_col):
        row = np.matmul(enc_row, self.data_arr)
        return np.matmul(row, enc_col)

    def get_data_row(self, enc_row):
        row = np.matmul(enc_row, self.data_arr)
        return row



from Pyfhel import Pyfhel, PyPtxt, PyPtxt

class Client:

    def __init__(self):
        HE = Pyfhel()                   
        HE.contextGen(p=63)   # Generating context.
        HE.keyGen()
        
        enc = lambda x: HE.encryptInt(x)
        self.enc_vec = np.vectorize(enc)

        dec = lambda x : HE.decryptInt(x)
        self.dec_vec = np.vectorize(dec)        

    def req_row(self, i, size):
        req = [ 0 if j != i else 1 for j in range(size)]
        if(verbose):
            print("generated row req to enc:", req)
        return self.enc_vec(np.array(req))

    def req_col(self, i,size):
        req = [[0] if j != i else [1] for j in range(size)]
        if(verbose):
            print("generated column req to enc:", req)
        return self.enc_vec(np.array(req))

    def make_and_dec_req(self,server, row, col):
        out = server.get_data(self.req_row(row, server.size), self.req_col(col, server.size))
        return self.dec_vec(out)

    def make_and_dec_row_req(self, server, row):
        out = server.get_data_row(self.req_row(row, server.size))
        return self.dec_vec(out)


import argparse

parser = argparse.ArgumentParser(description='Runs a demo of PIR scheme using homomorphic encryption on one server')
parser.add_argument('size', metavar='N', type=int, nargs="?", default=10,
                    help='the dimension of the matrix of data to work on NxN')
parser.add_argument('row', metavar = 'r', type = int, nargs = "?", default = 0, help = "index of row for data request")
parser.add_argument('col', metavar = 'c', type = int, nargs = "?", default = -1, help = "index of column for data request, if none specified entire row is returned")
parser.add_argument('--verbose', action = "store_true",
                    help='print out more information')

args = parser.parse_args()

verbose = args.verbose
size = args.size
server = Server(size)
client = Client()

row = args.row
col = args.col

print("starting request ... ")
if(col != -1):
    print("output:", client.make_and_dec_req(server, row, col))
else:
    print("output:", client.make_and_dec_row_req(server, row))
