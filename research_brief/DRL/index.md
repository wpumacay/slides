class: center, middle, inverse

# A preliminary study of the applications of Deep Reinforcement Learning
[Wilbert Pumacay]

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## TODAY

.slide_text_content[
*   Reinforcement Learning Background
*   Reinforcement Learning Solution Methods
*   Deep Reinforcement Learning
*   Related works
*   References
]

---
class: center, middle, inverse
# Reinforcement Learning Background

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## Reinforcement Learning Background

.slide_text_content[
Reinforcement learning is a learning paradigm in which an agent learns by interacting with an environment and optimizing the expected sum of rewards received from these interactions.
]

<img src = "imgs/img_RL_loop.png" style = "position: absolute; top: 50%; left: 25%;" >

---
<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## Markov decision processes ( MDP )

.slide_text_content[
    A Markov Decision Process is the basic framework for decision making when dealing with stochastic situations, and it is defined by these components :
    *  A set of states S = {s} ( state space )
    *  A set of actions A = {a} ( action space )
    *  A transition function T( s, a, s' ) = P( s' | s, a )
    *  A reward function R( s, a, s' )
]

<img src = "imgs/img_MDP_elements.png" style = "position: absolute; top: 55%; left: 20%;" >

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## Policies

.slide_text_content[
    The solution to a MDP is a policy, which is a 'function' that returns an action for each given state the agent encounters. The best solution is called optimal policy, which is the policy that maximizes the expected sum of rewards over a trajectory started at an initial state.
]

<img src = "imgs/img_optimal_policy.png" style = "position: absolute; top: 55%; left: 25%;" >

---

class: center, middle, inverse
# Reinforcement Learning Solution Methods

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## Methods

<img src = "imgs/img_rl_methods.png" style = "position: absolute; top: 25%; left: 5%;" >

---

class: center, middle, inverse
# Deep Reinforcement Learning

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## Deep Reinforcement Learning

.slide_text_content[
    Use Deep Neural Networks to 'approximate' modules of a RL setting:
    *   Policies
    *   Value or Q-value functions
    *   Dynamics Models
]

<img src = "imgs/img_drl.png" style = "position: absolute; top: 50%; left: 40%;" >

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## Deep Reinforcement Learning

.slide_text_content[
    By using this approach we can train an agent end-to-end and get a full pipeline, which otherwise would have been hand-crafted.
]

<img src = "imgs/img_end_to_end_drl.png" style = "position: absolute; top: 50%; left: 10%;" >

.footnote[.red[*] Image taken from Berkeley's Deep RL course slides]

---

class: center, middle, inverse
# Related works

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## Deep Q-Networks

<img src = "imgs/img_atari_dqn.png" style = "position: absolute; top: 30%; left: 10%;" >

<p style = "position: absolute; top:90%; left: 30%"> Architecture of DQN, from paper [1]</p>

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## Locomotion

<img src = "imgs/img_locomotion_deepmind.png" style = "position: absolute; top: 30%; left: 15%;" >

<p style = "position: absolute; top:45%; left: 20%"> Humanoid running in simulated environment, from paper [2] </p>

<img src = "imgs/img_deepterrain.png" style = "position: absolute; top: 60%; left: 10%;" >

<p style = "position: absolute; top:80%; left: 20%"> Quadruped running in simulated environment, from paper [4]</p>

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## More locomotion

<img src = "imgs/img_deeploco.png" style = "position: absolute; top: 25%; left: 30%;" >

<p style = "position: absolute; top:50%; left: 20%"> Biped doing task in simulated environment, from paper [5]</p>

<img src = "imgs/img_stuntman_drl.png" style = "position: absolute; top: 60%; left: 10%;" >

<p style = "position: absolute; top:90%; left: 20%"> Virtual stuntman in simulated environment, from paper [6]</p>

---

class: center, middle, inverse
# References

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## References

.slide_text_content[
*   [1] Volodymyr Mnih, et al. Human-level control through deep reinforcement learning. Nature - 2015.
*   [2] Emergence of Locomotion Behaviours in Rich Environments. ArXiv - 2017.
*   [3] Pieter Abbeel, John Schulman. Deep Reinforcement Learning through policy optimization. NIPS - 2016.
*   [4] Xue Bin Peng, Glen Berseth, Michiel van de Panne. Terrain-adaptive locomotion skills using deep reinforcement learning. SIGGRAPH - 2016.
*   [5] Xue Bin Peng, Glen Berseth, KangKang Yin, Michiel van de Panne. Deeploco: Dynamic locomotion skillsusing hierarchical deep reinforcement learning. SIGGRAPH - 2017.
*   [6] Xue Bin Peng, Pieter Abbeel, Sergey Levine, Michiel van de Panne. DeepMimic: Example-Guided Deep Reinforcement learning of Physics-Based Character Skills. Proc. SIGGRAPH - 2018:
]

---

class: center, middle, inverse
# Thanks