# Lecture 5
## Key Points 
----------------------------------------------------
- DDOS
- Firewall scrubbing
- Amplification attack
## Read
----------------------------------------------------
- Chapter 15 
  - **Intrusion Detection Systems** -NB
    - Vulnerability scanning
    - Integrity of files
    - Anomaly detection 
  - Honey pots
  - fig. 15.1
- Paper: *The Evolution of DDoS*
  - Classic DDoS was *Volumetric attack*
  - Problem with *Volumetric attack*, it overwhelms lock tools
  - **Third column, first paragraph**. They will attack you by not using full bandwith to ensure firewall wont take over
  - Firewalls is still predominant tech to counter DDoS
  - pg 19, Second hand DDoS
## Summary
----------------------------------------------------
- **Tyoes of attacks**
  - Non technical attacks
  - Technical attacks
    - DDoS (Distributed Denial of Service Attacks)
    - Malicious Code
    - Sniffing
    - Spoofing
- **DDoS**
    > attacker has access to a number of PC's
  - Syn Flood Attack
    - TCP 
    > Client (attacker) --syn--> server (victim)
    >
    > Client (attacker) <--syn+ack-- server (victim)
    >
    > Client (attacker) --syn--> server (victim)
    >
    > Client (attacker) <--syn+ack-- server (victim)
    >
    > ...repeat until bottle-neck
  - Characteristics of a DDoS attack
    - Percentage of new IP addresses that arrive at your firewall
  - Prevent DDoS attack
    - Firewall
    - High speed line (to ensure line itself doesn't get congested)
    - **Scrubbing**
  - Volumetric Attack
  - Amplification Attack
    - send small chunks between sender and receiver
    - receiver will send large chunks back
    - resulting in bottle neck
    - eg. DNS attack,**Memcached attack** (happens on application layer)
  - **Risk** 
    - Loss of Availablility
  - **Threat**
    - DDoS
      - Volumetric -> *Flooding, resource exhaustion*
      - Amplification 
  - **Vulnerability**
    - DNS servers
    - Server misconfiguration -> *Memcache*
    - Network Vulnerabilities
  - **Risk Reduction/ Countermeasure**
    - IDS/ IPS (Intrusion Detection/ Prevention Systems)
    - **Scrubbing**
    - Redundancy