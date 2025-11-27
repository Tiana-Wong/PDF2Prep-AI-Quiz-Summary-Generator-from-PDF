# Math Materials Revision Guide
## Mathematics in Games and Animations

**A comprehensive study guide for exam revision**

---

## Table of Contents

- [L12 - Collision Detection](#l12---collision-detection)
- [L1a - Course Overview](#l1a---course-overview)
- [L1b - Cartesian Coordinates](#l1b---cartesian-coordinates)
- [L1c - Multiple Coordinate Spaces](#l1c---multiple-coordinate-spaces)
- [L2a - Vectors](#l2a---vectors)
- [L2b- Random Numbers](#l2b--random-numbers)
- [L3 - Matrices](#l3---matrices)
- [L4a - Matrices and linear transformations](#l4a---matrices-and-linear-transformations)
- [L4b - Classes of transformations at a glance](#l4b---classes-of-transformations-at-a-glance)
- [L5a Matrix determinant - inverse - orthogonalization](#l5a-matrix-determinant---inverse---orthogonalization)
- [L6a - Homogeneous Matrices](#l6a---homogeneous-matrices)
- [L6b - 2D Polar Coordinate Systems](#l6b---2d-polar-coordinate-systems)
- [L6c - 3D Polar Coordinate Systems](#l6c---3d-polar-coordinate-systems)
- [L7 - Rotation in Three Dimensions -All forms](#l7---rotation-in-three-dimensions--all-forms)
- [L9 - Pendulum, Circular, Harmonic motion](#l9---pendulum,-circular,-harmonic-motion)

---


## L12 - Collision Detection

### Overview

[Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 12
Collision Detection
© P. Mengoni, IMD HKBU. All Rights Reserved. This content is copyright protected and shall not be shared, uploaded or distribu ted.Dr.Paolo Mengoni
pmengoni@hkbu.edu.hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Agenda
▪What is Collision Detection
▪Useful definitions: lines and rays
▪Bounding Spheres and Circles
▪Bounding Boxes
▪Collision Testing
▪Final Considerations
GAME20

### Key Concepts

- • Animation: interpolation, keyframe, easing
- • Collision: AABB, sphere, ray-casting
- • Vector: magnitude, direction, component
- • Rotation: quaternion, euler angles, axis-angle
- • Numerical Values: 

### Formulas & Equations

```
n= [ a  b], p= [ x  y] and use
```
```
by= d
```
```
p= [ x y z ]
```
```
p0= [ x0   y0   z0 ]
```
```
d = 0
```
```
n= d
```
```
d= [ x  y  z ]
```

### Applications

- ▪Applied to lots of objects, often in real -time 
applications
- [Page 22]
GAME2016 Mathematical Foundation of Game Design and Animation

[Page 23]
Spheres in Collision Detection
▪A bounding sphere is often used in collision 
detection for fast rejection because the equations 
for intersection with a sphere are simple
- ▪A bounding sphere can be used for an object 
regardless of the orientation of the object
- Expanding this, if p= [ x y z ]:
(x–cx)2+ (y–cy)2= r2(2D circle )
(x–cx)2+ (y–cy)2+ (z–cz)2= r2(3D sphere )
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 26]
Bounding Boxes
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 27]
Types of Bounding Box
▪Like spheres, bounding boxes are also used in 
collision detection
- ▪Can be efficient for some 
applications
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 37]
Collision Testing
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 38]
Testing for Collision
▪Will depend on type of objects and bounding 
volumes

### Quiz Questions


**Q1: [Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 12
Collision Detection
© P?**
- A) GAME2016
- B) 1]
- C) Mathematical
- D) Foundation

✓ **Answer: A**

**Q2: This content is copyright protected and shall not be shared, uploaded or distribu ted?**
- A) is
- B) content
- C) copyright
- D) protected

✓ **Answer: A**

**Q3: hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Agenda
▪What is Collision Detection
▪Useful definitions?**
- A) Lecturer
- B) Senior
- C) @HKBU
- D) Department

✓ **Answer: A**

**Q4: ▪Given two geometric objects, determine if they 
overlap?**
- A) geometric
- B) two
- C) objects,
- D) determine

✓ **Answer: A**

**Q5: ▪Typically, at least one of the objects is a set of 
triangles?**
- A) least
- B) at
- C) one
- D) of

✓ **Answer: A**

**Q6: ▪Rays/lines
▪Planes
▪Polygons
▪Frustums
▪Spheres
▪Curved surfaces
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 5]
When to useit
▪Often in simulations?**
- A) ▪Polygons
- B) ▪Planes
- C) ▪Frustums
- D) ▪Spheres

✓ **Answer: A**

**Q7: ▪Objects move –find when they hit something 
else
▪Other examples?**
- A) –find
- B) move
- C) when
- D) they

✓ **Answer: A**

**Q8: ▪Usually , needs to be fast?**
- A) needs
- B) ,
- C) to
- D) be

✓ **Answer: A**

### Practice Problems


**Problem 1:**
Calculate the result when applying Animation to the values 1, 12

**Solution Approach:** Refer to the Animation formula: work through step by step

**Problem 2:**
Explain how Collision differs from Vector

**Solution Approach:** Consider the definitions, properties, and applications of each

**Problem 3:**
Apply Vector to a scenario with game animation

**Solution Approach:** Break down the problem using the relevant formula or definition

### Revision Tips

- 1. Focus on understanding the core formulas and when to use them
- 2. Practice working through numerical examples
- 3. Understand the geometric or visual interpretation
- 4. Relate concepts to real-world game/animation scenarios
- 5. Create flashcards for key terms and definitions

---

## L1a - Course Overview

### Overview

[Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 1
Course Overview
©P. Mengoni, IMD HKBU. All Rights Reserved. This content is copyright protected and shall not be shared, uploaded or distribu ted.Dr. Paolo Mengoni
pmengoni@hkbu.edu.hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Course Overview
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 3]
Contact Information
▪Lecturer
▪Dr. Paolo Mengoni
▪Email: pmengoni@hkbu.edu.hk  
▪Co

### Key Concepts

- • Animation: interpolation, keyframe, easing
- • Vector: magnitude, direction, component
- • Matrix: determinant, inverse, transpose
- • Coordinate: cartesian, polar, spherical
- • Transformation: translation, scaling, shear
- • Collision: AABB, sphere, ray-casting
- • Numerical Values: 

### Formulas & Equations

```
▪Perugia! [ Video ]
```

### Applications

- ▪Basic mathematical foundation
▪Formal logic underpinning mathematics in general
▪Basic mathematical notions of vector, matrix, 
linear algebra, geometrical transformations in 2D 
and 3D
▪Motion of objects on the screen
▪Combinatorics and probability theory to enrich 
game designs and animations with stochastic 
behaviors and random outcomes
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 12]
Course Objectives
▪Course aims to
▪Explain the fundamental concepts and principles of the 
mathematical topics covered;
▪Perform basic deductions based on the mathematical 
principles covered to solve a mathematical problem;
▪Explain the mathematical approaches used in the 
context of game design and computer animation;
▪Apply the theories and concepts to model similar 
mathematical problems in game design and animation
- GAME2016 Mathematical Foundation of Game Design and Animation
[Page 13]
This course is interdisciplinary
▪Visual approach to Mathematics using Computer 
Science for Game Development and Animation
▪In the lectures will have a mathematics theory 
component and a computer programming 
component
▪We will:
▪Use a series of problem -based, practical exercises
▪Explore ideas about drawing graphics on a screen and 
how to implement physics techniques such as collisions 
and particle emitters
▪Apply vectors, vertices, matrices to 2D and 3D graphics
▪Use Python and its libraries to solve mathematical 
problems
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 14]
Course Information & Topics
▪Time & Venue
▪Wed  12:30 -15:20  (CVA203)
▪Three modules (tentative schedule):
▪Coordinates and Vectors (Week 1 -3)
▪Matrices and Transformations (Week 4 -9)
▪Advanced Math in GDA (Week 10 -11)
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 15]
Assessment Structure
GAME2016 Mathematical Foundation of Game Design and AnimationAssessment Weight
In-Class Exercises 30%
Assignments 30%
Final Exam 40%
[Page 16]
Assessment
▪In-Class Exercises (30%)
▪Exercises will be given and completed during the 
class: 
▪(ir-)regular  small quizzes and exercises
▪When
- Always
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 17]
Assessment
▪Assignments (30% total)
▪Applications of mathematics to game design and 
animation problems (20%)
▪Students will be assigned in a group to investigate applications of 
mathematics in game design and animation
▪Deliverables will include a written report and delivery of 10 to 20 minutes 
in-class presentation
▪Individual reflections and peer evaluation (10%)
▪The students will provide anonymous feedback to peers (100 -200 words 
in English)
▪The students will critically evaluate and reflect on their group work (200 -
300 words in English)
▪When
- ▪Improper Use of Generative AI Tools
▪Presenting the output of GenAI tools as your own work is a violation of 
the University’s guidelines for students on academic integrity
▪The following methods might be used to check your work:
▪Request GenAI records of use
▪Request drafts of your work
▪Request to be orally examined on your submission
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 21]
Group Activities
▪Grouping: 4 students per group
▪depends on final enrolment
▪Group List Deadline: The group leader (ONLY) 
should send the group list via email by 23 
September including the following information
▪Group leader name, responsible for the communications
▪Group  member names and student IDs
GAME2016 Mathematical Foundation of Game Design and Animation
Group Activities:
Teamwork will be evaluated
Do NOT simply combine individual part
[Page 22]
Textbooks and Readings
▪Fletcher Dunn, & Ian Parberry

