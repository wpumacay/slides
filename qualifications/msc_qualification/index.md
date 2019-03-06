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

*   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam faucibus nisi 
    eget hendrerit auctor. Etiam vitae velit sit amet nibh luctus tincidunt.

<img src="imgs/img_background_deeprl_policy_optimization.png" style = "position: absolute; top: 50%; left: 25%; width: 50%; height: 40%">

---

## Solution methods

*   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam faucibus nisi 
    eget hendrerit auctor. Etiam vitae velit sit amet nibh luctus tincidunt.

<img src = "imgs/img_background_rl_algorithms.png" style = "position: absolute; top: 40%; left: 15%; width: 65%; height: 50%">

.footnote[.red[>] Image taken from SpinningUp in RL [course](https://spinningup.openai.com/en/latest/) by OpenAI]

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

---

class: center, middle, inverse
# Related works

---

## SOTA DeepRL algorithms

*   A simple equation with KaTex: \\( E_\pi \lbrace G_t | s_t = s \rbrace \\)

---

## SOTA locomotion in complex terrain

*   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam faucibus nisi 
    eget hendrerit auctor. Etiam vitae velit sit amet nibh luctus tincidunt.

---

## SOTA DeepRL benchmarks for locomotion

*   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam faucibus nisi 
    eget hendrerit auctor. Etiam vitae velit sit amet nibh luctus tincidunt.

---

class: center, middle, inverse
# Proposal

---

## Proposal: Overview

---

## Proposal: Q: Why?. A: Measure of intelligence

---

## Proposal: Q: Why?. A: Curriculum learning

---

## Proposal: Are we reinventing the wheel?

---

## Proposal: Technical details (1)

---

class: center, middle, inverse
# Current Progress

---

## Current Progress: Framework (1)

---

## Current Progress: Framework (2)

---

## Current Progress: Framework (3)

---

## Current Progress: Framework (4)

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

