# Private Information Retrieval

## Introduction
Basic idea is to use multiple servers to achieve PIR.

Protocol achieved with two servers (Pudlak and Rodl) -> looking for bit i, send j and l s.t. j + l = i mod n, then perform protocol
- _is this similar to the ideas in key exchange, but where each server sees similar to what the open network sees in key exchange_
  - _then the user/requester can reconstruct the value of their query similar to how each party in key exchange calculates the key_
 
Protocol acheived with k servers and one user.
- _is this similar to the anonymous voting kind of problem, where each user sends some bits, when XOR can get result of the vote, but anonymity of each vote maintained, except in reverse kind of as each XORed thing gets the result of the bit, but sending one can't see what outcome would be_
- user holds "indices" 1 through k (could these be thought of as secrets? keys?)
- servers hold all indices but index j, and a 2^n length bit string in common (a key?)
- each server sends a message back to U, with XOR chain, user can deduce the value for bit x_i.

Instance Hiding -> computing a function f on known input i. Keep i hidden from oracles/server.
- see as having f(1)...f(n) where seeking bit f(i), but not usually directly applicable to information retrieval
- this paper focuses on a feasible size n, and small number of k servers in contrast

Subsequent Work
- k+1 server scheme instead of k
- private information storage
  - oblivious ram
  - multi-round protocol
- computationally bounded servers with one-way functions, O(n^E) two server PIR scheme
- database privacy is protected too, only info revealed is one physical bit, k servers

## Models, Definitions and Discussions
- one round
- randomized strategy -> input index from {1...n} and random input r (with length of security param?)
  - produce k queries Q1(i,r) ... Qn(i,r)
  - reconstruct x_i, with results from queries and r,i
  - privacy requirement = queries are distributed independently of i -> server gains no information about i
  - k answer functions
  - reconstruction function
- correctness = reconstruction function on all answers and i and r leads to x_i
- privacy = probability of query being issued is the same for any arbitrary j as it is for i


perfect privacy - having the probabilities being exactly equal so server gets no information about what was queried for. could be relaxed.

memoryless protocol - history independent user and server, allows for multiple users, concurrency

deterministic server strategies - not useful for user privacy, essential for database privacy though

noncollusion - servers can not collude about the protocol. can collude to update database. in practice could detect this fraud, too risky for a buisness to violate in this way

coalitions - privacy is maintained with collusions of groups of up to t servers

PIR of blocks
- instead of retrieving a bit-> retrieve a block of data
- saves work instead of retrieving a bit at a time

search by keyword
- how to search instead of on identfying index, more realistic 

complexity measures
- number of servers (k)
- communication complexity of the protocols, (n and k)
- computations be in polynomial time
- in this scheme -> servers computation in linear time
- user's actions linear to communication complexity
- communication overhead v privacy for an application
  - for example partition the database (can tell what part was accessed but not what item in a part)
  - computation prop. to portion length

## Single Bit PIR Schemes

linear summation types - user sends sequence of subsets, server responds with XORs of bits

Basic Two Server Scheme - 
- very simple PIR scheme that allows user to privately obtain the bit xi by receiving a single bit from each of two servers
- select random set
  - send set to server 1
  - send set XOR i to server 2
- servers respond with bits of index specified by set.
  - all the XORs cancel out except for the bit i
- server is only sent a single bit back
- user sends \[n\] items though, so not better communication yet


Multi-Server Scheme
- two server scheme is 1d, generalize to multi-d with multiple servers
- 2^d servers queried for xor of a random distribution subcube
- subcubes can be described more succinctly than general subsets -> less user sent communication bits
- n = l^d. each position is a d-dimension tuple. so i = (i_1,...i_d)

