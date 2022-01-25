## Chapter 6 - Distributed Systems

### 6.1 Introduction
- attacks on distributed systems via concurrency bugs
- scaling up systems leads to naming problems
- large flat namespaces

### 6.2 Concurrency
- concurrent run at same time
- inconsistency, ordering, deadlock, converging to consistent values
- users accidentally or purposefully interfere in concurrent env

#### 6.2.1 Using Old Data Versus Paying to Propagate State
- mkdir vulnerability in unix two phases, process renames object on which it acts, permission changes
- time of check to time of use attacks
- banks and hot credit cards -> longer interactions need online verification to account for changes in hot credit card list
- revoking credit card credentials is difficult
- revocation of web services using cookies with a time to live
- checking creds against db is expensive -> cookies

#### 6.2.2 Locking to Prevent Inconsistent Updates
- lock some data to prevent multiple updates from concurrent users
- callback keep list of changes -> notify list of users (who need for security) when changes occur
- pre-authorization for credit card
- publish register notify robust auth in distributeed
- callback is privacy threat? frequent checks to database for auth

#### 6.2.3 The Order of Updates
- order of deposits and withdrawls could matter if cause overflow one way
- batch transactions per day, apply credits before debits
- real time gross settlement -> network variages could matter
- large pre auth can tie up card
- sometimes order of transactions dont matter as much -> ie passport auths

#### 6.2.4 Deadlock
- waiting for locks in contention
- can happen between companies trading

#### 6.2.5 Non-Convergent State
- atomic transactions -> all or not at all
- consistent -> invaraint perserved
- isolated -> look the same from other transactios, serializable
- durable -> can't be undone
- covergent -> transaction volume tails off, leads to consistent state
- recoverablity vs durability for bad transactions
- conflicts with clearance checks etc.

#### 6.2.6 Secure Time
- cinderella attack -> programs depending on machine clock can be hacked by modifying machine clock time
- denial of service by tampering with clocks
- use lamport time to only care about relative timing between actions
- radio clock in computer
- clock sync protocols to make delay obvious
- network time protocol, clock voting and auth

### 6.3 Fault Tolerance and Failure Recovery
- avaliability and recovering mechanisms most expensive
- then integrity
- then confidentiality
- fault tolerance based on logs and locking -> harder when specifically attack these
- fault causes error leading to failure of unspec behavior
- mean time before failure and mean time to repair

#### 6.3.1 Failure Models
- analysis of threats

##### 6.3.1.1 Byzantine Failure
- maximum number of traitors in an env of n systems 
- hard to say who lied if A -> true, B -> A says false, C can't determine liar
- n >= 3t+1 
- digital signatures and MAC used

##### 6.3.1.2 Interaction with Fault Tolerance
- redundancy
- fail stop processors = error correction info along with data and stop if failed
- make system resilient
- fail stop leads to DoS
- redudancy can lessen confidentiality if any source of data is compromised
- how users deal with fail safe redudancy is more important

#### 6.3.2 What is Resilience For?
- increased trustowrthy-ness
- proactive security -> keys flushed regardless of reported attack
- how many unreliable clients in protocol
- security renewability

#### 6.3.3 At What Level is the Redudancy
- reduandancy at hardware level (RAID), redudant arrays of inexpensive disks
- process group redundancy -> running many copies of process
- backup of data or system
- fallback of system, less capable, process reverts

#### 6.3.4 Serive-Denial Attacks
- fault tolerance combats these attacks
- tcp/ip vulnerable to these attacks
- ddos distributed attack with botnet, hard to block
- smart card dos to get magnetic strip card to write details

### 6.4 Naming
- naming in distributed systems, security problem in terms of permissions,etc.
- larger, flatter namespaces

#### 6.4.1 The Distributed Systems View of Naming
- bind names to address -> rendexvous, exporting the names
- function of names facilitate sharing
- the naming info is not all in smae okace, resolve name is distributed
- can't assume fixed number of names needed
- global names are less powerful than you think
- names imply commitments, organizational changes
- names can have access tickets or capabilities
- incorrect names being obvious is simpler
- consistency is hard, naming consistency can cause trouble
- phone numbers are more robust than comp. addresses
- some names are bound early, don't bind early if possible

#### 6.4.2 What Else Goes Wrong
- naming in web based world is not from ground-up

##### 6.4.2.1 Naming and Identity
- principals can have amny names
- identity, two names are same principal (inditect name, symbolic link)
  - check fraud is identity failure
- pre-issue fraud, bad person gets identity before desired person

##### 6.4.2.2 Cultural Assumptions
- cultural differences in how we identify people in diff. governments with diff. name formats

##### 6.4.2.3 Semantic Content of Names
- changing what type of name a system uses can cause problems

##### 6.4.2.4 Uniqueness of Names
- human names are often not unique
- assigning numbers to things is not inherintely correct

##### 6.4.2.5 Stability of Names and Addresses
- names have addresses, addresses change
- ip change
- different orgs -> diff names
- pseudonyms online

##### 6.4.2.6 Adding Social Context to Naming
- facebook human and scaleable way to naming
- using network and connection to add context to naming?
  - _could this be applied generally? with duplicate names, usually the one with more connections is the trusted, intended target?_ 

##### 6.4.2.7 Restrictions on the Use of Names
- ssn only used in restricted ways
- law and policy about data collection or harvesting web urls, etc.

#### 6.4.3 Types of Names
- principal in role, delelgation, conjuction as rules
- names apply to services

### 6.5 Summary
- desginers not understanding distributed design leads to security problems
- fault tolerance and recovering
- naming doing too much

### Research  Problems
- communications protocol and OS
- design secure time protocols and naming
- resilience vs convergence and protection