### Quiz Questions


**Q1: [Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 1
Course Overview
©P?**
- A) GAME2016
- B) 1]
- C) Mathematical
- D) Foundation

✓ **Answer: A**

**Q2: This content is copyright protected and shall not be shared, uploaded or distribu ted?**
- A) is
- B) content
- C) copyright
- D) protected

✓ **Answer: A**

**Q3: hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Course Overview
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 3]
Contact Information
▪Lecturer
▪Dr?**
- A) Lecturer
- B) Senior
- C) @HKBU
- D) Department

✓ **Answer: A**

**Q4: hk  
▪Consultation hours?**
- A) hours:
- B) ▪Consultation
- C) by
- D) appointment

✓ **Answer: A**

**Q5: GAME2016 Mathematical Foundation of Game Design and Animation
http?**
- A) Foundation
- B) Mathematical
- C) of
- D) Game

✓ **Answer: A**

**Q6: com/large -detailed -illustrated -tourist -map -of-italy/
[Page 7]
Where I am From
▪Perugia?**
- A) -illustrated
- B) -detailed
- C) -tourist
- D) -map

✓ **Answer: A**

**Q7: GAME2016 Mathematical Foundation of Game Design and Animation
http?**
- A) Foundation
- B) Mathematical
- C) of
- D) Game

✓ **Answer: A**

**Q8: com/large -detailed -illustrated -tourist -map -of-italy/

[Page 8]
Where I am From
▪Perugia?**
- A) -illustrated
- B) -detailed
- C) -tourist
- D) -map

✓ **Answer: A**

### Practice Problems


**Problem 1:**
Calculate the result when applying Animation to the values 1, 1

**Solution Approach:** Refer to the Animation formula: work through step by step

**Problem 2:**
Explain how Vector differs from Matrix

**Solution Approach:** Consider the definitions, properties, and applications of each

**Problem 3:**
Apply Matrix to a scenario with game animation

**Solution Approach:** Break down the problem using the relevant formula or definition

### Revision Tips

- 1. Focus on understanding the core formulas and when to use them
- 2. Practice working through numerical examples
- 3. Understand the geometric or visual interpretation
- 4. Relate concepts to real-world game/animation scenarios
- 5. Create flashcards for key terms and definitions

---

## L1b - Cartesian Coordinates

### Overview

[Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 1
Cartesian Coordinate Systems
©P. Mengoni, IMD HKBU. All Rights Reserved. This content is copyright protected and shall not be shared, uploaded or distribu ted.Dr. Paolo Mengoni
pmengoni@hkbu.edu.hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Agenda
▪1D Mathematics
▪2D Cartesian mathematics
▪3D Cartesian mathematics
▪Angles and Trigonometric functions
GAME2016 Mathematical Foundation of Game Desig

### Key Concepts

- • Animation: interpolation, keyframe, easing
- • Coordinate: cartesian, polar, spherical
- • Rotation: quaternion, euler angles, axis-angle
- • Numerical Values: 

### Formulas & Equations

```
cos θ = x
```
```
▪The angle θ in figure
```
```
multiply by 180/ π (i.e., ≈ 57.29578)
```
```
θ Radians
```
```
▪360° = 2π rad
```
```
▪Circumference = 2 πr = 2π1 = 2π
```
```
▪To convert an angle θ from degrees to radians , we
```
```
▪The circumference of a unit circle is 2 π radians
```
```
cos θsin θ
```
```
▪π approximately equal to 3.14159265359
```

### Applications

- ▪The most frequently used framework to perform 
such calculations using a computer is called the 
Cartesian coordinate system
- GAME2016 Mathematical Foundation of Game Design and Animation

[Page 25]
Angles and Trigonometric 
functions
[Page 26]
Odds and Ends of Math Used
▪Summation and product notation:
GAME2016 Mathematical Foundation of Game Design and Animation

[Page 27]
Angles
▪An angle  measures an amount of rotation  in the 
plane

### Quiz Questions


**Q1: [Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 1
Cartesian Coordinate Systems
©P?**
- A) GAME2016
- B) 1]
- C) Mathematical
- D) Foundation

✓ **Answer: A**

**Q2: This content is copyright protected and shall not be shared, uploaded or distribu ted?**
- A) is
- B) content
- C) copyright
- D) protected

✓ **Answer: A**

**Q3: hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Agenda
▪1D Mathematics
▪2D Cartesian mathematics
▪3D Cartesian mathematics
▪Angles and Trigonometric functions
GAME2016 Mathematical Foundation of Game Design and Animation

[Page 3]
1D Mathematics
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 4]
Introduction
▪3D math is all about measuring
▪Locations
▪Distances
▪Angles 
▪precisely and mathematically in 3D space?**
- A) Lecturer
- B) Senior
- C) @HKBU
- D) Department

✓ **Answer: A**

**Q4: ▪The most frequently used framework to perform 
such calculations using a computer is called the 
Cartesian coordinate system?**
- A) frequently
- B) most
- C) used
- D) framework

✓ **Answer: A**

**Q5: GAME2016 Mathematical Foundation of Game Design and Animation
[Page 5]
René Descartes, 1596 - 1650
▪Cartesian mathematics was 
invented by René Descartes 
(1596 –1650)
▪French philosopher, physicist, 
physiologist, and mathematician?**
- A) Foundation
- B) Mathematical
- C) of
- D) Game

✓ **Answer: A**

**Q6: ▪Cartesian mathematics is a 
unification of algebra and 
geometry?**
- A) is
- B) mathematics
- C) a
- D) unification

✓ **Answer: A**

**Q7: GAME2016 Mathematical Foundation of Game Design and Animation
Source?**
- A) Foundation
- B) Mathematical
- C) of
- D) Game

✓ **Answer: A**

**Q8: ▪Corresponding to short, int, float, and double on a computer 
(with a limited precision)?**
- A) short,
- B) to
- C) int,
- D) float,

✓ **Answer: A**

### Practice Problems


**Problem 1:**
Calculate the result when applying Animation to the values 1, 1

**Solution Approach:** Refer to the Animation formula: work through step by step

**Problem 2:**
Explain how Coordinate differs from Rotation

**Solution Approach:** Consider the definitions, properties, and applications of each

**Problem 3:**
Apply Rotation to a scenario with game animation

**Solution Approach:** Break down the problem using the relevant formula or definition

### Revision Tips

- 1. Focus on understanding the core formulas and when to use them
- 2. Practice working through numerical examples
- 3. Understand the geometric or visual interpretation
- 4. Relate concepts to real-world game/animation scenarios
- 5. Create flashcards for key terms and definitions

---

## L1c - Multiple Coordinate Spaces

### Overview

[Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 1
Coordinate spaces
©P. Mengoni, IMD HKBU. All Rights Reserved. This content is copyright protected and shall not be shared, uploaded or distribu ted.Dr. Paolo Mengoni
pmengoni@hkbu.edu.hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Agenda
▪Why multiple coordinate spaces?
▪Some useful coordinate spaces.
▪Coordinate space transformations.
▪Camera Space
GAME2016 Mathematical Foundation of Game Design

### Key Concepts

- • Animation: interpolation, keyframe, easing
- • Coordinate: cartesian, polar, spherical
- • Rotation: quaternion, euler angles, axis-angle
- • Transformation: translation, scaling, shear
- • Collision: AABB, sphere, ray-casting
- • Numerical Values: 

### Formulas & Equations


### Applications

- GAME2016 Mathematical Foundation of Game Design and Animation
[Page 11]
Camera Space
▪Object space for the viewer, 
represented by a camera, 
used to project 3D space 
onto screen space
GAME2016 Mathematical Foundation of Game Design and Animation

[Page 12]
Camera Space Terminology
▪Frustum : the pyramid of 
space seen by the 
camera
▪Clipping : objects partially 
on screen
▪Occlusion : objects 
hidden behind another 
object
▪Visibility : inside or 
outside of frustum, 
occluded, clipped
GAME2016 Mathematical Foundation of Game Design and Animation

[Page 13]
Upright Space
▪Upright space is in a sense “halfway” between 
world space and object space
- ▪Which brings us to coordinate space 
transformations …
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 19]
Coordinate Space 
Transformations
[Page 20]
Coordinate Space Transformation
▪Two important types of transformation used to 
transform one coordinate space into another:
▪Translation
▪Changes position in space 
▪Gives new location of origin
▪Rotation 
▪Changes orientation in space 
▪Gives new directions of axes
▪Which one comes first

### Quiz Questions


**Q1: [Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 1
Coordinate spaces
©P?**
- A) GAME2016
- B) 1]
- C) Mathematical
- D) Foundation

✓ **Answer: A**

**Q2: This content is copyright protected and shall not be shared, uploaded or distribu ted?**
- A) is
- B) content
- C) copyright
- D) protected

✓ **Answer: A**

**Q3: hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Agenda
▪Why multiple coordinate spaces?**
- A) Lecturer
- B) Senior
- C) @HKBU
- D) Department

✓ **Answer: A**

**Q4: ▪Camera Space
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 3]
Why Multiple Coordinate 
Spaces?**
- A) GAME2016
- B) Space
- C) Mathematical
- D) Foundation

✓ **Answer: A**

**Q5: [Page 4]
Why Multiple Coordinate Spaces?**
- A) Why
- B) 4]
- C) Multiple
- D) Coordinate

✓ **Answer: A**

**Q6: ▪Some things become easier in the correct 
coordinate space?**
- A) become
- B) things
- C) easier
- D) in

✓ **Answer: A**

**Q7: ▪There is some historical precedent for this 
observation (next slide)?**
- A) some
- B) is
- C) historical
- D) precedent

✓ **Answer: A**

**Q8: ▪We can leave the details of transforming between 
coordinate spaces to the graphics hardware?**
- A) leave
- B) can
- C) the
- D) details

✓ **Answer: A**

### Practice Problems


**Problem 1:**
Calculate the result when applying Animation to the values 1, 1

**Solution Approach:** Refer to the Animation formula: work through step by step

**Problem 2:**
Explain how Coordinate differs from Rotation

**Solution Approach:** Consider the definitions, properties, and applications of each

**Problem 3:**
Apply Rotation to a scenario with game animation

**Solution Approach:** Break down the problem using the relevant formula or definition

### Revision Tips

- 1. Focus on understanding the core formulas and when to use them
- 2. Practice working through numerical examples
- 3. Understand the geometric or visual interpretation
- 4. Relate concepts to real-world game/animation scenarios
- 5. Create flashcards for key terms and definitions

---

## L2a - Vectors

### Overview

[Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 2
Vectors
©P. Mengoni, IMD HKBU. All Rights Reserved. This content is copyright protected and shall not be shared, uploaded or distribu ted.Dr. Paolo Mengoni
pmengoni@hkbu.edu.hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Agenda
▪Mathematical properties of vectors.
▪Geometric properties of vectors.
▪Connecting the mathematical definition with the 
geometric definition.
▪Vectors vs points.
▪Fundame

### Key Concepts

- • Vector: magnitude, direction, component
- • Animation: interpolation, keyframe, easing
- • Coordinate: cartesian, polar, spherical
- • Matrix: determinant, inverse, transpose
- • Numerical Values: 

### Formulas & Equations

```
negation = multiplying by the scalar –1
```
```
Direction = orientation
```
```
b = –(b – a)
```
```
Roman or Greek letters in italics: a, b, x, y, z, θ, α, ω,
```
```
v1 = 6, v2 = 19, v3 = 42
```
```
v = v
```
```
b = b + a
```
```
ka = b, then b1=ka1, etc
```
```
b = c, then c1 = a1 + b1, etc
```
```
b = a + (– b)
```

### Applications

- , 55mph)
▪Vectors  are used to express relative things
- ▪Scalars  are used to express absolute things
- ▪So, a vector can be used to 
represent a point
- ▪You need to deal with approximation errors and 
“aliasing”
GAME2016 Mathematical Foundation of Game Design and Animation

[Page 48]
The Distance Formula
[Page 49]
Application: Computing Distance
▪To find the geometric distance between two points 
a and b
- GAME2016 Mathematical Foundation of Game Design and Animation

[Page 53]
Sign of Dot Product
GAME2016 Mathematical Foundation of Game Design and Animation

[Page 54]
Dot Product: Geometry
▪Dot product can be used to find the angle between 
two vectors a and b

### Quiz Questions


**Q1: [Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 2
Vectors
©P?**
- A) GAME2016
- B) 1]
- C) Mathematical
- D) Foundation

✓ **Answer: A**

**Q2: This content is copyright protected and shall not be shared, uploaded or distribu ted?**
- A) is
- B) content
- C) copyright
- D) protected

✓ **Answer: A**

**Q3: hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Agenda
▪Mathematical properties of vectors?**
- A) Lecturer
- B) Senior
- C) @HKBU
- D) Department

✓ **Answer: A**

**Q4: ▪Connecting the mathematical definition with the 
geometric definition?**
- A) mathematical
- B) the
- C) definition
- D) with

✓ **Answer: A**

**Q5: ▪Fundamental vector calculations
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 3]
Mathematical Definition
and notation
[Page 4]
Vectors and Scalars
▪An “ordinary number ” is called a scalar?**
- A) calculations
- B) vector
- C) GAME2016
- D) Mathematical

✓ **Answer: A**

**Q6: ▪Algebraic definition of a vector ?**
- A) of
- B) definition
- C) a
- D) vector

✓ **Answer: A**

**Q7: ▪Vector dimension  is the number of numbers in the 
list 
▪The dimension of the vector in the example is 3?**
- A) is
- B) dimension
- C) the
- D) number

✓ **Answer: A**

**Q8: ▪Typically, we use dimension 2 for 2D work, dimension 3 
for 3D work?**
- A) use
- B) we
- C) dimension
- D) 2

✓ **Answer: A**

### Practice Problems


**Problem 1:**
Calculate the result when applying Vector to the values 1, 2

**Solution Approach:** Refer to the Vector formula: work through step by step

**Problem 2:**
Explain how Animation differs from Coordinate

**Solution Approach:** Consider the definitions, properties, and applications of each

**Problem 3:**
Apply Coordinate to a scenario with game animation

**Solution Approach:** Break down the problem using the relevant formula or definition

### Revision Tips

- 1. Focus on understanding the core formulas and when to use them
- 2. Practice working through numerical examples
- 3. Understand the geometric or visual interpretation
- 4. Relate concepts to real-world game/animation scenarios
- 5. Create flashcards for key terms and definitions

---

## L2b- Random Numbers

### Overview

[Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 2
Random numbers at a glance
©P. Mengoni, IMD HKBU. All Rights Reserved. This content is copyright protected and shall not be shared, uploaded or distribu ted.Dr. Paolo Mengoni
pmengoni@hkbu.edu.hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Random Number Generators
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 3]
Random Number Generators
▪Random number generation is a method 

