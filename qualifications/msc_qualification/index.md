class: center, middle

# Evaluation of Deep Reinforcement Learning algorithms in Rich and Complex Environments for Locomotion Tasks

<br>
Author: Wilbert Santos Pumacay Huallpa
<br>
<br>
Advisor: José Eduardo Ochoa Luna

---

## OUTLINE

*   Motivation
*   Background
*   Related works
*   Proposal
*   Current Progress
*   Preliminary conclusions

---
class: center, middle, inverse
# Motivation

---

## DeepRL success stories

<img src="imgs/gif_reference_atari_dqn.gif" style = "position: absolute; top: 21%; left: 8%; width: 40%; height: 30%">
<img src="imgs/gif_reference_alphastar.gif" style = "position: absolute; top: 21%; left: 52%; width: 40%; height: 30%">

<img src="imgs/img_reference_alphago.png" style = "position: absolute; top: 58%; left: 8%; width: 40%; height: 30%">
<img src="imgs/gif_reference_openai_five.gif" style = "position: absolute; top: 58%; left: 52%; width: 40%; height: 30%">

---

## DeepRL in locomotion

<img src="imgs/gif_reference_emergence_locomotion.gif" style = "position: absolute; top: 21%; left: 8%; width: 40%; height: 30%">
<img src="imgs/gif_reference_deepmimic.gif" style = "position: absolute; top: 21%; left: 52%; width: 40%; height: 30%">

<img src="imgs/gif_reference_minitaur_sac.gif" style = "position: absolute; top: 58%; left: 8%; width: 40%; height: 30%">
<img src="imgs/gif_reference_openai_dexterity.gif" style = "position: absolute; top: 58%; left: 52%; width: 40%; height: 30%">

---

## DeepRL benchmarks for locomotion

--

*   Current locomotion benchmarks allow to train agents in simulated environments
    based on popular physics engines.

--

*   However, these benchmarks do not offer more diverse and complex environments,
    and mostly consist of relatively simple environments.

--

*   Therefore, we focus on making the required infrastructure and support to
    allow researchers to build diverse and complex environments.

--

*   To do so, we propose to build a full locomotion framework from scratch, using
    only widely used physics engines as core dependencies.

--

*   Also, we focus on evaluating current state-of-the-art (SOTA) DeepRL algorithms
    in a new benchmark consisting of tasks built using the proposed framework.

---

## DeepRL benchmarks for locomotion

<img src="https://raw.githubusercontent.com/wpumacay/msc_qualif_doc/master/chapters/chapter_1/imgs/img_ch1_environments_from_to.png" 
     style="position: absolute; top: 30%; left: 10%; width: 80%; height: 60%">

---

class: center, middle, inverse
# Background

---

## Reinforcement Learning (RL)

<img src="imgs/img_background_rl_loop.png" style = "position: absolute; top: 60%; left: 28%; width: 45%; height: 30%">

--

*   RL is a learning approach in which an agent learns by interaction with an environment.

--

*   The agent configuration is given by a state \\( s_t \\).

--

*   Then, the agent interacts by means of actions \\( a_t \\)

--

*   As a result, the agent gets a reward \\( r_{t+1} \\) for that interaction.

---

## Learning Representations (Deep Learning)

--

*   Deep Learning allows us to learn useful representation by using deep models
    trained end-to-end, instead of handcrafting the required features for a given task.

--

<img src="imgs/img_background_deeprl_intuition_1.png" style = "position: absolute; top: 50%; left: 15%; width: 70%; height: 40%">

---

## Deep Reinforcement Learning (DeepRL)

--

*   By combining Reinforcement Learning with deep learning models we can learn to take
    decisions directly from raw sensory inputs, without handcrafting features, e.g. learn
    to play a video game from frames as inputs, and acting directly with the gamepad actions.

--

<img src="imgs/img_background_deeprl_dqn.png" style = "position: absolute; top: 50%; left: 15%; width: 70%; height: 40%">

---