protocol:
- user chooses d subsets
- xor each of d subsets with i_d etc. (the elements of the index tuple)
- then these subsets can be paired and sent to servers (i.e. (S_0, S_0 xor i_0). there are 2^d servers (_so pairing covers all? there are 2d items paired... but for each of the d dimensions? d dimensions, each having 2 options (with i or without) so 2*2*2...*2 for each of the d dimensions -> 2^d_)
  - can correspond which subset to send based on the name of server
- server responds with bit that is XOR of all the bits in the subcube sent over
- user XORs all recieved bits (2^d bits from k servers) to get x_i.

correctness: all other bits cancel across subset responses except for indexes corresponding to x_i

privacy: each subset appears random, even when xor with index i, still appears random

communication overhead: sequence of d subsets sent, k*(d\*l+1)
- user sends d * n^(1/d) bits, server responds with n bits


Covering Codes Scheme
- reduces number of participating servers
- d = 3, 8 servers required
- one server can emulate another by sending the 3root(n) possible combos for what the pair server could have responded with in the last coordinate
  - (s_0, s_1, s_2) and (s_0, s_1, s_2 xor j) where j = {1... n} (emulating j = i)
  - can emulate all three servers where it would be XORed in each place
  - other server can emulate ones where one coordiate is also flipped, to cover all 8 possibilities in 2 servers
  - having it emulate two flips too expensive (cube root n)^2.
- _how is it that emulating every possible index actually leaves XORing the correct index?_ 
  - _is it because the other j indexes will be cancelled out by generation where the other server actually has the XOR i in it? that is uncancelled, but other emulations cancel the other indexes?_

- Hamming geometry
  - hamming distance 1
  - covering code C_d = {c_0, ... c_k} for k database protocol for {0,1} ^d
 
Theorem: communcation complexity for k servers with d dimensions = k + (2^d + (d-1) * k) * n^(1/d)   
k<2^d
k >=2^d/(d+1) = radius one ball, volume bound

very good for small k

2 servers: 12 * cuberoot(n) + 2
3 servers: 28 * cuberoot(n) + 4

computation: 
server's computation is linear in n. for emulation: n^(1/d) possible. 
xor by construction is more efficient? n^((d-1)/d) bits examined? 
(d+1) * n computiation 

Generic Transformation: PIR scheme in one round
- consider mxn matrix instead of m * n bits
- send the requests based on the ith and jth bit. independently within the m bits and within the n dimension.
- communication complexity: 2 * (m+n)


## Private Block Retrieval

- to retireve an l bit block, can preform the 1 bit protocol l times.

protocol to get single bit with sum of answers mod 2:
- partition bits into m bits of n-1 bits each. N = m * (n-1)
- bit positions represented by coors in n and m, user sends to server n,1 m times to each server
- each server adds and takes mod 2 for each of the bytes it would have sent for the m invocations 
- gets the single bit back for x_i

- user can send m * a(n) bit requests, and each server responds with l bits (applying homomorphic function to summation)
- _this confuses me... how does this extend the single bit to the many bit block?_

- cases where length of record is longer than number of records achieved (not square table)
- n <= l -> 4l communication complexity
- n <= l^2/4 -> 8l communication complexity

- relalistic sizes for d, fewer servers -> slightly worse complexity, but realalistic

## Lower Bounds

- obvious lower communication bound: log n bits which holds for any number of servers

- single server case
  - n bits must be relayed with one server
  - (information-theoretic) privacy constraint
    - without PIR: log_2(n + 1) bits are enough (user sends i (log_2(n)) and gets back xi). 

Linear Summation Queries with Single Bit Answers
- query needs n - 1 bits to describe a set that looks random, set of all responses from server 2^(n-1) 

## Project Idea

Implement the 2 server basic construction as a proof of concept.

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
  - the user would send 2sqrt(n) bits of communications, the server responds with 1.
    - communication would still be sqrt(n) then... hahaha

- _could you use the idea of d dimensional coordinates with homomorphic encryption to get n^(1/d) communication?_
  - currently since matrix is 2d, we get n^1/2 communication. vectors of size n^1/d for extracting a d-1 dimension slice of the data vector math?
  - I think the server would respond with (d-1) sized data, when d = 2, this means that returned it n^1/2 and user sends n^1/2
  - if sent however k * n^(1/d) sized user data, meaning k of these bit matrix to specify a dimension then the server would also respond with less data.
    - server sends back (d-k) dimension. when k = d-1, sends back n^(1/d).

user has power over database servers in the sense that access control is not possible? 
