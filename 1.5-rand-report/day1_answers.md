## Exercise 1.5.1

1. According to RAND, what distinguishes OC4 from OC5 threat actors?
Answer -
OC4 - O(100) professionals in relevant domains with O($10M) budget and access to state resources such as legal cover, communication infra access etc.

OC5 - O(1000) professionals in relevant domains whose experience is matching or beyond the public SOTA and have O($1B) budget and access to state resources.


2. Which OC level can realistically compromise GPU firmware supply chains?
Answer - OC4

3. How does RAND estimate the cost difference between OC2 and OC5 operations?
Answer - the budget ceiling itself is 100,000x larger for OC5 against OC2

4. Read the attack vector examples in the RAND report and classify each scenario
Answer - 
* Scenario A: Social engineering attack against ML researchers to steal cloud credentials
OC2 - OC3

* Scenario B: Custom hardware implant placed during chip manufacturing
OC5

* Scenario C: Insider threat using legitimate access to copy model checkpoints
OC3

* Scenario D: Advanced persistent threat with multiple zero-day exploits
OC4 - OC5

## Exercise 1.5.2
1. There are 5 environments that RAND identifies in which AI models need protection:
1) model training, 2) research env, 3) internal deployment, 4) public API deployment and 5) on-prem deployment for orgs

2. The need for SL4 is determined by the adversary as per definition the SL4 needs to be able to thward OC4 level attacks. There's no capability level threshold set by RAND for SL4. Other factors that go into a company deciding if it needs SL4 is 1) whether other ways exist for an adversary to access similar model capabilities 2) whether model capabilities pose national security risks etc.

3. SL5. RAND's SL5 benchmark requires that any system containing or accessing the weights has protection equivalent to TS/SCI