### Key Concepts

- • Animation: interpolation, keyframe, easing
- • Numerical Values: 

### Formulas & Equations


### Applications

- ▪Random Number Generators (RNGs) have applications 
in a wide range of different fields such as:
▪Cryptography : RNGs ensure that encryption keys are 
unpredictable and secure
- ▪Uncorrelated 
▪with what you're interested in
▪Quantum computer systems are the only truly 
random
▪As far as we know
▪Pseudo RNGs are what we can achieve with normal 
computers
▪It’s random enough for your applications
▪Sometimes we want repeatability from a random 
number generator (seeding)
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 5]
Pseudo RNGs
▪PRNGs usually generate very long sequences of 
random numbers
- , the commonly used Mersenne Twister 
MT19937 has a sequence length of 219937-1
- ▪The Mersenne Twister is a widely used PRNG, the 
name comes from the period length which is chosen 
to be a Mersenne Prime Number
- ▪The commonly used MT19937 algorithm stores and 
generates 624 numbers at a time and can extract them 
one by one

### Quiz Questions


**Q1: [Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 2
Random numbers at a glance
©P?**
- A) GAME2016
- B) 1]
- C) Mathematical
- D) Foundation

✓ **Answer: A**

**Q2: This content is copyright protected and shall not be shared, uploaded or distribu ted?**
- A) is
- B) content
- C) copyright
- D) protected

✓ **Answer: A**

**Q3: hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Random Number Generators
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 3]
Random Number Generators
▪Random number generation is a method of producing 
a sequence of numbers that lack any discernible 
pattern?**
- A) Lecturer
- B) Senior
- C) @HKBU
- D) Department

✓ **Answer: A**

**Q4: ▪Random Number Generators (RNGs) have applications 
in a wide range of different fields such as?**
- A) Generators
- B) Number
- C) (RNGs)
- D) have

✓ **Answer: A**

**Q5: ▪Computer Simulations ?**
- A) :
- B) Simulations
- C) RNGs
- D) help

✓ **Answer: A**

**Q6: ▪Video Games ?**
- A) :
- B) Games
- C) RNGs
- D) play

✓ **Answer: A**

**Q7: This enhances the gaming experience by 
making each playthrough unique and engaging?**
- A) the
- B) enhances
- C) gaming
- D) experience

✓ **Answer: A**

**Q8: GAME2016 Mathematical Foundation of Game Design and Animation
[Page 4]
What is Random?**
- A) Foundation
- B) Mathematical
- C) of
- D) Game

✓ **Answer: A**

### Practice Problems


**Problem 1:**
Calculate the result when applying Animation to the values 1, 2

**Solution Approach:** Refer to the Animation formula: work through step by step

**Problem 2:**
Explain how Numerical Values differs from Animation

**Solution Approach:** Consider the definitions, properties, and applications of each

**Problem 3:**
Apply Animation to a scenario with game animation

**Solution Approach:** Break down the problem using the relevant formula or definition

### Revision Tips

- 1. Focus on understanding the core formulas and when to use them
- 2. Practice working through numerical examples
- 3. Understand the geometric or visual interpretation
- 4. Relate concepts to real-world game/animation scenarios
- 5. Create flashcards for key terms and definitions

---

## L3 - Matrices

### Overview

[Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 3
Matrices
©P. Mengoni, IMD HKBU. All Rights Reserved. This content is copyright protected and shall not be shared, uploaded or distribu ted.Dr. Paolo Mengoni
pmengoni@hkbu.edu.hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Agenda
▪Basic properties and operations of matrices 
▪Mathematical perspective. 
▪Geometrical perspective.
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 3]

### Key Concepts

- • Matrix: determinant, inverse, transpose
- • Animation: interpolation, keyframe, easing
- • Vector: magnitude, direction, component
- • Transformation: translation, scaling, shear
- • Coordinate: cartesian, polar, spherical
- • Rotation: quaternion, euler angles, axis-angle
- • Numerical Values: 

### Formulas & Equations

```
cr = 0
```
```
C = A(BC)
```
```
v = A(Bv)
```
```
B =A(kB)
```
```
C = AB
```
```
T = M for all
```
```
T = BTAT
```
```
C = [cij], where cij is the dot product of the ith
```
```
M = vM + wM
```
```
equation as
```

### Applications


### Quiz Questions


**Q1: [Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 3
Matrices
©P?**
- A) GAME2016
- B) 1]
- C) Mathematical
- D) Foundation

✓ **Answer: A**

**Q2: This content is copyright protected and shall not be shared, uploaded or distribu ted?**
- A) is
- B) content
- C) copyright
- D) protected

✓ **Answer: A**

**Q3: hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Agenda
▪Basic properties and operations of matrices 
▪Mathematical perspective?**
- A) Lecturer
- B) Senior
- C) @HKBU
- D) Department

✓ **Answer: A**

**Q4: GAME2016 Mathematical Foundation of Game Design and Animation
[Page 3]
GAME2016 Mathematical Foundation of Game Design and Animation

[Page 4]
Matrix?**
- A) Foundation
- B) Mathematical
- C) of
- D) Game

✓ **Answer: A**

**Q5: ▪Matrix dimension  is the width  and height  of the 
table, w x h?**
- A) is
- B) dimension
- C) the
- D) width

✓ **Answer: A**

**Q6: ▪Typically , we use dimensions 2 x 2 for 2D work, and 
3 x 3 for 3D work?**
- A) we
- B) ,
- C) use
- D) dimensions

✓ **Answer: A**

**Q7: ▪We’ll find a use for 4 x 4 matrices also?**
- A) a
- B) find
- C) use
- D) for

✓ **Answer: A**

**Q8: GAME2016 Mathematical Foundation of Game Design and Animation
[Page 6]
Matrix Components
▪Entries are numbered by row and column
▪eg?**
- A) Foundation
- B) Mathematical
- C) of
- D) Game

✓ **Answer: A**

### Practice Problems


**Problem 1:**
Calculate the result when applying Matrix to the values 1, 3

**Solution Approach:** Refer to the Matrix formula: work through step by step

**Problem 2:**
Explain how Animation differs from Vector

**Solution Approach:** Consider the definitions, properties, and applications of each

**Problem 3:**
Apply Vector to a scenario with game animation

**Solution Approach:** Break down the problem using the relevant formula or definition

### Revision Tips

- 1. Focus on understanding the core formulas and when to use them
- 2. Practice working through numerical examples
- 3. Understand the geometric or visual interpretation
- 4. Relate concepts to real-world game/animation scenarios
- 5. Create flashcards for key terms and definitions

---

## L4a - Matrices and linear transformations

### Overview

[Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 4
Matrices and Linear Transformations
©P. Mengoni, IMD HKBU. All Rights Reserved. This content is copyright protected and shall not be shared, uploaded or distribu ted.Dr. Paolo Mengoni
pmengoni@hkbu.edu.hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Agenda
▪Introduction to matrices for primitive linear 
transformations 
▪Rotation
▪Scaling
▪Orthographic projection
▪Reflection
▪Shearing
▪Complex tra

### Key Concepts

- • Animation: interpolation, keyframe, easing
- • Matrix: determinant, inverse, transpose
- • Rotation: quaternion, euler angles, axis-angle
- • Coordinate: cartesian, polar, spherical
- • Transformation: translation, scaling, shear
- • Vector: magnitude, direction, component
- • Numerical Values: 

### Formulas & Equations

```
formula
▪Details in the textbook
```

### Applications

- ▪For game programmers it is not used very often
- GAME2016 Mathematical Foundation of Game Design and Animation
[Page 27]
Projection Matrices
▪For completeness, we present the matrices for 
these transformations:
GAME2016 Mathematical Foundation of Game Design and Animation

[Page 28]
Reflection
[Page 29]
Reflection
GAME2016 Mathematical Foundation of Game Design and Animation

[Page 30]
Reflection in 2D
▪Reflection can be accomplished by applying a scale 
factor of -1

### Quiz Questions


**Q1: [Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 4
Matrices and Linear Transformations
©P?**
- A) GAME2016
- B) 1]
- C) Mathematical
- D) Foundation

