# Lecture 10
## Key Points 
----------------------------------------------------
- Main Cloud Security Threats
- Basic things to do to secure data in the cloud
- Reading Paper

## Read
----------------------------------------------------
- Paper: Cloud Security (Exam)
## Summary
----------------------------------------------------
- **Cloud Security Threats** (provide high level discussion on threats)
  - Data leakage/ data bridge
  - Data loss
  - DOS 
    - Shutdown of service
    - Due to network topology/ architecture
    - Account Hijacking
  - Crypto-Jacking
    - Malware that consumes local resources and degrades computing power
  - Insecure API's
  - Insider Threats
  - Biometric hacking
    - Someone gets hold of biometric access data
  - Skimming
    - eg: bank networks
    - go google wtf this is
- **Secure data in cloud environment**
  1. **GOOD PASSWORD POLICY**
     - Use a password manager if you want to reuse passwords
  2. Backups
  3. Encryption before uploading
  4. Common sense
     1. Dont store confidential stuff on the cloud
     2. Be aware of online behaviour
- **Paper: Cloud Operating System**
  - Minimize inter-vm attacks
  - Cloud Architectures
    - IAAS
      - Take a look at the **main** security issues for this one
      - Consists of VM's
      - Physical Nodes (contains vm's)
      - Cluster (groups of nodes)
      - Data Center (groups of clusters)
    - PAAS
    - SAAS
  - Virtual Machines
    - Placement within a cloud infrastructure
      - Look at resource consolidation/ utilization
      - Look at energy efficiency
      - Optimise network traffics (shorten physical distance between nodes that communicate alot)
  - Discuss the *chinese wall model* - **NB!!!!!!!!**
    1. Simple Security Rule
       - Cannot read data from object on higher level, Only nove down 
    2. Star Security Rule
       - Cannot write down, stop info from travelling down
  - CBAC4C
    - S,R,CTL (Security, Risk, Conflict Tolerance Level)
    1. Physical nodes can be shared if its non conflicting
    2. Companies that are in conflict with each other can share physical machine
    3. Companies that are in conflict with each other can run on different node but same cluster
    4. Companies that are in conflict with each other can run on different cluster but same data center