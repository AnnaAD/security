## Chapter 5 - Cryptography

### 5.1 Introduction
- math of security, cross discipline
- designing and breaking ciphers (cryptography vs cryptoanalysis)
- output = ciphertext
- cryptographic primitives: block ciphers, stream ciphers, hash functions
- shared key, secret key, symmetric
- public key or asymmetric 
- digital sig scheme
- random oracle model

### 5.2 Historical Background
- julius casear, sicilian mafia

#### 5.2.1 An Early Stream Cipher - The Vigenere
- adding key repeatedly to plain text and mod 26
- fixed length key matcing messages vs vigenere's repeating key
- long enough plaintext leads to patterns though -> break the key

#### 5.2.2 The One-Time Pad
- key sequence as long as plaintext and never repeat
- perfect secrecy if number of keys is number of plaintexts
- after seeing many messages should not be able to generate ciphertext
- sometimes done in hardware when compute power is low 

#### 5.2.3 An Early Block Cipher - Playfair
- playfair system -> grid of letters, if in same row or col, replace by next letters
- if in corners of a rectangle, replace with other two corners
- digraph letter pairs encrypted instead of single -> harder stats to analyze/attack
- can choose larger block lengths than 2 letters
- small changes to input -> sig change in output
- binding blocks together in good ways to not allow message extension easily, etc.

#### 5.2.4 One Way Functions
- ciphers and code books do not provide authenticity
- added test key (hash value or MAC for auth)
- one way function -> easy to calculate output given input but hard to deduce input from only output

#### 5.2.4 Asymmetric Primitives
- public key published, can decrypt with private key
- problems occur if keys are exposed, hacked, etc.
- digital sigature is also assymteric crypto in reverse, use private key to encrypt, others decrypt and verify with a public key

### 5.3 Random Oracle Model
- pseudorandom if it appears random, statistically, can not guess output, etc. indistinguishable from random
- basis of proofs that the cipher is pseudorandom
- encryption also holds over time, not only communication over distance

#### 5.3.1 Random Functions - Hash Functions
- one way functions = cryptographic hash functions
- compute checksums
- integrity of files
- message digest
- digital signature -> can hash to shorter message first (message digest)
- sending versions of data to be timestamped but want to maintain content secrecy

##### 5.3.1.1 Properties
- given x easy to get h(x). given h(x) difficult to find x. -> one way ness
- output can not give away any property of the input if used in encryption _(this is a looser def than in class, adding enc game to hash)_
- hard to find collisions with long enough outputs

##### 5.3.1.2 The Birthday Theorem
- likely to find a collision between some 2 out of N inputs in sqrt(N) hashes
- in challenge response protocols, collision search attacks aren't a problem --> looking to collide with a specific input not any input (target col resistance?)
- digital signatures need to be collision free though
- pseudorandom function should be collision free

#### 5.3.2 Random Generators - Stream Cipher
- short input long output, generate more randomness
- generate keys
- can replace keys of one time pad
- need to prevent same keystream being used more than once
- seed for the key
- key management details trciky, sych with wrong key

#### 5.3.3 Random Permuations - Block Ciphers
- random permutation
- function is invertable
- if seen before, generate same ciphertext, otherwise get new way to generate ciphertext, pseudorandom permutation
- same output given same input
- known plaintext attack -> attacker given random input/outputs
- chosen plaintext attack -> attacker can request any number of outputs for selected input
- chosen plaintext/ciphertext attack -> can also ask for decryptions
- related key attack
- key recovery attack or forgery attack (encrypting new message)
- DES could be broken with 2^43 known plaintexts
- lunchtime attacker -> temp access to cryptographic equipment
- related-key attacks when block cipher is building block = problem

#### 5.2.4 Public Key Encryption and Tapdoor One-Way Permutations
- public key encrpty = block cipher cna encrpyt with the public key, but only decrypts with the private key
- trapdoor one way permutation -> can only be reversed if known the trapdoor (priv key)
- given public key can't compute private, encrypt func with public key, decrypt with private key

#### 5.3.5 Digital Signatures
- can be randomized or deterministic
- can tell if signed message is from source
- sign with priv key, verify with published public key for that person
- message recovery vs mode that outputs TRUE/FALSE, often don't need message recovery, instead can hash message, sign the hash

### 5.4 Symmetric Crypto Primitives
- how to implement with math -> high level explination

