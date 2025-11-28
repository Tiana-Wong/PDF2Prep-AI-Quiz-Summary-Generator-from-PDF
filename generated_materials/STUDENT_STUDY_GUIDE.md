# GAME2016 Student Study Guide
## Exam Revision with Worked Solutions

---

## GAME2016 L9 - Pendulum, Circular, Harmonic Motion

### **Key Concepts Explained**

#### 1. **Animation**
- **What it is:** Animation is the technique of creating the illusion of motion by rapidly displaying a sequence of images. In game development, this involves three main ideas:
  - **Interpolation:** smoothly transitioning between values (e.g., position, rotation) over time
  - **Keyframe:** defining specific poses or positions at certain times; the animation system fills in the gaps
  - **Easing:** controlling the speed of transitions (e.g., speeding up or slowing down)
- **Real example:** When a character walks across the screen, we interpolate between keyframes to create smooth motion instead of jumping frame-to-frame.

#### 2. **Harmonic Motion**
- **What it is:** Motion that repeats in a predictable, oscillating pattern. Key components:
  - **Oscillation:** the back-and-forth movement
  - **Frequency:** how many times the motion repeats per unit time
  - **Amplitude:** the maximum distance from the center point
- **Real example:** A pendulum swinging, a spring bouncing, or a character bobbing up and down.

#### 3. **Rotation**
- **What it is:** Changing the orientation/angle of an object in 3D space. Three common ways to represent it:
  - **Quaternion:** a compact, efficient way to avoid gimbal lock
  - **Euler angles:** three rotations (pitch, yaw, roll)
  - **Axis-angle:** rotation around a specific axis
- **Real example:** Rotating a character's head, spinning a wheel, or tilting the camera.

---

### **Quiz Questions & Student Answers**

#### **Q1: Which of the following best describes 'Animation'?**
**Options:**
- A) Rotation typically involves quaternion, euler angles and axis-angle.
- B) Harmonic typically involves oscillation, frequency and amplitude.
- C) Animation typically involves interpolation, keyframe and easing.
- D) Numerical Values is an important concept in this lecture.

**Student approach:**
> *"Let me think about what animation is. Animation is about moving things smoothly on screen. That requires interpolation (smoothing between values), keyframes (key poses), and easing (controlling speed). That's option C. A is about rotation, B is about harmonic motion—those are different concepts."*

**Answer:** **C**  
**Explanation:** Animation involves smoothly transitioning between keyframes using interpolation and easing functions.

---

#### **Q2: Which of the following best describes 'Application of Harmonic'?**
**Options:**
- A) It is used for harmonic typically involves oscillation, frequency and amplitude.
- B) It is used for animation typically involves interpolation, keyframe and easing.
- C) It is used for numerical values is an important concept in this lecture.
- D) It is used for rotation typically involves quaternion, euler angles and axis-angle.

**Student approach:**
> *"The question asks how Harmonic is applied or used. Harmonic motion = oscillating back and forth. The definition of harmonic IS oscillation, frequency, and amplitude. So A is the definition. That makes sense."*

**Answer:** **A**  
**Explanation:** Harmonic motion is fundamentally characterized by oscillation, frequency (how fast it repeats), and amplitude (how far it swings).

---

#### **Q3: In a game scenario, how is 'Animation' commonly applied?**
**Options:**
- A) For spatial computations
- B) For audio processing
- C) For UI layout
- D) For network sync

**Student approach:**
> *"Where do we use animation in games? We animate characters moving, objects falling, cameras panning—all spatial things (position, rotation, scale). Audio processing is about sound, UI layout is about interface design. Animation is about spatial motion."*

**Answer:** **A**  
**Why:** Animation in games is primarily about changing spatial properties (position, rotation, scale) over time.

---

### **Practice Problems & Student Solutions**

#### **Problem 1: Explain Animation + Give an Example**

**Problem:**  
*Explain in your own words what Animation is and give one small example of where it is used in games/animation.*

**Student solution:**
> Animation is the technique of creating movement by smoothly transitioning between different states over time using interpolation between keyframes and easing functions to control the speed of changes.
> 
> **Example:** In a character running animation, we define keyframes at different points in the run cycle (legs extended, legs bent, etc.). The game engine interpolates between these keyframes each frame to create smooth motion. We use easing to make the transitions feel natural.

---

#### **Problem 2: Explain Harmonic Motion + Give an Example**

**Problem:**  
*Explain in your own words what Harmonic is and give one small example of where it is used in games/animation.*

