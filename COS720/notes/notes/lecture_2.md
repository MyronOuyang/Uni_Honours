# Lecture 2
## Key Points 
----------------------------------------------------
- BEC "Think like a security expert"
  - Business Email Compromise
- Impersonation
- Chap 12 - **Study whole chapter**
  - MIM - *Man In the Middle Attack*
  - Crypto Solution
  - DNS spoofing
  - Routers
## Read
----------------------------------------------------
- BEC
  - www.infosecurity.com
  - www.itweb.co.za
    - 20 June 2017
    - asdfasf
    - asdasdfsadf
      - asdfasdfsdaf
- Mirai attack
- NIST - **Just know about it**
  - Secure Inter Domain Routing
## Summary
----------------------------------------------------
- BEC
    - > Accountant in a large company received an email from the CFO (who was on leave at that time). The email from the CFO indicated that a lawyer will contact the accountant to transfer (EFT) a large sum of money. Email had letterhead and signature of the CFO. The CFO contacted the accountant and was informed that she is busy with the transfer of course. The CFO did not know anything regarding the transfer.
    - **Risk** - BEC compromise
    - **Threat** - Scammer (Orgranised crime syndicate), malaware
    - **Vulnerability** - No identification/ authentication checks. Large Organisation
    - **Countermeasure** - 2 Level authentication check (OTP), Behaviour of staff (Call CFO to verify)
- Impersonation
  - Construct impersonation attack
    - Go to website and view *about* page 
    - Go to social networks (eg: FB, LinkedIn, Twitter)
  - Create credibility
    - Learn writing style, to impersonate
    - Speak to the right people
  - Choose an attack
    - Impersonation
- MIM
  - *Access point spoofing, **Browser MIM are common**, Wireless access protocol MIM attack, WPA2 exploit, routers*
  - Digital Signatures
	1. Key generation (Asynchronous key generation): Each person has private and public key. Not reversible, can't derive either key from each other.
	2. Signing: Adding some form of certificate to message to prove authenticity. Use Private key. 
	3. Verification: Receiver will have a message they will want to verify. They will use Public key.
  - Stream cipher - ecnrypt char by char
  - Block cipher - encrypt block of data, different transforamtion/ transferring
  - DNS Spoofing
    - DNS: Domain lookup facility, provide IP of web address
    - Mislead client by intercepting response and providng a fake address 
  - Routers
    - Mirai attack - *Reading*
      - Attacked CCTV cameras in the world. Also attacked Routers whos config was not changed
      - **Threat** - Universal Plug and Play (UPnP)   
