CoRobots
========
--------------------------

* POMCP files:
pomcp.py			(basic POMCP classes)
corobots<X>.py			(cooperative robot examples - toy version of Bayesact using Robots)

--------------------------
INSTALL:
- download and install python v2.6 and numpy ***REVISION Dec 2013 -now works with python2.7 
- you also need packages re and itertools, but these come with python2.6 usually
- unzip bayesact.zip and enter the bayesact folder created thusly
- You will also need an affective identity dictionary, an affective behaviour dictionary, and dynamics equations for males and for females.  A default set is included with this distribution (see above).  You can get other ones by downloading the interact software, running the main applet, selecting a database (e.g Indiana2002-04), and then selecting "Import/Export", and click "Show Current Entries", and then cut and paste these into two text files: one for identities "fidentities.dat" and one for behaviours "fbehaviours.dat".  You can get the identities by selecting "view equations" from the main menu in Interact and cutting and pasting into the files tydnamics-male.dat and tdynamics-female.dat.

******
A program wishing to use a POMCP planner will create a POMCP object and then call POMCP_search with a belief state 
  as a set of samples, and itself as the blackBox simulator. The blackBox object then needs to implement the following

The main function to sample from the action space - returns a tuple of (affective,propositonal) actions. Usually does not need to be overloaded, as it just selects from a distribution over actions with mean = ACT default and a variance given by isiga_pomcp.  The propositional actions is selected using get_prop_action. This consults the oracle from state and return an action, can be different on rollouts and possibly using the sample number 
-----
a=oracle(self,state,rollout=False,samplenum=None): 

******
propagate a state forwards on action a returning the new state newsample, a new observation (newobs) and a new reward value (newreward)
------
(newsample, newobs, newreward) = blackBox.propagateSample(state,a):  

*****
The reward function and discount factor
-----
reward(self,state,action=None)
discount_factor:  a real number in (0,1.0) giving the discount


The rest implement methods to compare observations and actions basically

TO DO: 
---------------
- Fix up the null actions - somehow ensure that these have no effect on the client's turn - 
- Experiment with the stochastic turn-taking (this will also impact the first to-do above)
- same for null observations - maybe this should be changed so there is a null value in there somewhere? 
