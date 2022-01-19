## Chapter 4 - Access Control
_maybe can use this for my idea on ingrained access control for databases that hold users and user-data_

### 4.1 Introduction
- applicationlevel, middleware (database access), os, hardware
- protection goal, security policy
- preventing programs from interfereing
- virtualization
- running code with admin priveledges or not

### 4.2 Operating System Access Controls
- read, write, execute
- access triples, for a user, program, file combo
- groups, roles to compress size (if every user has a unique role for every application -> size blowup)

#### 4.2.1 Groups and Roles
- small number of groups or roles
- group is a list of principals, role is a fixed set of permissions principals assume
- os supports this
- role based access control RBAC

#### 4.2.2 Access Control Lists
- ACL, for some data, access control for each user in col
- used in unix
- protection data oriented, less number of users
- simpler to implement
- system wide checks taxing

#### 4.2.3 Unix OS security
- rwx tags
- userid leads os to make access control choice, root = all permissions good
- sys admin can do anything, can remove trace too
- apped only files
- triple access harder since not program based
- set user id file attribute to give access
- suid root leads to security holes
- programmers often give too much priveledge to code

#### 4.2.4 Apple's OS/X
- freeBSD based
- memory protection unless advanced permissions
- force quit apps
- any user can install, if user is in group that can su to root

#### 4.2.5 Windows - Basic Architecture
- take ownership, change permissions, delete
- same effect as suid
- access flags
- richer syntax
- partition user domains
- "everyone" is a principal

#### 4.2.6 Capabilities
- rows - for each user what that user's access to files is
- opposite acl
- efficiently checking run time security based on user
- file status changing is more tricky though
- capablities in public key certs
- managing capabilities is important

#### 4.2.7 Windows - Added Features
- users can be whitelisted or blacklisted
- security policy set by group not system
- groups are main method of control
- kerberos to auth users across networks
- TLS used on applications for web
- user accoutn control replaces default admin priviledge
- low integrity processes shouldnt modify high integrity data
- problem is apps running as root
- vista was complicated and kinda weird but has lots of features

#### 4.2.8 Middleware
- bookkeeping on top of database software
- _this might be what my idea would be classified as_

##### 4.2.8.1 Database Access Controls
- oracle, db2, mysql have own access control mechs
- products let users bypass os controls
- loopholes for sql injections
- david litchfield

##### 4.2.8.2 General Middleware Issues
- granularity, files = smallest object for access control
- state rules hard to manage with transactions
- level across machine, network, appllication hard to keep constant
- ease of admin = bottleneck, in terms of managing ppl

##### 4.2.8.3 ORBs and Policy Languages
- object request brokers, abstraction mediates object communication
- languages to express security protocol
- using access control language might be too cumbersome instead of just working with language you are familiar with
- composition of larger systems is tricky
- users fail to write secure code

#### 4.2.9 Sandboxing and Proof-Carrying Code
- sandbox is restricted env to run untrusted code (ie on jvm)
- proof carrying code, prooves that the code doesn't do anything unexpected, interpreter checks it, less overhead

#### 4.2.10 Virtualization
- single machine emulates many
- host multiple machines
- sharing data between these? how to maintain separation

#### 4.2.11 Trusted Computing
- software and hardware tools to check that running program is identifiable version, not patched, on PC configuration
- trusted platform module hardware chip with crypto keys
- digital content prevent piracy
- difficulty in maintaining backwards compatibility
- tpm can store root keys

### 4.3 Hardware Protection
- protection problem - prevent interference
- confinement problem - prevent programs unauthorized communication
- or protect just metadata
- confinement -> maybe only release confined queries about data
- segment addressing (point to segment and then point within), reference monitor
- acces control implemented on top
- rings of protection
- interfacing with hardware with permissions

#### 4.3.1 Intel Processors and Trusted Computing
- segment addressing and rings
- procedures can't access lower level rings, but gates execute lower
- processor serial number for big brother monitoring (tpm instead)
- complex interactions with virtualization?

#### 4.3.2 ARM Processors
- arm chips used for crypto often (fast add and multiply op)
- processor core can use on chip
- no memory itself
- hardware register locking?

#### 4.3.3 Security Processors
- secalist crypto devices
- 8 bit smart card processors
- application level access control on cards

### 4.4 What Goes Wrong
- bugs
- zero day exploit - first day known is attacked
- os bugs can transition from user to root, just need to know a way in
- compromise large number of pc for botnet, rootkit

#### 4.4.1 Smashing the Stack
- computer emergency repose team (cert)
- pass in size of args that is too big and then overwrite data
- landing pad, nop operation commands, catch processor if executed deliver processor to attack code
- widespread but still existing for years

#### 4.4.2 Other Technical Attacks
- stack overflow -> type saftey failure, exe as machine code
- format string vulnerbility, print user supplied info, can write to stack
- sql insertion
- integer manipulation attack, overflow or underflow
- race conditions, overwrite userid, allow for user to act as another
- user to root problems
- denial of service attacks, syn flooding attacks
- system call wrappers

#### 4.4.3 User Interface Failures
- trojan horse, program that looks like user interface but is malicious


#### 4.4.4 Why so Many Things Go Wrong
- large stystems are buggy
- kernel bloat -> lots of trusted code
- application devs run their programs as root
- applications with too many priviledges
- 

#### 4.4.5 Remedies
- automatic tools, compiler patch for stack overflow
- effort in design coding and testing
- clean interfaces
- default, easiest, way is safe

#### 4.4.6 Environmental Creep
- unix designed as single user multics then expanded for many people on one machine
- unix had protection mechnisms extended
- internet is growing off smaller code-> creep
- mixing components -> less secure, more complex, buggy
- easy to attack with accessible attack resources from others

### 4.5 Summary
- op at mult levels
- hgiher levels are expensive
- access control limits damange
- import part of smartcard and enc devices
- read write execute permissions
- distributed systems

### Research Problems
- engineer robust and usable access control mechanisms
- walling off data not always usable
- combine access control with admission control
- policy languages complex systems
