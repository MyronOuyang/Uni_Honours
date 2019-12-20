# Lecture 7
## Key Points 
----------------------------------------------------
- TensorFlow uses Differential privacy
  - Secure Computation Method (SCM)
  - Attempts to guarranty that data isnt encoded during processing.
- Privacy Preserving Data Mining (PPDM)
  - No disclosure of private data
  - **Discuss** how Privacy is Inversely proportional to utility
  - Rampart
    - Anonymization
      - From moment of data collections up to data mining
      - > Eg: Data preparation
        - No identifiers
        - No Quasi Identifiers
        - No Sensititve Attributes
        - No Non-Sensititve Attributes
      - Techniques
        - Generalization
          - > Eg: Instead of specfic age use range of ages
        - Suppression
          - removing informatiom
      - How effective is the anonymization you're doing?
        - > k-anonymity
          - > records needs to be indistinquishable from each other
    - Reconstruction
      - Generate new data set
      - Inverse Frequent Mining Set
    - Modification
      - Association rules
        - Apriori (AI how to detect hidden rules)
        - > Reference to 2007 Apple Patent in Research pape: Pollution of Electronic Profile
    - Provenance
      - Chronology of an object
        - As the object travels over the internet, every time it gets appended with a new ID
    - Trade
      - Data is a commodity
      - Privacy Auction Models
    - Agreement
      - Agreement between stakeholders and user
    - Restriction
      - Law, GDPR, Poppy act
## Read
----------------------------------------------------
- Read paper
## Summary
----------------------------------------------------
 