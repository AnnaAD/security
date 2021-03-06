import random

verbose = False

class Server:

    # data is a list of integers
    def __init__(self, data, name):
        self.data = data[:]
        self.size = len(data)
        self.name = name

    def get_parity(self, S):
        output = 0
        for i in S:
            output ^= self.data[i]
        return output
    
class User:
    def __init__(self):
        self.sets = []
        self.parity = []
        pass

    # assuming N^2 total elements
    def generate_sets(self, N):
        shuffled = list(range(N**2))
        random.shuffle(shuffled)
        output = []
        for i in range(N):
            output.append(shuffled[i*N:(i+1)*N])
        if(verbose):
            print("SETS:", output)
        self.sets = output

    def req_parity(self, server):
        self.parity = []
        for S in self.sets:
            self.parity.append(server.get_parity(S))
        
    def send_req(self, x_i, server):
        if(verbose):
            print("user requesting data at index:", x_i)
        for i in range(len(self.sets)):
            if x_i in self.sets[i]:
                # randomly remove element or randomly keep element
                removed = self.sets[i][:]
                removed.remove(x_i)
                a = server.get_parity(removed)
                h_i = self.parity[i]

                bit = h_i ^ a
                return bit

        print("ERROR")
        return None
                


import argparse

parser = argparse.ArgumentParser(description='Runs a demo of PIR scheme using two servers, basic scheme.')
parser.add_argument('size', metavar='N', type=int, nargs="?", default=1000,
                    help='the dimension of the data to work on, generates N^2 elements')
parser.add_argument('index', metavar = 'i', type = int, nargs = "?", default = 0, help = "index for user to request data at")
parser.add_argument('--verbose', action = "store_true",
                    help='print out more information')

args = parser.parse_args()

test_data = []

verbose = args.verbose
N = args.size

for i in range(N ** 2):
    test_data.append(random.randint(0, 1))

s1 = Server(test_data, "S1")
s2 = Server(test_data, "S2")

if(verbose):
    print("Initiliazing servers on data:", test_data)

user = User()
import time

if(verbose):
    print("\033[91m---------starting offline phase----------\033[0m")
start = time.time()
user.generate_sets(N)
user.req_parity(s1)
diff = time.time() - start
if(verbose):
    print("\033[91m----------offline phase completed in", diff, "secs------------\033[0m")

if(verbose):
    print("\033[91m------------starting online phase-------------\033[0m")
start =	time.time()
output = user.send_req(args.index,s2)
diff = time.time() - start
if(verbose):
    print("\033[91m-----------online phase completed in", diff, "secs-----------\033[0m")

assert output == test_data[args.index]
print("OUTPUT:", output)
