# Private Information Retrieval

## Project Idea

Implement basic PIR with homomorphic encryption
- use https://github.com/ibarrond/Pyfhel library
- have a basic matrix representing the data
- have a client.py file
- have a server.py file which contains the matrix data
- have the client.py file construct a request with the encrypted bitmask array
- have the server perform the operation and extract the row -> returning the data
- needs to have matrix multiplication -> 1xn column select matrix X nxn data matrix -> 1xN selected column...
  - with just vector by vector -> still sending over n items
  - why can't preform then the 1xn x nx1 matrix multiplication to get one item -> still encrypted but only send one item?
  - if n is big wouldn't it be worth it? esp. if operations don't need fast retrieval?