#### 5.4.1 SP-Networks
- combine substution with transposition repeatedly, confusion and diffusion
- sp netowkr ssizteen inputs, two layers of four bit invertible substition boxes (s boxes)
- to be secure needs to be wide enough, have enough rounds, and sutable s boxes

##### 5.4.1.1 Block Size
- need to deal with ciphertexts of 64 _(modern day this is too small lol)_, 128 bits by birthday paradox

##### 5.4.1.2 Number of Rounds
- depends on speed whiuch data diffuses through cipher
- to decrypt should be revertable

##### 5.4.1.3 Choice of S-Boxes
- map input to output -> chosen to be pseudorandom after X rounds

##### 5.4.1.4 Linear Cryptanalysis
- collect number of relations and reach for algebraic relation from input and output with different than guessing probability

##### 5.4.1.5 Differential Cryptanalysis
- oberving with probability given a change of inputs leads to some change in output
- look also for differences that don't occur
- per round information leakage
- more complicated design might be more secure but use more gates or be slower

##### 5.4.1.6 Serpent
- serpent is sp network of 128 bits
- change in input -> avalanche effect on ouput -> linear and differential attacks harder
- 32 s boxes

#### 5.4.2 The Advanced Encryption Standard (AES)
- aes is single s box, byte input to byte output
- lookup in table of 256
- bytewise shufflying and mixing operations (based on Square)
- 10 rounds, 128 bit keys, 12 rounds eith 192 bit keys, 14 rounds with 256
- no proof of security but confidence in practical urposes
- AES likely threatenened with cache miss overvation, timing attacks, etc. to deduce key

#### 5.4.3 Fiestel Ciphers
_similar to the chaining XOR thing that is subseptible to extension attacks? not the same though, just the idea of PRF and XOR combos_
- more complicated block cipher
- round function, split input into two halves
- apply function on one half, combined with XOR to sencond half, apply function, XOR, then swap halves, XOR, etc.
- to decrypt just do functions in reverse
- any one way function used as block cipher

##### 5.4.3.1 The Luby-Rackoff Result
- if the functions are random functions than it is indistinguishable from random
- four rounds good

##### 5.4.3.2 DES
_short key, not used anymore_
- used in banking
- expand blocks
- then xor in key
- basthrough 8 sboxes
- output permuted with fixed pattern
- vulnerable to shortcut attack, linear attack with 2^42 known texts, but key length is more of a problem
- triple DES, nest DES 3 times _in 2016 vulnerability found and it was phased out for AES_
- banking relied on message formats of DES
- composite cipher DESX - key whitening xoring with more keys to increase difficulty of keysearch

### 5.5 Modes of Operation
- specify block cipher can be extended for arbitrary length messages

#### 5.5.1 Electionic Code Book
- using ECB to ecnypt messages of more than one block could lead to cut and splice along block boundaries, doesn't connect the blocks. gen. new messages

#### 5.5.2 Cipher Block Chaining
- xor previous block with current block before exncrption
- however, if opponent knows some plaintext can cut and splice and integrity not gaurenteed

#### 5.5.3 Output Feedback
- repeatedly encrypting val and xoring blocks
- needs to have key expanded to k_i keys
- fail to protect message integrity
- extension attack

#### 5.5.4 Counter Encryption
- feedback modules are hard to parallelize
- generate keystream by encrypting a counter

#### 5.5.5 Cipher Feedback
- stream cipher
- self-syncronizing
- if bits are dropped will resync
- cipher feedback not as useful since silicon is cheap, link layer for synchronization and error correction instead of in crypto

#### 5.5.6 Message Authentication Code
- MAC
- encrypt it using CBC and only use the last
- MAC can depend on all plaintext blocks
- CMAC the key is xored before last encrpytion
- can also use hash function with a key _we discussed this method more in class_

#### 5.5.7 Composite Modes of Operation
- calcualte MAC on message, CBC wth different key
  - using same key means cut and splice attack is possible
- cbc-mac authentication ccm
- galois counter mode gcm parallelisable
  - encryption is performed in counter mode, resulting is multipled with key, 2^128 elements with auth tag, ciphertext same length as plain text
  - universal hash function tag computation
- new mac for any bit of message changed, gcm however computation is proportional to number of bits changed, highly parallelizable
- gcm is common now