**Student solution:**
> Harmonic motion is a repeating, oscillating pattern where an object moves back and forth. It's defined by oscillation (the back-and-forth pattern), frequency (how many cycles per second), and amplitude (how far it moves from center).
> 
> **Example:** A pendulum in a puzzle game swings left and right on a fixed cycle. The period is fixed, the amplitude determines how far it swings (difficulty), and we can use harmonic equations to predict where the pendulum will be at any future time—useful for timing-based challenges.

---

#### **Problem 3: Explain Rotation + Give an Example**

**Problem:**  
*Explain in your own words what Rotation is and give one small example of where it is used in games/animation.*

**Student solution:**
> Rotation is the change in an object's orientation in 3D space. We can represent it using quaternions (compact, efficient), Euler angles (intuitive but prone to gimbal lock), or axis-angle (rotation around a specific axis).
> 
> **Example:** When a player character turns to face a direction, we rotate them around the vertical (Y) axis. For smooth head tracking, we might use quaternions to interpolate between the current head orientation and the target orientation without gimbal lock issues.

---

---

## GAME2016 L12 - Collision Detection

### **Key Concepts Explained**

#### 1. **Collision Detection**
- **What it is:** The process of determining when two objects in a game world are touching or overlapping. Three main techniques:
  - **AABB (Axis-Aligned Bounding Box):** Fast, but only works for axis-aligned rectangles
  - **Sphere:** Works for circular/spherical objects; faster than exact shapes
  - **Ray-casting:** Shoots a ray and checks what it hits; useful for line-of-sight or projectiles
- **Real example:** Detecting when the player touches an enemy, collects a coin, or hits a wall.

#### 2. **Vector**
- **What it is:** A quantity with both magnitude (size) and direction. Key components:
  - **Magnitude:** the length/size of the vector
  - **Direction:** which way it points
  - **Component:** individual x, y, z values
- **Real example:** The velocity of a projectile is a vector—it has both speed (magnitude) and direction.

---

### **Quiz Questions & Student Answers**

#### **Q1: Which of the following best describes 'Application of Collision'?**
**Options:**
- A) It is used for rotation typically involves quaternion, euler angles and axis-angle.
- B) It is used for collision typically involves AABB, sphere and ray-casting.
- C) It is used for animation typically involves interpolation, keyframe and easing.
- D) It is used for vector typically involves magnitude, direction and component.

**Student approach:**
> *"The question asks what Collision is or how it's applied. Collision detection uses bounding volumes: AABB (axis-aligned boxes), spheres (circles), and ray-casting (lines). That's the definition of collision detection. Answer B."*

**Answer:** **B**  
**Explanation:** Collision detection is performed using bounding volumes like AABB, spheres, and ray-casting.

---

#### **Q2: In a game scenario, how is 'Collision' commonly applied?**
**Options:**
- A) For spatial computations
- B) For audio processing
- C) For UI layout
- D) For network sync

**Student approach:**
> *"When do we use collision detection in games? When objects touch: player hits enemy (spatial), projectile hits wall (spatial), character walks on ground (spatial). These are all spatial computations—checking if things occupy the same space."*

**Answer:** **A**  
**Why:** Collision detection is about spatial relationships—determining if and where objects are touching in game space.

---

### **Practice Problems & Student Solutions**

#### **Problem 1: Collision in Practice**

**Problem:**  
*Explain in your own words what Collision is and give one small example of where it is used in games/animation.*

**Student solution:**
> Collision detection is the process of identifying when two objects in a game world overlap or are touching. We use fast approximations like AABB (bounding boxes), spheres (bounding circles), and ray-casting (line intersection) rather than exact geometry for performance.
> 
> **Example:** A player character walking on terrain. We check if the player's bounding sphere collides with the ground's bounding box every frame. If yes, the player is standing on solid ground. If no, the player is falling.

---

---

## GAME2016 L7 - Rotation in Three Dimensions

### **Key Concepts Explained**

#### 1. **Matrix**
- **What it is:** A grid of numbers used to perform transformations (rotation, scaling, translation). Key properties:
  - **Determinant:** a single number that tells you about the matrix's properties
  - **Inverse:** the "undo" operation—if M transforms a point, M⁻¹ transforms it back
  - **Transpose:** flipping rows and columns; useful for certain operations
- **Real example:** Multiplying a vector by a 3×3 matrix rotates it; multiply a vector by a 4×4 matrix to rotate AND translate.

#### 2. **Rotation (revisited with Matrix)**
- **What it is:** Rotation can be represented as a matrix. A 3×3 rotation matrix preserves vector lengths and angles.
- **Real example:** A 90° rotation matrix around the Z-axis looks like specific values that rotate points counterclockwise.

---

### **Quiz Question & Student Answer**