✓ **Answer: A**

**Q2: This content is copyright protected and shall not be shared, uploaded or distribu ted?**
- A) is
- B) content
- C) copyright
- D) protected

✓ **Answer: A**

**Q3: hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Agenda
▪Introduction to matrices for primitive linear 
transformations 
▪Rotation
▪Scaling
▪Orthographic projection
▪Reflection
▪Shearing
▪Complex transformations and matrix 
multiplication
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 3]
Matrices and Linear 
Transformations
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 4]
GAME2016 Mathematical Foundation of Game Design and Animation

[Page 5]
Rotation
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 6]
Reminder?**
- A) Lecturer
- B) Senior
- C) @HKBU
- D) Department

✓ **Answer: A**

**Q4: ▪Given an arbitrary matrix, visualize the 
transformation by its effect on the standard basis 
vectors – the rows of the matrix?**
- A) arbitrary
- B) an
- C) matrix,
- D) visualize

✓ **Answer: A**

**Q5: ▪Given an arbitrary linear transformation, create 
the matrix by visualizing what it does to the 
standard basis vectors and using that for the rows 
of the matrix?**
- A) arbitrary
- B) an
- C) linear
- D) transformation,

✓ **Answer: A**

**Q6: GAME2016 Mathematical Foundation of Game Design and Animation
[Page 7]
2D Rotation Around Point
GAME2016 Mathematical Foundation of Game Design and AnimationBefore After

[Page 8]
It’s All About Rotating Basis Vectors?**
- A) Foundation
- B) Mathematical
- C) of
- D) Game

✓ **Answer: A**

**Q7: GAME2016 Mathematical Foundation of Game Design and Animation

[Page 9]
Construct Matrix from Basis Vectors
GAME2016 Mathematical Foundation of Game Design and Animation

[Page 10]
3D Rotation About Cardinal Axis
▪In 3D, rotation occurs about an axis rather than a 
point as in 2D?**
- A) Foundation
- B) Mathematical
- C) of
- D) Game

✓ **Answer: A**

**Q8: ▪The most common type of rotation is a simple 
rotation about one of the cardinal axes?**
- A) common
- B) most
- C) type
- D) of

✓ **Answer: A**

### Practice Problems


**Problem 1:**
Calculate the result when applying Animation to the values 1, 4

**Solution Approach:** Refer to the Animation formula: work through step by step

**Problem 2:**
Explain how Matrix differs from Rotation

**Solution Approach:** Consider the definitions, properties, and applications of each

**Problem 3:**
Apply Rotation to a scenario with game animation

**Solution Approach:** Break down the problem using the relevant formula or definition

### Revision Tips

- 1. Focus on understanding the core formulas and when to use them
- 2. Practice working through numerical examples
- 3. Understand the geometric or visual interpretation
- 4. Relate concepts to real-world game/animation scenarios
- 5. Create flashcards for key terms and definitions

---

## L4b - Classes of transformations at a glance

### Overview

[Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 4
Classes of transformations at a glance
©P. Mengoni, IMD HKBU. All Rights Reserved. This content is copyright protected and shall not be shared, uploaded or distribu ted.Dr. Paolo Mengoni
pmengoni@hkbu.edu.hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Classes of Transformations
▪Linear transformations
▪Affine transformations
▪Invertible transformations
▪Angle preserving transformations
▪Orthogona

### Key Concepts

- • Transformation: translation, scaling, shear
- • Animation: interpolation, keyframe, easing
- • Matrix: determinant, inverse, transpose
- • Vector: magnitude, direction, component
- • Rotation: quaternion, euler angles, axis-angle
- • Numerical Values: 

### Formulas & Equations

```
M = k(aM) = kF(a)
```
```
M = aM + bM = F(a) + F(b)
```

### Applications


### Quiz Questions


**Q1: [Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 4
Classes of transformations at a glance
©P?**
- A) GAME2016
- B) 1]
- C) Mathematical
- D) Foundation

✓ **Answer: A**

**Q2: This content is copyright protected and shall not be shared, uploaded or distribu ted?**
- A) is
- B) content
- C) copyright
- D) protected

✓ **Answer: A**

**Q3: hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Classes of Transformations
▪Linear transformations
▪Affine transformations
▪Invertible transformations
▪Angle preserving transformations
▪Orthogonal transformations
▪Rigid body transformations
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 3]
Disclaimer
▪When we discuss transformations in general, we make 
use of the synonymous terms mapping  or function?**
- A) Lecturer
- B) Senior
- C) @HKBU
- D) Department

✓ **Answer: A**

**Q4: ▪A mapping is simply a rule that takes an input and 
produces an output?**
- A) is
- B) mapping
- C) simply
- D) a

✓ **Answer: A**

**Q5: ▪We denote that the mapping F maps a to b by writing F(a) = b?**
- A) that
- B) denote
- C) the
- D) mapping

✓ **Answer: A**

**Q6: (Read “ F of a equals b?**
- A) F
- B) “
- C) of
- D) a

✓ **Answer: A**

**Q7: ”) 
▪We are mostly interested in the transformations that 
can be expressed as matrix multiplication, but others 
are possible?**
- A) are
- B) ▪We
- C) mostly
- D) interested

✓ **Answer: A**

**Q8: ▪In this section we introduce the determinant of a 
matrix?**
- A) section
- B) this
- C) we
- D) introduce

✓ **Answer: A**

### Practice Problems


**Problem 1:**
Calculate the result when applying Transformation to the values 1, 4

**Solution Approach:** Refer to the Transformation formula: work through step by step

**Problem 2:**
Explain how Animation differs from Matrix

**Solution Approach:** Consider the definitions, properties, and applications of each

**Problem 3:**
Apply Matrix to a scenario with game animation

**Solution Approach:** Break down the problem using the relevant formula or definition

### Revision Tips

- 1. Focus on understanding the core formulas and when to use them
- 2. Practice working through numerical examples
- 3. Understand the geometric or visual interpretation
- 4. Relate concepts to real-world game/animation scenarios
- 5. Create flashcards for key terms and definitions

---

## L5a Matrix determinant - inverse - orthogonalization

### Overview

[Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 5
Course Overview
©P. Mengoni, IMD HKBU. All Rights Reserved. This content is copyright protected and shall not be shared, uploaded or distribu ted.Dr. Paolo Mengoni
pmengoni@hkbu.edu.hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Agenda
▪Determinant of a matrix
▪Inverse of a matrix
▪With adjoint matrix
▪Orthogonal matrices and orthogonalization
GAME2016 Mathematical Foundation of Game Design and A

### Key Concepts

- • Matrix: determinant, inverse, transpose
- • Animation: interpolation, keyframe, easing
- • Vector: magnitude, direction, component
- • Transformation: translation, scaling, shear
- • Rotation: quaternion, euler angles, axis-angle
- • Coordinate: cartesian, polar, spherical
- • Numerical Values: 

### Formulas & Equations

```
r3
= 0
```
```
MMT = I
```
```
M = I
```
```
MT = M-1
```
```
vM = 0 is true only when v = 0
```
```
vI = v
```
```
r2
= 0
```

### Applications

- ▪The determinant of the matrix can also be used to 
help classify the type of transformation represented by 
a matrix
- ▪The determinant of a singular matrix is zero
▪Checking the magnitude of the determinant is the 
most commonly used test for invertibility
▪it’s easier and quicker
- GAME2016 Mathematical Foundation of Game Design and Animation
[Page 34]
Example of Matrix Inverse
▪If:
GAME2016 Mathematical Foundation of Game Design and Animation

[Page 35]
Gaussian Elimination
▪There are other techniques that can be used to compute 
the inverse of a matrix, such as Gaussian elimination
- ▪For arbitrary smaller order matrices like 2 x 2, 3 x 3, and 4 x 
4 used most often in geometric applications, the classical 
adjoint method is faster

### Quiz Questions


**Q1: [Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 5
Course Overview
©P?**
- A) GAME2016
- B) 1]
- C) Mathematical
- D) Foundation

✓ **Answer: A**

**Q2: This content is copyright protected and shall not be shared, uploaded or distribu ted?**
- A) is
- B) content
- C) copyright
- D) protected

