## Chapter 3 - Protocols
- security protocols as foundation

### 3.1 Introduction
- protocols work in large complex systems -> flaws lead to security problems
- magnetic strip banking cards

### 3.2 Password Eavesdropping Risks
- intercept passwords/replay attacks for car door openers
- RFID/barcodes etc. are easy to impersonate 

### 3.3 Who Goes There - Simple Authentication
- authentication device protocol, encrypts serial with secret key. 
- also using a nonce, number used once (no replays)
  - nonce ensures freshness
- key management each token key is encrypted under global key to be retrievied
  - key diversification
- valet attack = replay attack with a low number of randomness on nonces
- accessory control for ink on printers for example

#### 3.3.1 Challenge and Response
- car key responds by encrypting a value sent as a challenge
- difficulty in generating randomness for the actual challenge
- two factor authentication
  - server responds with last seven digits of encrypted pass from source 1, enter that to source 2 and server can re-verify
  - also use nonce

#### 3.3.2 THe MIG-in-the-Middle Attack
- telling apart friend and foe planes (IFF)
- crptographic protection
- attack: relay the challenge to another plane of the enemy's -> pass by unattacked
- man in the middle attack
- often possible but not economic

#### 3.3.3 Reflection Attacks
- "reflection attack": use own challenge back at the enemy asking for it
  - prevent it by requiring the challenged plane to repond by encrypting it's name and the nonce, or something similar that would be unique per plane
- problem: IFF transmitter, too loud, too great range

### 3.4 Manipulating the Message
- delayed data tranfer -> log keys sent out by paid for key system, decoder uses same keys, publish/leak these keys
- attacker manipulating message contents, not observing others, leading to attacks
- replaying command requests for example

### 3.5 Changing the Environment
- chaning env of protocol leads to vulnerabilities
- diff. sec assumptions

### 3.6 Chosen Protocol Attacks
- given target protocol, cam design a new protocol to attack it if users can be tricked into using a same token or key with the attacking protocol
- mafia in the middle attack
- trusted hardware solution with this being the only app

### 3.7 Managing Encryption Keys
- protocols used

#### 3.7.1 Basic Key Management
- authenticating a key with a trusted third party (i.e alice asks trusted sam for bob's key)

#### 3.7.2 The Needham-Schroeder Protocol
- key distributuion using trusted third party to provide an encrpyted message with key to pass along
- problems with asserting key freshness -> if you wait for a long time after contacting trusted party to send along
- enemys can be users of the system = flaw

#### 3.7.3 Kerberos
- derived from needham schroeder
- authentication service (gives key to interact with ticket server) and ticket granting server (manage access to resources)
- ticket sent to server to souce b, sendt back is a key encrpted for source b.
- added timestamps to needham
- clocks can get out of sync
- send back timestamps to verify

#### 3.7.4 Practical Key Management
- atms have key of the day chosen and managed
- long term private and public keys
- process security module hardware
- master keys to retrieve more keys encrypted and saved

### 3.8 Getting Formal
- verifying correctness -> over time logic of belief
- random oracle model in crypto s an assumption then can verify

#### 3.8.1 A typical Smartcard Banking Protocol
- copac
- customer and retailer share key
- send encrypted message to retailer, retailer can confirm and send back info, customer can send check to retailer with nonces along the way

#### 3.8.2 The BAN Logic
- message meaning rule, if A sees message enc with k and k communicartes with B, A believes B once said message
- nonce verification rule, if message is fresh and principal said it, principal believes it
- jurisdiction rule, if principle believes something and it authority, should be believed

#### 3.8.3 Verifying the Payment Protocol
- verifies the smartcard protocol using statements about enc and freshness

#### 3.8.4 Limitations of Formal Verificiation
- based on external assumptions, outside factors not detected
- idealization
- are all mechanisms of proitocol included
- protocol robustness based on technicalities

### 3.9 Summary
- passwords are a part of security ptocols
- a series of steps to extablish trust
- middleperson attacks, modificiation attacks, reflection attacks, replay attacks

### Research Problems
- formal proof methods
- specification without overrestraint
- unsolved as new protocols are developed
- web implementations, custom apis


