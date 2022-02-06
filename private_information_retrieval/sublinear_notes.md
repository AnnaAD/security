## Introduction
- PIR small communication requirements -> large computation req
- n-bit database must incur Ω(n) total server-side work
- to decrease server-side work, increase the required server storage by potentially large polynomial factors

### 1.1 - A new approach: Offline/online PIR with sublinear online time
- linear-time server-side computation into a query-independent offline phase
- offline phase - the client fetches a one-time-use “hint” from the database servers
- online phase - client sends request _do they use the hint to make the query in some way?_
- goals:
  - run in online time sublinear in the database size
  - do not increase the storage requirements at the servers

assumptions:
- one-way functions in the two-server setting 
- linearly homomorphic encryption in the single-server setting—and are concretely efficient
- bottleneck: servers must perform an amount of offline computation in that is linear in the database size

- heavy computation in advance
- process series of queries in sublinear online time (reusing the hint)

### Our results

two server pir
- interact with first server in O(n) offline time, second server in O(sqrt(n)) online time

two server pir with sublinear total amortized time
- making q queries in series O(n/q + sqrt(n)) total computation cost (online and offline)

single server pir
- using linear homomorphic encryption
- O(n^2/3) total communications
- neither the client nor the server performs any public-key cryptographic operations in the online phase
- does not have multiple query feature per offline phase

lower bound
- C*T >= Omega(n)
- C bits of communication
- T bits of database probed 
- optimal in term of communication and online time

### Limitations
- more total communication
- subpolynomial in other schemes, sqrt(n) in this scheme
- This limitation inherent to PIR schemes that have sublinear online server time and where servers store the database in unmodified form
- ammortize the sqrt(n) offline communication

### Related Work
- store database in encoded form, PIR with pre-processing to allow for sublinear server time
  - doubly efficient PIR scheme
  - designated client -> encode the database with secret key _so the client must send the encoded database over to start? database does not have key?/decryption abilities?_
  - encoding can be large
  - public-key analogue
- private anonymous data access (“PANDA”) 
  - respond in sublinear time
  - mutable database
  - require storage proportional to malicious clients (possibly unbounded)
- pre-processing = polylogarithmic total com- munication and total work
  - necessarily increase the storage costs at the servers, by large polynomial factors in many cases
- paper's scheme:
  -servers store the database  in unencoded form and keep no additional state
  - the client and servers must run the linear-server-time offline phase once per client or once per query

Use linear additional storage per query.
- client sends query in offline phase
  - use this request to generate a one-time-use n-bit encoding of the n-bit database
- online phase use precomputation to respond in sublinear online time
- polylog(n) online time
- each client, the servers must store n additional bits until that client makes its online query O(mn) storage queries per user  

Use linear online time
- “privately constrained PRFs” (pseudorandom func) = two-server online/offline scheme, only one of the servers needs to be active in the online phase
  - polylog communication, online server’s work is linear in the database size.
- private stateful information retrieval.
  - single server offline phase, linear number of bits downloaded
  - online phase linear computations required (not sublinear)
- sharding database -> linear still

Marginally sublinear online time.
- two server PIR with slightly sublinear communication
- encode database as branching program, server homomorphically evaluates the branching program in O(n/log(n))
  - running time is dominated by the public key operations

Amortize work
- batching queries
- but can still make some queries one at a time (adaptively?) or only all at once (non-adaptively)

Relax the security property. 
- differential privacy with some leakage of the query

### 1.5 Technical overview

O(n) online phase, O(n) communication

A toy protocol - _implement this?_

Offline phase: before client decides which byte they want to read
- client divides the database indices into sqrt(n) disjoint sets of size sqrt(n) and sends to server. (would be large to send O(nlogn) explicitly) 
  - -> _can you send a seed to PRF or something to have server recalc these sets themself?_
- server recieves, computes parity bits of the database at the indices of each set
- client stores the parity bits

Online phase: once client has decided on the index
- find the set that contains the index i, S_j, remove an item from the set randomly, probability of 1 - (sqrt(n) - 1)/n that they chose i
- send set with i* removed to second server, recieve parity O(sqrt(n)) time
- x_i* = x_i∗ <- h_j − a mod 2. Finds x_i with probability 1 − O(1/√n).

seconds server set sent without i* is uniformly random subset of n of size sqrt(n) - 1. 
- _intuitively, the fraction at which we choose to remove i, adjusted because we know that it was the set that it was included in?_

downsides:
- offline phase is super-linear
- O(nlogn) bits of client storage between online and offline (the parity bits)

solution: derandomize client
- single set of sqrt(n) shifts
- client and server use sets to calculate the sqrt(n) sets
  - slightly increased chance of failure -> i might not be in any set
  - repeat protocol O(log(n)) times though
 
Improvements
- assumptions that one-way functions exist, we can reduce the online-phase communication to poly(λ, log n)
  - puncturable pseudorandom set
  - send over a set in the form of a short-key k
  - puncturable in the sense can produce ki∗ that is a compressed representation of S XOR {i∗}
  - keys: O(λ log n) for sets of size sqrt(n)
- Refreshing the client’s state.
  - refreshes its state by asking the first server for the parity of a random size-(√n − 1), knowing x_i, add x_i to that set, and compute parity manually
  - _second server now has up to date parities for all?_ 
  - puncturable pseudorandom sets the client can send to the offline server all of them using only O(sqrt(n)) bits of communication.
- two servers to one server with homomorphic encryption on the query


## Puncturable Pseudorandom Sets

- puncturable PRF
- allow removal of items from set, use PRF to represent a set with a short key.

### Definitions
- gen, punc, eval
- efficiency, correctness, security