✓ **Answer: A**

**Q3: hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Agenda
▪Determinant of a matrix
▪Inverse of a matrix
▪With adjoint matrix
▪Orthogonal matrices and orthogonalization
GAME2016 Mathematical Foundation of Game Design and Animation

[Page 3]
Determinant of a Matrix
[Page 4]
Determinant
▪Determinant is defined for square matrices?**
- A) Lecturer
- B) Senior
- C) @HKBU
- D) Department

✓ **Answer: A**

**Q4: ▪Denoted | M| or det M?**
- A) M|
- B) |
- C) or
- D) det

✓ **Answer: A**

**Q5: ▪Determinant of a 2x2 matrix is
GAME2016 Mathematical Foundation of Game Design and Animation

[Page 5]
2 x 2 Example
GAME2016 Mathematical Foundation of Game Design and Animation

[Page 6]
3 x 3 Determinant
GAME2016 Mathematical Foundation of Game Design and Animation

[Page 7]
3 x 3 Example
GAME2016 Mathematical Foundation of Game Design and Animation

[Page 8]
Triple Product
▪If we interpret the rows of a 3x3 matrix as three 
vectors , then the determinant  of the matrix is 
equivalent to the so-called triple product of the 
three vectors ?**
- A) a
- B) of
- C) 2x2
- D) matrix

✓ **Answer: A**

**Q6: ▪Consider the matrix obtained by deleting row i and 
column j from M?**
- A) matrix
- B) the
- C) obtained
- D) by

✓ **Answer: A**

**Q7: ▪This matrix size will obviously be r-1 x c-1?**
- A) size
- B) matrix
- C) will
- D) obviously

✓ **Answer: A**

**Q8: ▪The determinant of this submatrix , denoted M{ij} is 
known as a minor  of M?**
- A) of
- B) determinant
- C) this
- D) submatrix

✓ **Answer: A**

### Practice Problems


**Problem 1:**
Calculate the result when applying Matrix to the values 1, 5

**Solution Approach:** Refer to the Matrix formula: work through step by step

**Problem 2:**
Explain how Animation differs from Vector

**Solution Approach:** Consider the definitions, properties, and applications of each

**Problem 3:**
Apply Vector to a scenario with game animation

**Solution Approach:** Break down the problem using the relevant formula or definition

### Revision Tips

- 1. Focus on understanding the core formulas and when to use them
- 2. Practice working through numerical examples
- 3. Understand the geometric or visual interpretation
- 4. Relate concepts to real-world game/animation scenarios
- 5. Create flashcards for key terms and definitions

---

## L6a - Homogeneous Matrices

### Overview

[Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 6
Homogeneous Matrices and General Affine Transformations
©P. Mengoni, IMD HKBU. All Rights Reserved. This content is copyright protected and shall not be shared, uploaded or distribu ted.Dr. Paolo Mengoni
pmengoni@hkbu.edu.hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Agenda
▪Homogeneous matrices
▪From vectors to 4 ×4 matrices
▪General Affine Transformations in 3D
▪Perspective projection at a gla

### Key Concepts

- • Animation: interpolation, keyframe, easing
- • Matrix: determinant, inverse, transpose
- • Transformation: translation, scaling, shear
- • Vector: magnitude, direction, component
- • Rotation: quaternion, euler angles, axis-angle
- • Coordinate: cartesian, polar, spherical
- • Numerical Values: 

### Formulas & Equations

```
z = -d
```
```
vRT = v(RT) = vM
```
```
w = ax + b
```
```
equation is w = qx/p
```
```
w = 1 and w = 0 so far
```
```
M = RT, so
```
```
w = 1, x = p/q
```
```
t = [Δx, Δy, Δz]
```
```
w = 1
```
```
w = 1 along a line to the origin, which turns out
```

### Applications

- Let M = RT, so
v = vRT = v(RT) = vM
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 25]
GAME2016 Mathematical Foundation of Game Design and Animation

[Page 26]
In Reverse
▪Applying this information in reverse, we can take a 
4 x 4 matrix M and separate it into a linear 
transformation portion, and a translation portion
- GAME2016 Mathematical Foundation of Game Design and Animation
[Page 36]
Perspective Projection
[Page 37]
Projections
▪We’ve only used w = 1 and w = 0 so far
- It will apply a normalizing scale factor such 
that w = 1 at the far clip plane
- Values used for 
depth buffering will be distributed 
appropriately and maximize the precision

### Quiz Questions


**Q1: [Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 6
Homogeneous Matrices and General Affine Transformations
©P?**
- A) GAME2016
- B) 1]
- C) Mathematical
- D) Foundation

✓ **Answer: A**

**Q2: This content is copyright protected and shall not be shared, uploaded or distribu ted?**
- A) is
- B) content
- C) copyright
- D) protected

✓ **Answer: A**

**Q3: hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Agenda
▪Homogeneous matrices
▪From vectors to 4 ×4 matrices
▪General Affine Transformations in 3D
▪Perspective projection at a glance
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 3]
4×4 Homogenous Matrices
[Page 4]
Why Homogenous Matrices?**
- A) Lecturer
- B) Senior
- C) @HKBU
- D) Department

✓ **Answer: A**

**Q4: ▪It will let us handle translation with a matrix 
transformation?**
- A) let
- B) will
- C) us
- D) handle

✓ **Answer: A**

**Q5: ▪Single framework to work with when developing a 
software system?**
- A) to
- B) framework
- C) work
- D) with

✓ **Answer: A**

**Q6: GAME2016 Mathematical Foundation of Game Design and Animation
[Page 5]
Homogenous Coordinates
▪Extend 3D into 4D?**
- A) Foundation
- B) Mathematical
- C) of
- D) Game

✓ **Answer: A**

**Q7: ▪The 4th dimension is not “time”?**
- A) dimension
- B) 4th
- C) is
- D) not

✓ **Answer: A**

**Q8: ▪The 4th dimension is really just a trick to help the 
math work out
▪The 4th dimension is called w?**
- A) dimension
- B) 4th
- C) is
- D) really

✓ **Answer: A**

### Practice Problems


**Problem 1:**
Calculate the result when applying Animation to the values 1, 6

**Solution Approach:** Refer to the Animation formula: work through step by step

**Problem 2:**
Explain how Matrix differs from Transformation

**Solution Approach:** Consider the definitions, properties, and applications of each

**Problem 3:**
Apply Transformation to a scenario with game animation

**Solution Approach:** Break down the problem using the relevant formula or definition

### Revision Tips

- 1. Focus on understanding the core formulas and when to use them
- 2. Practice working through numerical examples
- 3. Understand the geometric or visual interpretation
- 4. Relate concepts to real-world game/animation scenarios
- 5. Create flashcards for key terms and definitions

---

## L6b - 2D Polar Coordinate Systems

### Overview

[Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 6
Polar coordinate systems
©P. Mengoni, IMD HKBU. All Rights Reserved. This content is copyright protected and shall not be shared, uploaded or distribu ted.Dr. Paolo Mengoni
pmengoni@hkbu.edu.hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Agenda
▪Why Use Polar Coordinates?
▪Some examples where polar coordinates are preferable 
to Cartesian coordinates. 
▪2D polar coordinates.
GAME2016 Mathematical

### Key Concepts

- • Animation: interpolation, keyframe, easing
- • Coordinate: cartesian, polar, spherical
- • Rotation: quaternion, euler angles, axis-angle
- • Numerical Values: 

### Formulas & Equations

```
also ambiguous. Clearly r = 0, but what value of θ
```
```
▪Computing polar coordinates ( r, θ) from Cartesian
```
```
y = 0 using
```
```
all of the polar coordinates that are aliases for ( r, θ)
```
```
▪A polar coordinate pair (r, θ) is in canonical form if
```
```
angle is usually called θ.
```
```
1.If r = 0, then assign θ = 0.
```
```
x = r cos θ
```
```
show lines of constant θ, consisting of points that
```
```
3.If θ ≤ 180°, then add 360 ° until θ >  –180°
```

### Applications

- GAME2016 Mathematical Foundation of Game Design and Animation
[Page 14]
Aliasing
▪In fact, for any given point, there are infinitely many 
polar coordinate pairs that can be used to describe 
that point

### Quiz Questions


**Q1: [Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 6
Polar coordinate systems
©P?**
- A) GAME2016
- B) 1]
- C) Mathematical
- D) Foundation

