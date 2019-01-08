class: center, middle, inverse

# A quick overview of (Deep)Reinforcement Learning
<br>
[Wilbert Santos Pumacay Huallpa]

---

## OUTLINE

.slide_text_content[
*   The RL problem
*   An overview of the solution methods
*   Value based methods
    *   Model-based methods using DP
    *   Model-free prediction using MC and TD
    *   Model-free control using MC, SARSA and Q-learning
*   Function Approximation
*   Policy based methods
    *   Vanilla Policy Gradients
    *   Improving PG
    *   Actor-Critic
*   An overview of DeepRL
    *   Why DeepRL?
    *   Case study: DQN
    *   Case study: PPO
]

---
class: center, middle, inverse
# The RL problem

---

## The RL problem

.slide_text_content[
*   RL is a learning approach in which an agent **learns by interaction** with the 
    environment.
]

---

## The RL problem

.slide_text_content[
*   RL is a learning approach in which an agent **learns by interaction** with the 
    environment. 
*   By each interaction the agent makes with the environment (by taking **actions**), 
    the agent ends up in a different state (because of the **environment dynamics**) 
    and receives a **reward** from the environment according to this transition.
]

---

## The RL problem

.slide_text_content[
*   RL is a learning approach in which an agent **learns by interaction** with the 
    environment. 
*   By each interaction the agent makes with the environment (by taking **actions**), 
    the agent ends up in a different state (because of the **environment dynamics**) 
    and receives a **reward** from the environment according to this transition.
*   The objective of the agent is then to get the most reward it can in all its
    interactions, so it tries to pick actions that would try to **maximize the total
    sum of rewards**.
]

---

## The RL problem

.slide_text_content[
*   RL is a learning approach in which an agent **learns by interaction** with the 
    environment. 
*   By each interaction the agent makes with the environment (by taking **actions**), 
    the agent ends up in a different state (because of the **environment dynamics**) 
    and receives a **reward** from the environment according to this transition.
*   The objective of the agent is then to get the most reward it can in all its
    interactions, so it tries to pick actions that would try to **maximize the total
    sum of rewards**.
]

<img src = "imgs/img_rl_loop.png" style = "position: absolute; top: 60%; left: 18%; width: 65%; height: 35%">

---

## Example: locomotion

<img src = "imgs/img_rl_mdp_locomotion.png" style = "position: absolute; top: 35%; left: 5%; width: 95%; height: 55%">

---

## Example: video games

<img src = "imgs/img_rl_mdp_atari.png" style = "position: absolute; top: 35%; left: 5%; width: 95%; height: 55%">

---

## RL background: MDPs

.slide_text_content[
*   To mathematically formalize the RL problem we make use of Markov Decision Processes (MDPs),
    which are a framework to model sequential decision making problems under uncertainty.
]

---

## RL background: MDPs

.slide_text_content[
*   To mathematically formalize the RL problem we make use of Markov Decision Processes (MDPs),
    which are a framework to model sequential decision making problems under uncertainty.
]

<img src = "imgs/img_rl_mdp_definition.png" style = "position: absolute; top: 42%; left: 10%; width: 85%; height: 50%">

---
<!-- POMDP SLIDE BEGIN --------------------------->
## RL background: POMDPs

.slide_text_content[
*   In general, the Markov property is not satisfied in most of the settings we work with,
    due to the fact that we cannot observe the full environment state.
]

---

## RL background: POMDPs

.slide_text_content[
*   In general, the Markov property is not satisfied in most of the settings we work with,
    due to the fact that we cannot observe the full environment state.
*   Instead, we usually just have an observation \\(o_t\\) that gives some information
    about the state of the environment.
]

---

## RL background: POMDPs

.slide_text_content[
*   In general, the Markov property is not satisfied in most of the settings we work with,
    due to the fact that we cannot observe the full environment state.
*   Instead, we usually just have an observation \\(o_t\\) that gives some information
    about the state of the environment.
]

<img src="imgs/img_pomdp_dog_chase_cat_1.png" style="position: absolute; top: 60%; left: 5%; width: 45%; height: 35%">

---

## RL background: POMDPs

.slide_text_content[
*   In general, the Markov property is not satisfied in most of the settings we work with,
    due to the fact that we cannot observe the full environment state.
*   Instead, we usually just have an observation \\(o_t\\) that gives some information
    about the state of the environment.
]

<img src="imgs/img_pomdp_dog_chase_cat_1.png" style="position: absolute; top: 60%; left: 5%; width: 45%; height: 35%">
<img src="imgs/img_pomdp_dog_chase_cat_2.png" style="position: absolute; top: 60%; left: 50%; width: 45%; height: 35%">

