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




