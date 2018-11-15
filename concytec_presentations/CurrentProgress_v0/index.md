class: center, middle, inverse

# Evaluation of Deep Reinforcement Learning algorithms in Rich and Complex Environments for Continuous Control
[Msc. Candidate: Wilbert Pumacay]
<br>
<br>
[Advisor: Dr. Jose Ochoa Luna]

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## AGENDA

.slide_text_content[
*   Problem formulation
*   Proposal
*   State of the Art
*   Current progress
]

---
class: center, middle, inverse
# Problem formulation

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## Robot Locomotion

<img src = "imgs/gif_darpa_1.gif" style = "position: absolute; top: 40%; left: 8%; width: 40%; height: 30%">

<p style="position: absolute; top: 70%; left: 32%">DARPA robotics challenge (2015)</p>

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## Robot Locomotion

<img src = "imgs/gif_darpa_1.gif" style = "position: absolute; top: 40%; left: 8%; width: 40%; height: 30%">

<img src = "imgs/gif_darpa_2.gif" style = "position: absolute; top: 40%; left: 54%; width: 40%; height: 30%">

<p style="position: absolute; top: 70%; left: 32%">DARPA robotics challenge (2015)</p>

---

class: center, middle
# The problem (1): Robot locomotion is HARD!

.logo[![logo](imgs/img_logo.jpg)]

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## Robot Locomotion

<img src = "imgs/img_ref_robot_control_darpa.png" style = "position: absolute; top: 25%; left: 15%; width: 80%; height: 40%" >

<p style="position: absolute; top: 55%; left: 70%">Feng, et al. [13]</p>

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## Robot Locomotion

<img src = "imgs/img_ref_robot_control_darpa.png" style = "position: absolute; top: 25%; left: 15%; width: 80%; height: 40%" >

<img src = "imgs/img_ref_levine_drl_course_robotics_pipeline.png" style = "position: absolute; top: 65%; left: 10%; width: 80%; height: 25%" >

<p style="position: absolute; top: 55%; left: 70%">Feng, et al. [13]</p>

<p style="position: absolute; top: 87%; left: 30%">Extracted from DeepRL course cs294, Berkeley [14]</p>

---

class: center, middle
# The approach (1): Try using DeepRL to solve locomotion

.logo[![logo](imgs/img_logo.jpg)]

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## RL Background

.slide_text_content[
RL is a learning approach in which an agent **learns by interaction** with the environment. By each interaction the agent makes with the environment (by taking **actions**), the agent ends up in a different state (because of the **environment dynamics**) and receives a **reward** from the environment according to this transition.
]

<img src = "imgs/img_mdp_1.png" style = "position: absolute; top: 45%; left: 20%;" >

<p style="position: absolute; top: 90%; left: 17%">Extracted from Sutton and Barto, Reinforcement learning book [1]</p>

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## RL Background

.slide_text_content[
RL is a learning approach in which an agent **learns by interaction** with the environment. By each interaction the agent makes with the environment (by taking **actions**), the agent ends up in a different state (because of the **environment dynamics**) and receives a **reward** from the environment according to this transition.
]

<img src = "imgs/img_mdp_2.png" style = "position: absolute; top: 45%; left: 20%;" >

<p style="position: absolute; top: 90%; left: 17%">Extracted from Sutton and Barto, Reinforcement learning book [1]</p>

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## Learning environments

<img src = "imgs/img_reference_learning_environments.png" style = "position: absolute; top: 25%; left: 15%;" >

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## Learning environments - locomotion

<img src = "imgs/img_reference_locomotion_learning_environments_1.png" style = "position: absolute; top: 28%; left: 8%; width: 85%; height: 65%" >

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## Learning environments - locomotion

<img src = "imgs/img_reference_locomotion_learning_environments_2.png" style = "position: absolute; top: 28%; left: 8%; width: 85%; height: 65%" >

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## Learning environments - locomotion

<img src = "imgs/img_reference_locomotion_learning_environments_2_commented.png" style = "position: absolute; top: 28%; left: 8%; width: 85%; height: 65%" >

---

class: center, middle
# The problem (2): There are not enough tools to solve the problem

.logo[![logo](imgs/img_logo.jpg)]

---

class: center, middle, inverse
# Proposal

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## Proposal

<img src = "imgs/img_proposal.png" style = "position: absolute; top: 22%; left: 4%; width: 90%; height: 70%" >

<p style="position: absolute; top: 85%; left: 5%">(a) Sim-to-real, from Tan et al. [15]</p>
<p style="position: absolute; top: 88%; left: 5%">(b) Jetson TX2 platform from NVIDIA</p>
<p style="position: absolute; top: 91%; left: 5%">(c) Dynamixel motors</p>

<p style="position: absolute; top: 60%; left: 63%">(a)</p>
<p style="position: absolute; top: 75%; left: 58%">(b)</p>
<p style="position: absolute; top: 78%; left: 88%">(c)</p>

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## Proposal : Framework