✓ **Answer: A**

**Q2: This content is copyright protected and shall not be shared, uploaded or distribu ted?**
- A) is
- B) content
- C) copyright
- D) protected

✓ **Answer: A**

**Q3: hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Agenda
▪Why Use Polar Coordinates?**
- A) Lecturer
- B) Senior
- C) @HKBU
- D) Department

✓ **Answer: A**

**Q4: ▪Some examples where polar coordinates are preferable 
to Cartesian coordinates?**
- A) where
- B) examples
- C) polar
- D) coordinates

✓ **Answer: A**

**Q5: GAME2016 Mathematical Foundation of Game Design and Animation

[Page 3]
Why Use Polar Coordinates?**
- A) Foundation
- B) Mathematical
- C) of
- D) Game

✓ **Answer: A**

**Q6: [Page 4]
Why Use Polar Coordinates?**
- A) Why
- B) 4]
- C) Use
- D) Polar

✓ **Answer: A**

**Q7: ▪They’re better for humans ( eg?**
- A) for
- B) better
- C) humans
- D) (

✓ **Answer: A**

**Q8: “I live 22 miles NNE 
of Dallas, TX”)
▪They’re useful in video games
▪Cameras 
▪Turrets 
▪Position the assassin’s arms
▪Sometimes we even use 3D spherical coordinates 
for locating things on the globe
▪Latitude and longitude?**
- A) 22
- B) live
- C) miles
- D) NNE

✓ **Answer: A**

### Practice Problems


**Problem 1:**
Calculate the result when applying Animation to the values 1, 6

**Solution Approach:** Refer to the Animation formula: work through step by step

**Problem 2:**
Explain how Coordinate differs from Rotation

**Solution Approach:** Consider the definitions, properties, and applications of each

**Problem 3:**
Apply Rotation to a scenario with game animation

**Solution Approach:** Break down the problem using the relevant formula or definition

### Revision Tips

- 1. Focus on understanding the core formulas and when to use them
- 2. Practice working through numerical examples
- 3. Understand the geometric or visual interpretation
- 4. Relate concepts to real-world game/animation scenarios
- 5. Create flashcards for key terms and definitions

---

## L6c - 3D Polar Coordinate Systems

### Overview

[Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 6
Polar coordinate systems
©P. Mengoni, IMD HKBU. All Rights Reserved. This content is copyright protected and shall not be shared, uploaded or distribu ted.Dr.Paolo Mengoni
pmengoni@hkbu.edu.hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Agenda
▪3D polar space.
GAME2016 Mathematical Foundation of Game Design and Animation [Page 3]
3D Polar Space
[Page 4]
3D Polar Space
There are two kinds in commo

### Key Concepts

- • Animation: interpolation, keyframe, easing
- • Coordinate: cartesian, polar, spherical
- • Rotation: quaternion, euler angles, axis-angle
- • Numerical Values: 

### Formulas & Equations

```
h= atan2( x, z)
```
```
p= 180 °–p
```
```
inclination, 90 °–φ.
```
```
▪It would be nicer if the 2D polar coordinates ( r, θ) were
```
```
▪The horizontal angle θis known as the azimuth , and φ
```
```
▪In fact, assigning φ = 0 puts us in the awkward situation of
```
```
coordinates ( r, θ, z), start by
```
```
2.Rotate your arm downward by the angle φ.
```
```
y= rsin φsinθ
```
```
▪But ( r, θ, 0) don't correspond to ( r, θ) as we'd like.
```

### Applications

- GAME2016 Mathematical Foundation of Game Design and Animation
[Page 12]
Visualizing Polar Coordinates
▪The spherical coordinate system described in the 
previous section is the traditional right -handed 
system used by “math people
- No offense to the Greeks, but θand φtake a little 
while to get used to
- ” 
▪Wouldn't it be great if the symbols we used to 
denote the angles were similarly short for English 
words, rather than completely arbitrary Greek 
symbols
- For a better comparison it would be nice if the 
two angles for spherical coordinates were the same 
as the first two angles we will use for Euler angles
▪Which are used to describe orientation in 3D
- ▪Trivial, it’s caused by the cyclic nature of angular 
measurements

### Quiz Questions


**Q1: [Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 6
Polar coordinate systems
©P?**
- A) GAME2016
- B) 1]
- C) Mathematical
- D) Foundation

✓ **Answer: A**

**Q2: This content is copyright protected and shall not be shared, uploaded or distribu ted?**
- A) is
- B) content
- C) copyright
- D) protected

✓ **Answer: A**

**Q3: hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Agenda
▪3D polar space?**
- A) Lecturer
- B) Senior
- C) @HKBU
- D) Department

✓ **Answer: A**

**Q4: GAME2016 Mathematical Foundation of Game Design and Animation

[Page 3]
3D Polar Space
[Page 4]
3D Polar Space
There are two kinds in common use?**
- A) Foundation
- B) Mathematical
- C) of
- D) Game

✓ **Answer: A**

**Q5: Cylindrical coordinates 
▪1 angle and 2 distances
2?**
- A) ▪1
- B) coordinates
- C) angle
- D) and

✓ **Answer: A**

**Q6: Spherical coordinates 
▪2 angles and 1 distance
GAME2016 Mathematical Foundation of Game Design and Animation

[Page 5]
3D Cylindrical Space
▪To locate the point 
described by cylindrical 
coordinates ( r, θ, z), start by 
processing rand θjust like 
we would for 2D polar 
coordinates, and then 
move up or down the zaxis 
by z?**
- A) ▪2
- B) coordinates
- C) angles
- D) and

✓ **Answer: A**

**Q7: GAME2016 Mathematical Foundation of Game Design and Animation

[Page 6]
3D Spherical Coordinates
▪As with 2D polar coordinates, 3D spherical coordinates 
also work by defining a direction and distance?**
- A) Foundation
- B) Mathematical
- C) of
- D) Game

✓ **Answer: A**

**Q8: ▪The only difference is that in 3D it takes two angles to 
define a direction?**
- A) difference
- B) only
- C) is
- D) that

✓ **Answer: A**

### Practice Problems


**Problem 1:**
Calculate the result when applying Animation to the values 1, 6

**Solution Approach:** Refer to the Animation formula: work through step by step

**Problem 2:**
Explain how Coordinate differs from Rotation

**Solution Approach:** Consider the definitions, properties, and applications of each

**Problem 3:**
Apply Rotation to a scenario with game animation

**Solution Approach:** Break down the problem using the relevant formula or definition

### Revision Tips

- 1. Focus on understanding the core formulas and when to use them
- 2. Practice working through numerical examples
- 3. Understand the geometric or visual interpretation
- 4. Relate concepts to real-world game/animation scenarios
- 5. Create flashcards for key terms and definitions

---

## L7 - Rotation in Three Dimensions -All forms

### Overview

[Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 7
Rotation in Three Dimensions
©P. Mengoni, IMD HKBU. All Rights Reserved. This content is copyright protected and shall not be shared, uploaded or distribu ted.Dr. Paolo Mengoni
pmengoni@hkbu.edu.hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Agenda
▪Orientation, direction, and angular displacement.
▪How to express orientation:
▪Matrix form
▪Euler angles
▪The axis -angle and exponential map forms


### Key Concepts

- • Animation: interpolation, keyframe, easing
- • Matrix: determinant, inverse, transpose
- • Rotation: quaternion, euler angles, axis-angle
- • Vector: magnitude, direction, component
- • Coordinate: cartesian, polar, spherical
- • Transformation: translation, scaling, shear
- • Numerical Values: 

### Formulas & Equations

```
v1 = [ x1 y1 z1 ] and v2 = [ x2 y2 z2 ], then
```
```
a = a1 – a0
```
```
orientation, when θ = 0 and any axis may be used.
```
```
i= −1
```
```
Q = [ cos /2      sin /2 n ]
```
```
t = ast, do not apply to quaternions
```
```
q = [ w ( x y z ) ]
```
```
i.e. θ = 𝐞, and
```
```
lerp( a0, a1, t) = a0 + t.Δa
```
```
q = [ w v ],
```

### Applications

- GAME2016 Mathematical Foundation of Game Design and Animation
[Page 10]
Example
▪We've seen how a matrix can 
be used  to transform points 
from one coordinate space 
to another
- ▪In the figure, the matrix in 
the upper right hand  corner 
can be used to rotate points 
from the object space of the 
jet into upright space
- GAME2016 Mathematical Foundation of Game Design and Animation

[Page 14]
Direction Cosines Matrix
▪The matrix of direction cosines (dot products) of 
each pair of basis vectors, is constructed as 
follows:
▪These axes can be interpreted as geometric 
entities
▪Independent from coordinates used to describe the 
axes, the rotation matrix will be the same
- GAME2016 Mathematical Foundation of Game Design and Animation
[Page 22]
Advantages of Matrix Form 2
Format used by graphics APIs
- ▪For example, applying a large number of  incremental changes 
to an orientation leads to large number of matrix 
multiplications which leads to errors due to the limited 
floating point  precision

### Quiz Questions


**Q1: [Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 7
Rotation in Three Dimensions
©P?**
- A) GAME2016
- B) 1]
- C) Mathematical
- D) Foundation

✓ **Answer: A**

**Q2: This content is copyright protected and shall not be shared, uploaded or distribu ted?**
- A) is
- B) content
- C) copyright
- D) protected

✓ **Answer: A**

**Q3: hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Agenda
▪Orientation, direction, and angular displacement?**
- A) Lecturer
- B) Senior
- C) @HKBU
- D) Department

✓ **Answer: A**

**Q4: ▪How to express orientation?**
- A) express
- B) to
- C) orientation:
- D) ▪Matrix

✓ **Answer: A**

**Q5: ▪How to choose representation
▪Quick note on conversion
GAME2016 Mathematical Foundation of Game Design and Animation

[Page 3]
What Exactly is “Orientation”?**
- A) choose
- B) to
- C) representation
- D) ▪Quick

✓ **Answer: A**

**Q6: GAME2016 Mathematical Foundation of Game Design and Animation
[Page 4]
Orientation
▪What is orientation?**
- A) Foundation
- B) Mathematical
- C) of
- D) Game

✓ **Answer: A**

**Q7: ▪A vector specifies direction, but it can also be 
twisted?**
- A) specifies
- B) vector
- C) direction,
- D) but

✓ **Answer: A**

**Q8: GAME2016 Mathematical Foundation of Game Design and Animation

[Page 5]
This is Important Because
▪Twisting an object changes its orientation?**
- A) Foundation
- B) Mathematical
- C) of
- D) Game

✓ **Answer: A**

### Practice Problems


**Problem 1:**
Calculate the result when applying Animation to the values 1, 7

**Solution Approach:** Refer to the Animation formula: work through step by step

**Problem 2:**
Explain how Matrix differs from Rotation

**Solution Approach:** Consider the definitions, properties, and applications of each

**Problem 3:**
Apply Rotation to a scenario with game animation

**Solution Approach:** Break down the problem using the relevant formula or definition

### Revision Tips

- 1. Focus on understanding the core formulas and when to use them
- 2. Practice working through numerical examples
- 3. Understand the geometric or visual interpretation
- 4. Relate concepts to real-world game/animation scenarios
- 5. Create flashcards for key terms and definitions

---

## L9 - Pendulum, Circular, Harmonic motion

### Overview

[Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 9
Circular, Harmonic, and Pendulum Motion
©P. Mengoni, IMD HKBU. All Rights Reserved. This content is copyright protected and shall not be shared, uploaded or distribu ted.Dr. Paolo Mengoni
pmengoni@hkbu.edu.hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Agenda
▪Understanding Circular Motion
▪Exploring Harmonic Motion
▪Analyzing  Pendulum Motion
▪Integrating Motion Types in Game Design
GAME2016 Mat

### Key Concepts

- • Animation: interpolation, keyframe, easing
- • Harmonic: oscillation, frequency, amplitude
- • Rotation: quaternion, euler angles, axis-angle
- • Numerical Values: 

### Formulas & Equations


### Applications

- These principles are used to create 
realistic object behaviors in games
- GAME2016 Mathematical Foundation of Game Design and Animation
[Page 17]
Analyzing  Pendulum Motion
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 18]
Principles of Pendulum Motion
▪Oscillation Dynamics
▪Pendulum motion is an example of 
simple harmonic motion
▪The restoring force is proportional to 
the displacement
▪This leads to predictable oscillations 
that can be modeled mathematically
▪Energy Conservation
▪The pendulum's motion illustrates 
the conversion between potential 
and kinetic energy
▪Maximum potential energy at the 
highest points
▪Maximum kinetic energy at the 
lowest point
GAME2016 Mathematical Foundation of Game Design and Animation

[Page 19]
Pendulum Motion Essentials
Component Description Game Application
Bob Mass at the end of 
the pendulumSwinging obstacles or 
collectibles
String/Rod Connects bob to 
pivot pointGrappling hooks, swing 
mechanics
Amplitude Maximum swing 
angleDifficulty adjustment in 
pendulum puzzles
Period Time for one 
complete swingTiming challenges in 
platformers
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 20]
Pendulums in Games and Animation
▪Puzzle Elements
▪Pendulums create timing -based 
puzzles
- ▪Used for realistic swinging actions, 
like grappling hooks or vines

### Quiz Questions


**Q1: [Page 1]
GAME2016
Mathematical Foundation of Game 
Design and Animation
Lecture 9
Circular, Harmonic, and Pendulum Motion
©P?**
- A) GAME2016
- B) 1]
- C) Mathematical
- D) Foundation

✓ **Answer: A**

**Q2: This content is copyright protected and shall not be shared, uploaded or distribu ted?**
- A) is
- B) content
- C) copyright
- D) protected

✓ **Answer: A**

**Q3: hk
Senior Lecturer @HKBU Department of Interactive Media
[Page 2]
Agenda
▪Understanding Circular Motion
▪Exploring Harmonic Motion
▪Analyzing  Pendulum Motion
▪Integrating Motion Types in Game Design
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 3]
Circular, Harmonic, and 
Pendulum Motion in Game 
Design and Animation
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 4]
Understanding Circular 
Motion
GAME2016 Mathematical Foundation of Game Design and Animation
[Page 5]
Understanding Circular Motion
▪Realism
▪Accurate physical motions create immersive game 
worlds?**
- A) Lecturer
- B) Senior
- C) @HKBU
- D) Department

✓ **Answer: A**

**Q4: Players expect objects to behave naturally, 
enhancing their experience?**
- A) objects
- B) expect
- C) to
- D) behave

✓ **Answer: A**

**Q5: ▪Gameplay Mechanics
▪Understanding these motions allows designers to create 
innovative gameplay elements?**
- A) ▪Understanding
- B) Mechanics
- C) these
- D) motions

✓ **Answer: A**

**Q6: Circular platforms and 
pendulum obstacles challenge players in unique ways?**
- A) and
- B) platforms
- C) pendulum
- D) obstacles

✓ **Answer: A**

**Q7: ▪Visual Appeal
▪Smooth, natural animations based on these motions 
captivate players?**
- A) ▪Smooth,
- B) Appeal
- C) natural
- D) animations

✓ **Answer: A**

**Q8: They add life and dynamism to game 
environments and characters?**
- A) life
- B) add
- C) and
- D) dynamism

✓ **Answer: A**

### Practice Problems


**Problem 1:**
Calculate the result when applying Animation to the values 1, 9

**Solution Approach:** Refer to the Animation formula: work through step by step

**Problem 2:**
Explain how Harmonic differs from Rotation

**Solution Approach:** Consider the definitions, properties, and applications of each

**Problem 3:**
Apply Rotation to a scenario with game animation

**Solution Approach:** Break down the problem using the relevant formula or definition

### Revision Tips

- 1. Focus on understanding the core formulas and when to use them
- 2. Practice working through numerical examples
- 3. Understand the geometric or visual interpretation
- 4. Relate concepts to real-world game/animation scenarios
- 5. Create flashcards for key terms and definitions

---
