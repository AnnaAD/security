### 2.1 Introduction

- phishing, example of using physology as well as tech
- pre-texting, calling under false pretext
- social engineering

### 2.2 Attacks based on psychology
#### 2.2.1 Pretexting
- i.e fake calls from the "IRS"
- can target staff of an organization
- _if phone calls/emails/etc. were properly authenticated then would this be a problem?_

#### 2.2.2 Phishing
- target customers not staff, hard to train against compared to pretexting

### 2.3 Insights from Psychology Research
- users as opposed to technology as the target

#### 2.3.1 What the Brain Does Worse Than the Computer
- HCI - human comp. interaction as a field
- human error when operating tech = security application
- capture error -> humans "auto-pilot", hit OK without thinking
- post completion error -> humans do not tidy up after action
- humans dont understand the security problem
- information overload

#### 2.3.2 Perceptual Bias and Behavioral Economics
- public perception of risk is skewed
- hard for people to accurately assess secuity risks (ie. worry too much about bank fraud)

#### 2.3.3 Different Aspects of Mental Processing
-  explain by intent over situation
-  fundamental attriburtion error
-  affect heuristic -> emotional questions lead to emotional answers

#### 2.3.4 Differences Between People
- gender HCI - women and men nav space diff (but men design systems more) -> bias
- does this have security implications?

#### 2.3.5 Social Psychology
- belonging to groups, obeying authority -> security/fraud implications from impersonating authority
- cognitive dissonance ->.leads to persist in wrong courses of action

#### 2.3.6 What the Brain Does Better Than the Computer
- recognizing humans, image processing
- captchas

### 2.4 Passwords
- managing password -> practical security problem
- large number of people, people choose for many diff. sites -> more pass. problems
- authentication via possessing a device, a piece of info (password), or biomentrics
- password "hardness" (can limit attempts)
- identity fraud (passwords of SSN, maiden name, etc)
- problems: can enter correctly, memorable, dislcosed the password by deception

#### 2.4.1 Difficulties with Reliable Password Entry
- nuclear codes = 12 digits, max length with reliable entry under stress

#### 2.4.2 Difficulties with Remembering the Password
- choose easy to guess, or write them down somewhere else

#### 2.4.3 Naive Password Choice
- people choose bad passwords (v. short, common words, names, etc.)
- gotten longer overtime
- people use same pass everywhere

#### 2.4.4 User Abilities and Training
- training users to make good password choices, have good pass management practices
- mnemonic prgases are good
- user compliance problems
- centrally assigned passwords are hard and disliked

###### 2.4.4.1 Design Errors
- design errors in systems = insecure
- contextual secuirty information relied upon
- mothers maiden name is bad for example
- people use same passwords on other sites
- if done so poorly can loose legal claims too

###### 2.4.4.1 Operational Issues
- i.e. forgetting to reset default passwords

#### 2.4.5 Socail-Engineering Attacks
- getting users/sys admins to accidentally reveal passwords

#### 2.4.6 Trusted Path
- can tell if software you are running is what you expect
- secure attention sequence (ctrl-alt-delete for example)
- skimmers over front of genuine cash machines

#### 2.4.7 Phising Countermeasures

##### 2.4.7.1 Password Manglers
- browser extentions that stengthen passwords

##### 2.4.7.2 Client Certs or Specialist Apps
- client certificate SSL protocol
- server cert ide web sites to browser
- cleint cert used to make auth mutual
- bank provides special banking app to client (expensive and maybe cumbersome)

##### 2.4.7.3 Using Broswer Password Database
- browser as pass. manager
- composimise by malware
- no autocomplete?

##### 2.4.7.4 Soft keyboards
- prevent key logging with on-screen virtual keyboard (but still can be defeated w/ img processing)

##### 2.4.7.5 Customer Education

##### 2.4.7.9 Trusted Computing
- tie transaction to hardware and motherboard
- way for software to ID specific PC (but hard in practice)

##### 2.4.7.10 Fortified Password PRotocols
- encrypted key exchange to shared password

##### 2.4.7.11 Two Channel Authentication
- send acccess code to phone
- usability problems as cost
- requires independence of platforms

#### 2.4.8 Future of Hpising
man in the middle attacks
identity markey
front end widgets

### 2.5 System Issues
- is it possible to restrict number of guesses?
- targeted attacks on one account
- attempt to penetrate any account on a system in geneeral
- attempt to penetrate any account on any system
- sevie denial attack

#### 2.5.1 Can you deny service?
- is it okay to stop user access after many bad pass. attempts?

#### 2.5.2 Protecting Oneself or Others
- protecting legit users of system from eachorher?
- strong sep. of users?

#### 2.5.3 Attacks on Password Entry

##### 2.5.3.1 Interface Design
- possible to witness pin entry?

##### 2.5.3.2 Eaves Droppping
- monitoring free wifi

##### 2.5.3.3 Technical Defeats of Password Retry Counters
- timing attacks on password entry

#### 2.5.4 Attacks on Password Storage
- vulnerable where they are stored

##### 2.5.4.1 One-Way Encrypton
- passwords saved by one way function
- check by re-encrypting and matching
- need random salt to prevent precomputing and checking
- hash of password's hash as cookie -> easy to calculate from a table of password hashes and could be hacked

##### 2.5.4.2 Password Cracking
- dictionary attack
- slow down guessing can help

#### 2.5.5 Absolutie Limits
- total exhaust time for all passwords of specific length
- shadow passwords, encrypted passwords in secret file with obsure encrption and or secret key
- issue random passwords -> protect individuals but not overall all accounts
- botnet for trying many attempts
- counting failed attempts

### 2.6 CAPTCHAs
- slow down machine guessing but people are good at them
- can be integrated into other auth measures
- challenge response protocol

### 2.7 Summary
- usability is hard
- phising is growing threat
- passwords can be guessed or insecurely used
- increasing cost of attack on your specific system

### Research Problems
- captachas
- physchology and security and usablity






