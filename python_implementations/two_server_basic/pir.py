import random

verbose = False

class Server:

    # data is a list of integers
    def __init__(self, data, name):
        self.data = data[:]
        self.size = len(data)
        self.name = name

    # req is a dictionary mapping indexes to booleans of to include or not
    def make_req(self, req):
        if(verbose):
            print("server", self.name ,"recieved req:", req)
        output = 0
        for i in req:
            if(req[i]):
                output = output ^ self.data[i]
        return output

class User:
    def __init__(self, server1, server2):
        self.server1 = server1
        self.server2 = server2
        self.size = server1.size

        
    def send_req(self, x_i):
        if(verbose):
            print("user requesting data at index:", x_i)
        req = {}
        for i in range(self.size):
            req[i] = random.randint(0,1) == 1

        req2 = req.copy()
        req2[x_i] = not req[x_i]

        res = self.server1.make_req(req)
        res2 = self.server2.make_req(req2)

        return res ^ res2


import argparse

parser = argparse.ArgumentParser(description='Runs a demo of PIR scheme using two servers, basic scheme.')
parser.add_argument('size', metavar='N', type=int, nargs="?", default=1000,
                    help='the number of data elements in data list to work on')
parser.add_argument('index', metavar = 'i', type = int, nargs = "?", default = 0, help = "index for user to request data at")
parser.add_argument('--verbose', action = "store_true",
                    help='print out more information')

args = parser.parse_args()

test_data = []

verbose = args.verbose

for i in range(args.size):
    test_data.append(random.randint(0, 100000))

s1 = Server(test_data, "S1")
s2 = Server(test_data, "S2")

if(verbose):
    print("Initiliazing servers on data:", test_data)

user = User(s1,s2)
print("OUTPUT:", user.send_req(args.index))