### 5.6 Hash Funcitons
- hash function from block ciper
- feed message blocks one at a time, xor and update input, feedforward

#### 5.6.1 Extra Requirements on the Underlying Cipher
- birthday effect, 64 block cipher is not addiquite, 128 bit AES might hust work
- many rounds, 32 bits for its less than ideal s box
- fixed ppint attack, given input can find a key which will leave the input unchanged
  - treyfer sed as hash function can find collision, chosen key attack

#### 5.6.2 Common Hash Functions and Applications
- treyger
- md4
- us secure hash standard
- _i think these are all different now_
- SHA256 SHA512
- certificational threats
- key updating, backware security
- autokeying, share a hash key, agreed on times since last message
- forward security, security can be recovered as soon as compromised machine exchanges with uncomp.

### 5.7 Asymmetric Crypto Primitives
- math for how it works

#### 5.7.1 Cryptography Based On Factoring
- prime number with no divisor
- fundamental theorem of arithmetic -> ever number factors into unqiue primes
- easy to find primes and multiply, hard to factor
- quantum computers make facturing easy?
- fermat's lttle theorem in RSA
- euler's function
- ciphertext = c = m^e mod n
- decrpytion m = eth root of C mod N
- can use fermat's therem to decrypt
- multiplicative homorphism matintained over encryption
- need to use large exponents
- probablilstic encrpytion adds randomness
- semantic security attacker cannot get info about plaintext
- optimal asymmetric encryption passing
- xor with hash of nonce
- can break security by sending messages and observing error messages to deduce info
- padding in poorly implemented standards

#### 5.7.2 Cryptography Based on Discrete Logarithms
- elliptic curbves vs normal case
- primitive root
- discrte log calculations repeatedly (6.042 stuff)

##### 5.7.2.1 Public Key Encryption - Diffie Hellman and ElGamat
- how to establish keys without leaking info
- discrete log used
- g^xA mod P sent to Bob
- g^xAxB mod p sent to Alice. Alice removes her exponentiation and sent back to Bob, Bob removes his
- they both get gbothpublish g^xA and g^xB as public keys
- can use their B^xA and A^xB with public key and decrypt

##### 5.7.2.2 Key Establishment
- session key g^RARB
- they might not know who they share session key with it
- middle person attack
- key exchange with bob pretending to be alice
- sit in middle, translate messages with own key
- sign messages they send to eachother

##### 5.7.2.3 Digitial Signature
-ElGamal sig scheme
- rX + sk = m, g^rX * g^sK = g^m
- p and g need to be chosen well
- use hash to sign arbitrary length
- DSA on 1

#### 5.7.3 Special Purpose Primitives
- threshold crypto mechanism where a signing key is split between n principals
- any k out of n can sign a message _whoa this is really cool!_
- blind signatures making aisnature on a message without knowing the message, give R^eM mod n back to signer to computes the rest, then give back, and divide out R
  - used in digital cash
- use in online elections?

#### 5.7.4 Elliptic Curve Cyptography
- discrete logarithms on elliptic curve
- less computation and shorter variables
- bilinear paring - public key is name
- identity based cryptosystem, central authority issued private key
- global public key
- sign messages
- central authority though would know private key
- identity based primitives only used in specialist systems

#### 5.7.5 Certification
- public keys associated with names
- certification ayuthority to sign public keys
- certification is hard
- abadi and needham, problem with denning and sacco, alice sending a key to bob, bob can masquarade as alice
- subtle middle person attacks
- crypto ignition key, protable electronic device to id security clearance
- getting users to understand implications

#### 5.7.6 Stength of Asymmetric Cryptographic Primitives
- elliptic curves require twice the block length srength as block cipher
- commoner schemes on discrete logs are less robust
- quantum computers threaten integrity of this encryption?

### 5.8 Summary
- random oracle model provides basis of encryption asusmptuons
- blcok ciphers constructed with substitutiona dn permutations
- asymmetric aplpications uses number theorey
- stream ciphers and hash functions can be constructed with block ciuohers
- subtlties and details are where the crypto breaks down

### Research Problems
- designing primitives for encryption, signatures and composite operations which perform reasonably well
- _this could be fun work, optimizing these costly functions in practicality, 6.172 comes to the rescue!_
- trsuted computing
- confrences: crypto, eurocrypt, asiacrypt, CHES, fast software encryption