## Learning behaviours end-to-end

--

*   By using DeepRL we can train agents end-to-end in a very different approach to
    traditional pipelines, e.g. for robotics we could train agents without crafting
    separate modules of a traditional robotics pipeline.

--

<img src="imgs/img_background_deeprl_intuition_2.png" style = "position: absolute; top: 50%; left: 15%; width: 70%; height: 40%">

---

## DeepRL

--

*   Deep models (whose parameters we represent by \\( \theta \\)) can be used to 
    parameterize various components of the RL problem.

--

*   The State-Value and Action-Value functions: 
    *   \\( V_\theta (s) \\)
    *   \\( Q_\theta (s,a) \\)

--

*   The Policy :
    *   Deterministic: \\( a = \pi_{\theta}(s) \\)
    *   Stochastic: \\( a \sim \pi_{\theta}(.|s) \\)

--

*   The Model:
    *   \\( s' = f_\theta (s, a) \\)

---

## DeepRL

*   Deep models (whose parameters we represent by \\( \theta \\)) can be used to 
    parameterize various components of the RL problem.

*   The baselines we will focus on deal mainly with parameterized policies

--

<img src="imgs/img_background_deeprl_parameterized_policy.png" style = "position: absolute; top: 50%; left: 25%; width: 50%; height: 40%">

---

## Solution methods

*   Below we show a taxonomy of current DeepRL algorithms, separated between
    model-free and model-based. 

<img src = "imgs/img_background_rl_algorithms.png" style = "position: absolute; top: 45%; left: 20%; width: 60%; height: 45%">

.footnote[.red[>] Image taken from SpinningUp in RL [course](https://spinningup.openai.com/en/latest/) by OpenAI]

--

*   The baselines we will use belong to the Policy Optimization class of algorithms,
    and are highlighted below.

<img src = "imgs/img_util_rectangle.png" style = "position: absolute; top: 71%; left: 19.5%; width: 23%; height: 21%">

---

## Policy Optimization

--

*   We focus on policy optimization algorithms, which try to learn the parameters
    \\( \theta \\) of a parameterized policy \\( \pi_{\theta} \\) such that it maximizes
    the following expected return:

.center[![Policy-gradients cost](imgs/img_related_works_pg_base_cost.png)]

--

*   The **Vanilla Policy Gradients** algorithm updates the weights \\( \theta \\)
    of the policy by computing an estimate \\( \hat g \\) of the gradient of 
    the loss function from above (refer to section 2.1.3 for more details):

.center[![Policy-gradients cost](imgs/img_related_works_pgradient.png)]

---

## Simulated environments

<img src="imgs/img_background_rl_loop.png" style = "position: absolute; top: 5%; left: 60%; width: 30%; height: 18%">

---

count: false

## Simulated environments

<img src="imgs/img_background_rl_loop.png" style = "position: absolute; top: 5%; left: 60%; width: 30%; height: 18%">

*   These consists of simulations, which serve as learning environments for our RL agents.
    Some such environments are shown below:

---

layout: true

## Simulated environments

<img src="imgs/img_background_rl_loop.png" style = "position: absolute; top: 5%; left: 60%; width: 30%; height: 18%">

*   These consists of simulations, which serve as learning environments for our RL agents.
    Some such environments are shown below:

---

count: false

*   The Atari Learning Environment (ALE), consist of an interface to Atari 2600
    games. The API exposes as observations the raw frames of the game, and as 
    actions the available actions for an Atari gamepad.

<img src="https://raw.githubusercontent.com/wpumacay/msc_qualif_doc/master/chapters/chapter_2/imgs/img_atari_learning_environment.png"
     style="position: absolute; top: 55%; left: 25%; width: 50%; height: 30%">

---

count: false;

*   Gym (by OpenAI) consists of a set of environments in various domains, from
    simple toy-text problems, to complex robotic manipulation simulations.

<img src="https://raw.githubusercontent.com/wpumacay/msc_qualif_doc/master/chapters/chapter_2/imgs/img_openai_gym_envs.png"
    style="position: absolute; top: 50%; left: 20%; width: 60%; height: 40%">

---

layout: false

## Locomotion environments

*   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam faucibus nisi 
    eget hendrerit auctor. Etiam vitae velit sit amet nibh luctus tincidunt.

---

class: center, middle, inverse
# Related works

---

class: center, middle
# DeepRL algorithms used in locomotion

---

## Trust Region Policy Optimization (TRPO)

*   Desc. 1
*   Desc. 2

<iframe src="https://www.youtube.com/embed/jeid0wIrSn4" 
        frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen
        style="position: absolute; top: 40%; left: 20%; width: 60%; height: 50%"></iframe>

---

## Proximal Policy Optimization (PPO)

*   Desc. 1
*   Desc. 2

<iframe src="https://d4mucfpksywv.cloudfront.net/openai-baselines-ppo/knocked-over-stand-up.mp4"
        frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen
        style="position: absolute; top: 50%; left: 5%; width: 40%; height: 30%"></iframe>

<iframe src="https://d4mucfpksywv.cloudfront.net/openai-baselines-ppo/atlas.mp4"
        frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen
        style="position: absolute; top: 50%; left: 55%; width: 40%; height: 30%"></iframe>

---

## Soft Actor-Critic (SAC)

*   Desc. 1
*   Desc. 2

<iframe src="https://www.youtube.com/embed/FmMPHL3TcrE?start=48" 
        frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen
        style="position: absolute; top: 50%; left: 5%; width: 40%; height: 30%"></iframe>

<iframe src="https://www.youtube.com/embed/KOObeIjzXTY" 
        frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen
        style="position: absolute; top: 50%; left: 55%; width: 40%; height: 30%"></iframe>

---

class: center, middle
# Recent DeepRL results in locomotion

---

## Benchmarking DeepRL for Continuous control

*   Desc. 1
*   Desc. 2

---

## DeepTerrainRL

*   Desc. 1
*   Desc. 2

<iframe src="https://www.youtube.com/embed/KPfzRSBzNX4?start=59" 
        frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen
        style="position: absolute; top: 40%; left: 20%; width: 60%; height: 50%"></iframe>

---

## DeepLoco

*   Desc. 1
*   Desc. 2

<iframe src="https://www.youtube.com/embed/G4lT9CLyCNw?start=11" 
        frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen
        style="position: absolute; top: 40%; left: 20%; width: 60%; height: 50%"></iframe>

---

## Emergence of locomotion behaviours in rich environments

*   Desc. 1
*   Desc. 2

<iframe src="https://www.youtube.com/embed/hx_bgoTF7bs?start=11" 
        frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen
        style="position: absolute; top: 50%; left: 22.5%; width: 50%; height: 40%"></iframe>

---

class: center, middle
# DeepRL benchmarks for locomotion

---

## OpenAI-Gym: MuJoCo-py

*   Desc. 1

---

## OpenAI-Gym: Roboschool

*   Desc. 1

---

## Deepmind: Controlsuite

*   Desc. 1

---

## Rllab and Garage

*   Desc. 1

---

## Robosuite

*   Desc. 1

---

## GPU-Accelerated Simulation

*   Desc. 1

---

## TerrainRLSim

*   Desc. 1

---

## Unity ML-Agents

*   Desc. 1

---

class: center, middle, inverse
# Proposal

---

## Overview

---

## Why?: Measure of intelligence

---

## Why?: Curriculum learning

---

## Are we reinventing the wheel?

---

## Technical details (1)

---

class: center, middle, inverse
# Current Progress

---

## Framework (1)

---

## Framework (2)

---

## Framework (3)

---

## Framework (4)

---

class: center, middle, inverse
# Preliminary conclusions

---

## Preliminary Conclusions

---
class: center, middle, inverse
# References

---

## References

---

class: center, middle, inverse
# Thanks for your attention. Any questions?