#### **Q1: Which of the following best describes 'Compare Rotation and Vector'?**
**Options:**
- A) Rotation and Vector are both about... (irrelevant)
- B) **Rotation focuses on rotation (quaternion, euler angles, axis-angle). Vector focuses on vector (magnitude, direction, component).**
- C) Rotation and Vector are both about... (irrelevant)
- D) Rotation and Vector are both about... (irrelevant)

**Student approach:**
> *"I need to compare these two concepts. Rotation = changing orientation (quaternion, euler, axis-angle). Vector = quantity with size and direction (magnitude, direction, component). They're different things. B correctly distinguishes between them."*

**Answer:** **B**  
**Explanation:** Rotation and vectors are different concepts. Rotation describes orientation using quaternions/euler/axis-angle. Vectors describe displacement/velocity with magnitude and direction.

---

### **Practice Problem & Student Solution**

#### **Problem: Compare Matrix and Rotation**

**Problem:**  
*In 3D rotations, how do matrices and rotation representations relate?*

**Student solution:**
> A rotation matrix is a 3×3 matrix that represents rotation. It's equivalent to any of the rotation representations (quaternions, euler angles, axis-angle), just in matrix form. We can convert between them:
> - Quaternion → 3×3 matrix
> - Euler angles → 3×3 matrix
> - Axis-angle → 3×3 matrix
> 
> **Why use matrices?** Because we can multiply a point by the matrix to rotate it: `rotated_point = rotation_matrix × original_point`

---

---

## GAME2016 L2a - Vectors

### **Key Concepts Explained**

#### 1. **Vector Operations**
- **Magnitude:** The length of the vector. Formula: `||v|| = √(x² + y² + z²)`
- **Dot product:** Measures how aligned two vectors are. Useful for angles and projections.
- **Cross product:** Produces a vector perpendicular to two input vectors. Useful for finding normals.

#### 2. **Vector Application**
- **Representing velocity:** A vector with magnitude (speed) and direction (which way)
- **Representing position:** A vector from origin to a point
- **Representing forces:** Wind, gravity, push—all vectors

---

### **Quiz Question & Student Answer**

#### **Q1: Which of the following best describes 'Vector'?**
**Options:**
- A) Coordinate typically involves...
- B) Numerical Values...
- C) Animation...
- D) **Vector typically involves magnitude, direction and component.**

**Student approach:**
> *"What defines a vector? It has magnitude (size), direction (which way), and component values (x, y, z). Option D is the textbook definition."*

**Answer:** **D**  
**Explanation:** Vectors are defined by magnitude (length), direction (orientation), and components (x, y, z values).

---

### **Practice Problem & Student Solution**

#### **Problem: Calculate Vector Magnitude and Use It**

**Problem:**  
*Given a velocity vector v = (3, 4, 0), calculate its magnitude and explain what it means in a game.*

**Student solution:**
> **Step 1:** Calculate magnitude using the formula `||v|| = √(x² + y² + z²)`  
> `||v|| = √(3² + 4² + 0²) = √(9 + 16) = √25 = 5`
> 
> **Interpretation:** The magnitude of 5 means the object is moving at speed 5 units/second.  
> The direction (3, 4, 0) normalized is (0.6, 0.8, 0), meaning it's moving mostly in the +Y direction with some +X component.
> 
> **In a game:** An NPC moving with this velocity travels diagonally, covering 5 units each second.

---

---

## Quick Study Tips (Student Perspective)

1. **Connect to Games:** Every concept should map to something you see in a game. Rotation = turning characters. Vectors = movement and speed. Collision = touching objects.

2. **Work Through Examples:** Don't just memorize formulas—compute them with real numbers.

3. **Distinguish Concepts:** Many questions test whether you can tell similar-sounding concepts apart (Animation vs. Harmonic, Matrix vs. Vector, etc.).

4. **Understand Applications:** Ask yourself: "Why would a game programmer need this? When would they use it?"

5. **Practice Consistently:** Work through practice problems before the exam. Explain concepts in your own words.

---

## Formula Quick Reference

| Concept | Key Formula/Property |
|---------|----------------------|
| Vector Magnitude | `\|\|v\|\| = √(x² + y² + z²)` |
| Dot Product | `a · b = a_x*b_x + a_y*b_y + a_z*b_z` |
| Angle Between Vectors | `cos(θ) = (a · b) / (\|\|a\|\| × \|\|b\|\|)` |
| Matrix Transpose | Flip rows and columns: `(M^T)_{ij} = M_{ji}` |
| Quaternion Properties | Used for smooth 3D rotations; avoids gimbal lock |
| AABB Collision | Check if bounding boxes overlap in each dimension |
| Harmonic Period | `T = 1/f` (period = 1 / frequency) |

---

**Good luck on your exam! Remember: understand the concepts deeply, then apply them to game scenarios.**
