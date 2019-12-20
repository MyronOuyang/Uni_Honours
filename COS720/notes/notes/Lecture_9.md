# Lecture 9
## Key Points 
----------------------------------------------------
- P2P Network Security
- DropBox Security
- Chapter 17 (pg 686 - 687)
## Read
----------------------------------------------------
- Take a look at the table in the textbook
- Read paper (**No need to know history**)
    - pg 5
    - Ignore bitcoin
## Summary
----------------------------------------------------
-**P2P Network Security**
> Nodes - client fulfills role of server
> There is no Central control
  - Understand Client Server
    - One high performance computer and low performance nodes connected
    - Server recognises communications from clients (protocols)
  - Benefits
    - Shared resources
    - Different architectures/ topologies
      - Pure 2 pure
        - No central control
        - Social, mimics human social communications
      - Hybrid
        - Combination of Client server and p2p, has super nodes and **Serious vulnerability**
    - Highly decentralized
  - Security Issues
    - High disclosure of information
    - Spread of malware
      - Ease of download and upload
    - Leachers
      - Affects availability of resource
      - Person who just downloads and doesnt upload / contribute back
    - DDoS attack (worse on a Client Server)
  - Discuss main countermeasures for security issues
    - **Read research paper**
    - Encrypt traffic
    - Use Encryption to minimize leachers
      - Seeders generate keys for pieces of data
    - Legal
    - Access control
    - Memory and firmware segmentation
    - Code hygiene
- **Drop Box**
> Discussion on Security Risks
  - Client server
  - Data theft
    - Sync of employees devices
    - Where is it stored? You don't know
  - Data loss
    - You've got no control over the sync process
    - You cannot control spread of information
  - No real backup strategy/ tools
  - Large attack surface
  - No private encryption
  - File Sharing
  - Device Sync
  - Encryption
    - AES 256
  - P2P patent **Read**
    - Direct private communication