---

## RL background: POMDPs

.slide_text_content[
*   In general, the Markov property is not satisfied in most of the settings we work with,
    due to the fact that we cannot observe the full environment state.
*   Instead, we usually just have an observation \\(o_t\\) that gives some information
    about the state of the environment.
]

<img src="imgs/img_pomdp_dog_chase_cat_1.png" style="position: absolute; top: 60%; left: 5%; width: 45%; height: 35%">
<img src="imgs/img_pomdp_dog_chase_cat_2.png" style="position: absolute; top: 60%; left: 50%; width: 45%; height: 35%">
<img src="imgs/img_pomdp_car_occlusion.png" style="position: absolute; top: 70%; left: 15%; width: 25%; height: 15%">

---

## RL background: POMDPs

.slide_text_content[
*   In general, the Markov property is not satisfied in most of the settings we work with,
    due to the fact that we cannot observe the full environment state.
*   Instead, we usually just have an observation \\(o_t\\) that gives some information
    about the state of the environment.
]

<img src="imgs/img_rl_pomdp_definition.png" style="position: absolute; top: 50%; left: 10%; width: 80%; height: 45%">

---

## RL background: POMDPs

.slide_text_content[
*   In general, the Markov property is not satisfied in most of the settings we work with,
    due to the fact that we cannot observe the full environment state.
*   Instead, we usually just have an observation \\(o_t\\) that gives some information
    about the state of the environment.
*   To avoid this, we can do state augmentation, to try to satisfy the underlying
    markov property of the environment (if any exists).
]

<img src="imgs/img_pomdp_dog_chase_cat_3.png" style="position: absolute; top: 60%; left: 5%; width: 45%; height: 35%">
<img src="imgs/img_pomdp_dog_chase_cat_2.png" style="position: absolute; top: 60%; left: 50%; width: 45%; height: 35%">
<!-- POMDP SLIDE END ----------------------------->

---

## RL background: Returns

.slide_text_content[
*   As mentioned earlier, the objective of the agent is to maximize the sum of rewards
    (discounted sum if using a discount factor) it gets from its interaction with
    the environment.
]

---

## RL background: Returns

.slide_text_content[
*   As mentioned earlier, the objective of the agent is to maximize the sum of rewards
    (discounted sum if using a discount factor) it gets from its interaction with
    the environment.
*   We define the total (discounted) sum of rewards from timestep _t_ the **Return** \\(G_{t}\\).
]

---

## RL background: Returns

.slide_text_content[
*   As mentioned earlier, the objective of the agent is to maximize the sum of rewards
    (discounted sum if using a discount factor) it gets from its interaction with
    the environment.
*   We define the total (discounted) sum of rewards from timestep _t_ the **Return** \\(G_{t}\\).
]

<img src="imgs/img_rl_return.png" style="position: absolute; top: 50%; left: 30%;">

---

## RL background: Returns

.slide_text_content[
*   As mentioned earlier, the objective of the agent is to maximize the sum of rewards
    (discounted sum if using a discount factor) it gets from its interaction with
    the environment.
*   We define the total (discounted) sum of rewards from timestep _t_ the **Return** \\(G_{t}\\).
*   Because the return is a random variable, then the return will vary with each interaction
    with the environment. So instead we try to maximize the **expected sum of rewards**, or
    **Expected Return**.
]

---

## RL background: Returns

.slide_text_content[
*   As mentioned earlier, the objective of the agent is to maximize the sum of rewards
    (discounted sum if using a discount factor) it gets from its interaction with
    the environment.
*   We define the total (discounted) sum of rewards from timestep _t_ the **Return** \\(G_{t}\\).
*   Because the return is a random variable, then the return will vary with each interaction
    with the environment. So instead we try to maximize the **expected sum of rewards**, or
    **Expected Return**.
]

<img src="imgs/img_rl_expected_return.png" style="position: absolute; top: 65%; left: 35%;">

---

## Comparison to Supervised Learning

.slide_text_content[
*   In the context of Supervised Learning, we learn from a given dataset and
    optimize our model to _optimize a metric_/_minimize a loss_ for a certain task like
    classification.
*   For supervised learning tasks the dataset is given, and we make the assumption 
    that the data satisfies the **i.i.d** property (independent and identically distributed).
*   In RL we completely violate this assumption, due to the sequential nature of
    the tasks. 
*   Next states, rewards and observations are dependent of the previous state of the
    environment, and this in turn depended on the previous actions taken by the agent.
*   Basically, the experience (data) that the agent collects is dependent of previous
    actions (at least from the previous time step, if satisfying the Markov property).
]

---