<img src = "imgs/img_proposal_part1_framework.png" style = "position: absolute; top: 25%; left: 4%; width: 90%; height: 70%" >

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## Proposal : Baselines

<img src = "imgs/img_proposal_part2_baselines.png" style = "position: absolute; top: 35%; left: 5%; width: 90%; height: 30%" >

---

class: center, middle, inverse
# State of the art

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## State of the art

<img src = "imgs/gif_reference_state_of_the_art_deepmind_locomotion.gif" style = "position: absolute; top: 27%; left: 4%; width: 50%; height: 40%" >

<img src = "imgs/gif_reference_state_of_the_art_dterrainrl.gif" style = "position: absolute; top: 72%; left: 4%; width: 50%; height: 20%" >

<img src = "imgs/gif_reference_state_of_the_art_minitaur_tfagents.gif" style = "position: absolute; top: 27%; left: 60%; width: 30%; height: 20%" >

<img src = "imgs/gif_reference_state_of_the_art_ant_tfagents.gif" style = "position: absolute; top: 50%; left: 60%; width: 30%; height: 20%" >

<p style="position: absolute; top: 65%">a) Walker traversing terrain, from [8]</p>

<p style="position: absolute; top: 90%">b) Dog traversing terrain, from [10]</p>

<p style="position: absolute; top: 70%; left: 60%">c) Agents from the <b>tfagents</b> package, from [11]</p>

---

class: center, middle, inverse
# Current Progress

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

##  Model Editor + Terrain Generator

<img src = "imgs/img_current_progress_framework_1.png" style = "position: absolute; top: 25%; left: 4%; width: 90%; height: 70%" >

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

##  Model Editor + Terrain Generator

<img src = "imgs/gif_terrain_progress_1.gif" style = "position: absolute; top: 30%; left: 3%; width: 45%; height: 40%" >

<img src = "imgs/gif_terrain_progress_2.gif" style = "position: absolute; top: 30%; left: 51%; width: 45%; height: 40%" >

<p style="position: absolute; top: 70%; left: 17%">WIP: Terrain generator on top of the MuJoCo physics engine [12]</p>

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## Proposed framework: Poster invitation

.slide_text_content[
Invited to present at a workshop in Canada, on Dec. 8 this year. The organizers are the group **LatinxinAI**.
]

<img src = "imgs/img_ref_latinx.png" style = "position: absolute; top: 40%; left: 15%; width: 70%; height: 50%" >

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## Baselines: WIP with extra course

.slide_text_content[
I'm enrolled (paid the fee) for a course in Deep Reinforcement Learning from **Udacity**, called, **Deep Reinforcement Learning Nanodegree**, which I'm using to get to the level I need to implement the baselines.
]

<img src = "imgs/img_current_progress_baselines.png" style = "position: absolute; top: 40%; left: 15%; width: 80%; height: 40%" >

---

class: center, middle, inverse
# References

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## References

.slide_text_content[
*   [1] Richard S. Sutton, Andrew G. Barto. Reinforcement Learning: An Introduction. MIT Press - 2017.
*   [2] Bellemare, et al. The Arcade Learning Environment: An Evaluation Platform for General Agents. IJCAI - 2015.
*   [3] Charles Beattie, et al. DeepMind Lab. ArXiv - 2016.
*   [4] Yuval Tassa, et al. DeepMind Control Suite. ArXiv - 2018.
*   [5] OpenAI. Roboschool. https://github.com/openai/roboschool.
*   [6] Yan Duan, Xi Chen, et al. Benchmarking Deep Reinforcement Learning for Continuous Control. ICML - 2016.
*   [7] Juliani, A., et al. Unity: A General Platform for Intelligent Agents. ArXiv - 2018.
]

---

<!-- logo -->
.logo[![logo](imgs/img_logo.jpg)]

## References

.slide_text_content[
*   [8] Nicolas Heess, et al. Emergence of Locomotion Behaviours in Rich Environments. ArXiv - 2017.
*   [9] Xue Bin Peng, et al. Terrain-Adaptive Locomotion Skills Using Deep Reinforcement Learning. Proc. SIGGRAPH - 2016.
*   [10] Glen Berseth, et al. Terrain RL simulator. ArXiv - 2018.
*   [11] Danijar Hafner, et al. Tensorflow Agents: Efficient Batched Reinforcement Learning in Tensorflow. ArXiv - 2017.
*   [12] MuJoCo physics engine. https://mujoco.org
*   [13] Siyuan Feng, et al. Optimization-based Full Body Control for the DARPA Robotics Challenge. Journal of Field Robotics, Volume 32, Issue 2, pages 293-312, 2015.
*   [14] cs294: Deep Reinforcement Learning course. http://rail.eecs.berkeley.edu/deeprlcourse/ . Berkeley - 2018.
*   [15] Jie Tan, et al. Sim-to-Real: Learning Agile Locomotion For Quadruped Robots. RSS - 2018.
]

---

class: center, middle, inverse
# Thanks