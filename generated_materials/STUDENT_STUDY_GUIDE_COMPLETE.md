# GAME2016 Complete Student Study Guide
## All 15 Lectures with Worked Solutions & Applications

---

## Table of Contents
1. L1a - Course Overview
2. L1b - Cartesian Coordinates
3. L1c - Multiple Coordinate Spaces
4. L2a - Vectors
5. L2b - Random Numbers
6. L3 - Matrices
7. L4a - Matrices and Linear Transformations
8. L4b - Classes of Transformations
9. L5a - Matrix Determinant, Inverse, Orthogonalization
10. L6a - Homogeneous Matrices
11. L6b - 2D Polar Coordinate Systems
12. L6c - 3D Polar Coordinate Systems
13. L7 - Rotation in Three Dimensions
14. L9 - Pendulum, Circular, Harmonic Motion
15. L12 - Collision Detection

---

## GAME2016 L1a - Course Overview
### Key Concepts Explained

1. Course Foundations
- Purpose: Understand why vectors, matrices, and transforms are the backbone of game math. They let us describe positions, motions, and relationships between objects.
- Typical elements: vectors for movement, matrices for changing coordinate spaces, and coordinate systems for placing objects in the scene.

2. Practical Applications
- Asset transforms: combining position, rotation and scale to place models in the world.
- Pipeline awareness: how world, camera, and screen spaces connect during rendering and input handling.

---

### Quiz Question & Student Answer

Q1: Which of the following best explains the role of coordinate spaces in a rendering pipeline?
Options:
- A) They control audio mixing levels.
- B) They allow consistent placement of objects across world, camera and screen.
- C) They determine font sizes in UI.
- D) They are irrelevant for rendering.

Student approach:
"Coordinate spaces map object-local positions into the world and then into camera/screen space. That matches option B." 

Answer: B

Explanation: Coordinate spaces are essential for transforming object-local coordinates to world coordinates and then projecting them through the camera to screen coordinates.

---

### Practice Problem & Student Solution

Problem: Explain the steps to render a model located at local coordinates (1, 2, 0) into screen space. List the transforms applied.

Student solution:
Step 1: Apply the object's local transform (scale, rotation, translation) to move from local to model space.
Step 2: Multiply by the world transform if the object has a parent or world offset.
Step 3: Multiply by the camera/view matrix to convert world → camera space.
Step 4: Multiply by projection matrix (perspective or orthographic) to convert camera → clip space.
Step 5: Perform perspective divide (divide by w) and map to screen coordinates.

Result: The model's vertex position is transformed through model → world → camera → clip → NDC → screen.

---
## GAME2016 L1b - Cartesian Coordinates

### **Key Concepts Explained**

#### **Cartesian Grid**
- **What it is:** A coordinate system using perpendicular axes (X, Y, Z). Each point is described by (x, y, z) values.
- **Example:** A player at position (10, 0, 5) is 10 units along X-axis, 0 units along Y, and 5 units along Z.

#### **3D vs 2D**
- **2D:** Uses (x, y)—like a flat map.
- **3D:** Uses (x, y, z)—adds depth for full 3D space.

### **Practice Problem & Solution**

**Problem:** *Given a player at Cartesian coordinate (3, 4, 0) and an enemy at (0, 0, 0), calculate the distance between them.*

**Student solution:**
> **Step 1:** Use the distance formula: `d = √[(x₂-x₁)² + (y₂-y₁)² + (z₂-z₁)²]`  
> **Step 2:** Substitute: `d = √[(0-3)² + (0-4)² + (0-0)²] = √[9 + 16 + 0] = √25 = 5`  
> **Result:** The distance is 5 units.

---

## GAME2016 L1c - Multiple Coordinate Spaces

### **Key Concepts Explained**

#### **Different Coordinate Spaces**
- **World Space:** The "master" coordinate system for the entire game world.
- **Object/Local Space:** Each object has its own local coordinates (relative to itself).
- **Camera Space:** Coordinates relative to the camera's viewpoint.
- **Screen Space:** 2D coordinates on the screen (pixels).

#### **Why This Matters**
- An NPC at (0, 0, 0) in its local space might be at (100, 50, 200) in world space.
- To check collision, convert both objects to the same coordinate space.

#### **Coordinate Space Transformations**
- **Translation:** Shifts the origin; changes position.
- **Rotation:** Changes the orientation of axes.

### **Practice Problem & Solution**

**Problem:** *An NPC is at local position (1, 0, 0) in its object space. The object itself is positioned at world coordinate (10, 10, 0). Where is the NPC in world space?*

**Student solution:**
> **Step 1:** Local position of NPC: (1, 0, 0)  
> **Step 2:** Object world position (translation): (10, 10, 0)  
> **Step 3:** NPC world position = local + world = (1+10, 0+10, 0+0) = **(11, 10, 0)**

---

## GAME2016 L2a - Vectors

### **Key Concepts Explained**

#### **Vector Components**
- **Magnitude:** The length of the vector. Formula: `||v|| = √(x² + y² + z²)`
- **Direction:** Which way the vector points (normalized form).
- **Components:** Individual x, y, z values.

#### **Vector Operations**
- **Addition:** Combine vectors: `(1,2) + (3,1) = (4,3)`
- **Scalar Multiplication:** Scale vector: `2 * (1,2) = (2,4)`
- **Dot Product:** Measure alignment: `a·b = a_x*b_x + a_y*b_y + a_z*b_z`
- **Cross Product:** Get perpendicular vector (used for normals).

#### **Game Applications**
- **Velocity:** Direction and speed combined.
- **Force:** Wind, gravity, push—all vectors.
- **Normal vectors:** Used for lighting and collision.

### **Quiz Q&A**

**Q: Which of the following best describes 'Vector'?**  
**Student approach:**  
> *"A vector has magnitude (size), direction (which way), and component values (x, y, z). That's the definition."*

**Answer:** Vector typically involves magnitude, direction, and component.

### **Practice Problems & Solutions**

**Problem 1:** *Calculate the magnitude of vector v = (3, 4, 0).*

**Solution:**
> `||v|| = √(3² + 4² + 0²) = √(9 + 16) = √25 = 5`

**Problem 2:** *If vector a = (2, 3) and vector b = (1, 4), calculate their dot product.*

**Solution:**
> `a · b = (2)(1) + (3)(4) = 2 + 12 = 14`  
> **Interpretation:** Positive dot product means they point somewhat in the same direction.

**Problem 3:** *A projectile has velocity vector (10, 20, 0) (in units/second). Where will it be in 3 seconds?*

**Solution:**
> **Step 1:** Distance = velocity × time = (10, 20, 0) × 3  
> **Step 2:** Position = (30, 60, 0)  
> **The projectile travels 30 units in X and 60 units in Y over 3 seconds.**

---

## GAME2016 L2b - Random Numbers

### **Key Concepts Explained**

#### **True vs Pseudo-Random**
- **True Random:** Quantum computers can generate truly random numbers (unpredictable).
- **Pseudo-Random:** Regular computers use algorithms (deterministic but appear random).

#### **Mersenne Twister (MT19937)**
- **What it is:** A popular PRNG algorithm.
- **Properties:** Generates 624 numbers at a time; very long sequence length (2^19937 - 1).
- **Use:** Game randomness, shuffling, procedural generation.

#### **Seeding**
- **What it is:** Setting the starting value for the RNG.
- **Why:** For reproducible randomness (same seed = same sequence).
- **Game example:** Same level seed means same enemy spawn locations every time.

### **Practice Problem & Solution**

**Problem:** *Explain why pseudo-random numbers are "good enough" for games even though they're not truly random.*

**Solution:**
> Pseudo-random numbers follow deterministic algorithms, but the output appears random to players. For games, this is ideal because:
> 1. It's fast (important for real-time performance)
> 2. It's reproducible (seeding for consistent level generation)
> 3. The sequence is long enough that players never see a pattern
> 4. True randomness isn't necessary—the illusion of randomness is

---

## GAME2016 L3 - Matrices

### **Key Concepts Explained**

#### **What's a Matrix?**
- A grid of numbers: rows × columns.
- Example 2×2 matrix: `[[1, 2], [3, 4]]`

#### **Matrix Operations**
- **Determinant (det):** A single number describing matrix properties. If det = 0, matrix is singular (not invertible).
- **Inverse (M⁻¹):** The "undo" operation. If M transforms a vector, M⁻¹ reverses it.
- **Transpose (Mᵀ):** Flip rows and columns.

#### **Game Applications**
- **Transform 3D points:** Multiply point vector by transformation matrix.
- **Combine transformations:** Multiply matrices to apply multiple transforms.
- **Undo transforms:** Use inverse matrix.

### **Quiz Q&A**

**Q: Which of the following best describes 'Matrix'?**  
**Student approach:**  
> *"A matrix involves three key concepts: determinant (a property), inverse (undo operation), and transpose (flip rows/cols)."*

**Answer:** Matrix typically involves determinant, inverse, and transpose.

### **Practice Problem & Solution**

**Problem:** *Given transformation matrix M, explain what M⁻¹ does and when you'd use it.*

**Solution:**
> If matrix M rotates a point 90° clockwise, then M⁻¹ rotates it 90° counter-clockwise (undoing the transform).
>
> **When to use:**
> - To reverse a transformation
> - To convert from one coordinate space back to another
> - To "undo" camera transforms

---

## GAME2016 L4a - Matrices and Linear Transformations

### **Key Concepts Explained**

#### **Linear Transformations**
- **Definition:** A transformation described by matrix multiplication.
- **Types:** Rotation, scaling, shearing, projection.
- **Property:** Straight lines remain straight.

#### **Matrix-Vector Multiplication**
- **Concept:** `v' = M × v` transforms vector v using matrix M.
- **Example:** Rotate point (1, 0) by 90° using rotation matrix.

#### **Combining Transformations**
- **Multiple transforms:** `v' = M3 × (M2 × (M1 × v)) = (M3 × M2 × M1) × v`
- **Optimization:** Pre-multiply matrices instead of applying one at a time.

### **Practice Problem & Solution**

**Problem:** *If you need to rotate an object 45° and then scale it by 2, what's the most efficient way to apply both transforms in code?*

**Solution:**
> **Efficient approach:**
> 1. Create rotation matrix R (45°)
> 2. Create scale matrix S (scale by 2)
> 3. Pre-multiply: `Combined = S × R`
> 4. Apply once: `point' = Combined × point`
>
> **Why:** One matrix multiplication is faster than two. This is crucial for 1000s of game objects each frame.

---

## GAME2016 L4b - Classes of Transformations

### **Key Concepts Explained**

#### **Three Main Transformation Classes**
1. **Translation:** Move objects. Formula: `new_point = old_point + offset`
2. **Scaling:** Resize objects. Formula: `new_point = old_point × scale_factor`
3. **Shear:** Skew objects. Formula: Complex; depends on shear direction.

#### **Properties**
- **Linear:** Rotation, scaling, shearing (preserve origin).
- **Affine:** Translation + linear (general transformation).

### **Quiz Q&A**

**Q: Which of the following best describes 'Transformation'?**  
**Student approach:**  
> *"Transformation = translation (move), scaling (resize), and shear (skew)."*

**Answer:** Transformation typically involves translation, scaling, and shear.

### **Practice Problem & Solution**

**Problem:** *Distinguish between scaling and shearing. Give a game example for each.*

**Solution:**
> **Scaling:** Resize uniformly or non-uniformly. All axes scale.
> - Example: A powerup grows from size 1 to size 2 (scales 2x).
>
> **Shearing:** One axis moves relative to another.
> - Example: Text italics—horizontal text shears (leans) while vertical stays fixed.

---

## GAME2016 L5a - Matrix Determinant, Inverse, Orthogonalization

### **Key Concepts Explained**

#### **Determinant**
- **What it is:** A single number that describes a matrix's properties.
- **Meaning:** 
  - If det = 0: matrix is singular (not invertible, no unique inverse).
  - If det ≠ 0: matrix is invertible.
  - If det < 0: transformation includes reflection.

#### **Matrix Inverse**
- **Formula:** M⁻¹ is the matrix such that `M × M⁻¹ = I` (identity).
- **Use:** Reverse transformations.
- **Computation:** Multiple methods; classical adjoint or Gaussian elimination.

#### **Orthogonalization**
- **Concept:** Ensuring matrix columns/rows are perpendicular (orthogonal).
- **Property:** Orthogonal matrices are easy to invert: `M⁻¹ = Mᵀ`
- **Benefit:** Rotation matrices are orthogonal → fast inversion.

### **Practice Problem & Solution**

**Problem:** *Why are orthogonal matrices important for 3D rotation in games?*

**Solution:**
> Orthogonal rotation matrices have the property that `M⁻¹ = Mᵀ` (transpose = inverse).
>
> **Benefit:** Computing transpose is trivial—just swap rows/columns. No complex calculations needed.
>
> **Game impact:** Reversing a rotation is free; essential for efficient physics and animation.

---

## GAME2016 L6a - Homogeneous Matrices
### Key Concepts Explained

1. Vector Operations
- Magnitude: The length of the vector. Formula: `||v|| = √(x² + y² + z²)`
- Dot product: Measures how aligned two vectors are. Useful for angles and projections.
- Cross product: Produces a vector perpendicular to two input vectors. Useful for finding normals.

2. Vector Application
- Representing velocity: A vector with magnitude (speed) and direction (which way)
- Representing position: A vector from origin to a point
- Representing forces: Wind, gravity, push—all vectors

---

### Quiz Question & Student Answer

Q1: Which of the following best describes 'Vector'?
Options:
- A) Coordinate typically involves...
- B) Numerical Values...
- C) Animation...
- D) Vector typically involves magnitude, direction and component.

Student approach:
"What defines a vector? It has magnitude (size), direction (which way), and component values (x, y, z). Option D is the textbook definition."

Answer: D

Explanation: Vectors are defined by magnitude (length), direction (orientation), and components (x, y, z values).

---

### Practice Problem & Student Solution

Problem: Calculate Vector Magnitude and Use It

Problem:
Given a velocity vector v = (3, 4, 0), calculate its magnitude and explain what it means in a game.

Student solution:
Step 1: Calculate magnitude using the formula `||v|| = √(x² + y² + z²)`
`||v|| = √(3² + 4² + 0²) = √(9 + 16) = √25 = 5`
Interpretation: The magnitude of 5 means the object is moving at speed 5 units/second.
The direction (3, 4, 0) normalized is (0.6, 0.8, 0), meaning it's moving mostly in the +Y direction with some +X component.
In a game: An NPC moving with this velocity travels diagonally, covering 5 units each second.

#### **Aliasing Problem**
- **Issue:** Infinitely many polar coordinates describe the same point.
- **Example:** (5, 0°) = (5, 360°) = (5, 720°)
- **Solution:** Normalize θ to [0°, 360°) or (-180°, 180°].

### **Practice Problem & Solution**

**Problem:** *A radar system detects an enemy at polar coordinates (100 meters, 45°). What are the Cartesian coordinates (assuming up = Y-axis, right = X-axis)?*

**Solution:**
> **Step 1:** Use formulas:
> - `x = 100 × cos(45°) = 100 × 0.707 ≈ 70.7`
> - `y = 100 × sin(45°) = 100 × 0.707 ≈ 70.7`
>
> **Result:** Enemy is at Cartesian (70.7, 70.7), northeast of the radar.

---

## GAME2016 L6c - 3D Polar Coordinate Systems (Spherical)

### **Key Concepts Explained**

#### **Spherical Coordinates (r, θ, φ)**
- **r:** Distance from origin.
- **θ:** Azimuthal angle (rotation around vertical axis, like longitude).
- **φ:** Polar angle (angle from vertical, like latitude).

#### **Conversion (3D)**
- **To Cartesian:**
  - `x = r × sin(φ) × cos(θ)`
  - `y = r × cos(φ)`
  - `z = r × sin(φ) × sin(θ)`

#### **Game Applications**
- **Camera orbits:** Rotate camera around player using spherical coords.
- **Directional audio:** Determine where sound comes from (3D).
- **Procedural generation:** Distribute points on sphere.

### **Practice Problem & Solution**

**Problem:** *Using spherical coordinates, explain how to make a camera orbit a player at distance 10 units, at angle θ=45°, and φ=30°.*

**Solution:**
> **Spherical coordinates: (r=10, θ=45°, φ=30°)**
>
> **Convert to Cartesian:**
> - `x = 10 × sin(30°) × cos(45°) = 10 × 0.5 × 0.707 ≈ 3.54`
> - `y = 10 × cos(30°) = 10 × 0.866 ≈ 8.66`
> - `z = 10 × sin(30°) × sin(45°) = 10 × 0.5 × 0.707 ≈ 3.54`
>
> **Camera position:** (3.54, 8.66, 3.54) relative to player.  
> To rotate: vary θ; to tilt up/down: vary φ.

---

## GAME2016 L7 - Rotation in Three Dimensions

### **Key Concepts Explained**

#### **Three Rotation Representations**
1. **Euler Angles (pitch, yaw, roll):**
   - Intuitive: three angle rotations.
   - Problem: Gimbal lock (loss of degree of freedom).

2. **Quaternions:**
   - Compact: 4 values (x, y, z, w).
   - Smooth interpolation: ideal for animation.
   - Avoids gimbal lock.

3. **Axis-Angle:**
   - Intuitive: rotate around axis by angle.
   - Less efficient; harder to combine.

4. **Rotation Matrices:**
   - 3×3 matrix (or 4×4 homogeneous).
   - Used by graphics APIs.
   - Efficient for transforming points.

#### **Why Multiple Representations?**
- **User input:** Euler angles (intuitive).
- **Animation:** Quaternions (smooth blending).
- **GPU:** Matrices (fast multiplication).

### **Practice Problem & Solution**

**Problem:** *Explain gimbal lock and why quaternions solve it.*

**Solution:**
> **Gimbal Lock:**
> When rotating Euler angles in certain orders, you can lose one degree of freedom. All three angles can't be independently controlled.
>
> **Example:** If pitch = 90°, rotating yaw and roll produces the same result (both rotate around same axis).
>
> **Quaternion Solution:**
> Quaternions don't suffer from gimbal lock. They smoothly interpolate between any two rotations without singularities.
>
> **Game impact:** Camera rotation, character animation, and physics calculations are smooth and reliable with quaternions.

---

## GAME2016 L9 - Pendulum, Circular, Harmonic Motion

### **Key Concepts Explained**

#### **Harmonic Motion**
- **Definition:** Repeating oscillation where restoring force ∝ displacement.
- **Key properties:**
  - **Oscillation:** Back-and-forth movement.
  - **Frequency:** How many cycles per second.
  - **Amplitude:** Maximum distance from center.
  - **Period:** Time for one complete cycle.

#### **Pendulum Example**
- **Forces:** Gravity pulls bob down; string tension pulls up.
- **Energy:** Converts between potential (high points) and kinetic (low points).
- **Period Formula:** `T ≈ 2π√(L/g)` where L = length, g = gravity.

#### **Game Applications**
- **Swinging obstacles:** Pendulum motion in puzzle games.
- **Oscillating platforms:** Moving up/down in rhythm.
- **Character bobbing:** Walking animation (head bobs up/down).
- **Wave effects:** Water, flags, particles.

### **Quiz Q&A**

**Q: Which of the following best describes 'Harmonic'?**  
**Student approach:**  
> *"Harmonic motion = oscillation (back-and-forth), frequency (cycles/second), and amplitude (max distance)."*

**Answer:** Harmonic typically involves oscillation, frequency, and amplitude.

### **Practice Problems & Solutions**

**Problem 1:** *A pendulum swings with period T = 2 seconds and amplitude A = 1 meter. At what times is the bob at the highest point?*

**Solution:**
> **Concept:** Highest point = maximum displacement = amplitude.
> **Timing:** At t = 0, T/2, T, 3T/2, 2T, ...  
> **For T = 2s:** Highest point at t = 0s, 1s, 2s, 3s, 4s, ...  
> **Answer:** Every 1 second, the bob is at maximum height.

**Problem 2:** *If you need to create a bobbing animation for a character's head using sine function, explain the formula and parameters.*

**Solution:**
> **Formula:** `height = center + amplitude × sin(2π × frequency × time + phase)`
>
> **Parameters:**
> - `center`: Resting height (e.g., 1.7m for standing)
> - `amplitude`: How much it bobs (e.g., 0.05m)
> - `frequency`: Bobs per second (e.g., 2 Hz = 2 bobs/sec)
> - `phase`: Time offset for multiple characters
>
> **Example:** Head height = 1.7 + 0.05 × sin(2π × 2 × time)

---

## GAME2016 L12 - Collision Detection

### **Key Concepts Explained**

#### **Collision Detection Methods**
1. **AABB (Axis-Aligned Bounding Box):**
   - Fast: simple comparisons.
   - Limited: only for axis-aligned boxes.

2. **Bounding Sphere:**
   - Circle/sphere for collision.
   - Pros: Rotation-independent, fast.
   - Cons: Loose fit for non-spherical objects.

3. **Ray-Casting:**
   - Shoot a ray; check what it hits.
   - Use: Line-of-sight, projectiles, raycasting.

#### **3D Sphere Formula**
- **Equation:** `(x - cx)² + (y - cy)² + (z - cz)² = r²`
- **Check collision:** Two spheres collide if distance between centers ≤ sum of radii.

### **Quiz Q&A**

**Q: Which of the following best describes 'Application of Collision'?**  
**Student approach:**  
> *"Collision detection uses AABB (axis-aligned boxes), spheres (circles), and ray-casting (lines)."*

**Answer:** Collision typically involves AABB, sphere, and ray-casting.

### **Practice Problems & Solutions**

**Problem 1:** *Two spheres: Sphere A (center = (0, 0, 0), radius = 2), Sphere B (center = (3, 4, 0), radius = 1). Do they collide?*

**Solution:**
> **Step 1:** Calculate distance between centers:  
> `d = √[(3-0)² + (4-0)² + (0-0)²] = √[9 + 16] = √25 = 5`
>
> **Step 2:** Sum of radii: `r_A + r_B = 2 + 1 = 3`
>
> **Step 3:** Compare: d = 5, sum = 3  
> `5 > 3` → **No collision**
>
> Spheres are 2 units apart.

**Problem 2:** *Explain why ray-casting is used for detecting if a player can "see" an enemy.*

**Solution:**
> **Ray-casting approach:**
> 1. Cast a ray from player's eye position toward enemy
> 2. Check if ray hits any obstacles (walls, objects) before reaching enemy
> 3. If obstacle detected first: enemy is hidden (not visible)
> 4. If ray reaches enemy: enemy is visible (direct line of sight)
>
> **Game benefit:** Realistic visibility; enemies don't see through walls.

---

## COMPREHENSIVE FORMULA REFERENCE

| Concept | Formula |
|---------|---------|
| **Vector Magnitude** | `\|\|v\|\| = √(x² + y² + z²)` |
| **Distance Between Points** | `d = √[(x₂-x₁)² + (y₂-y₁)² + (z₂-z₁)²]` |
| **Dot Product** | `a · b = a_x×b_x + a_y×b_y + a_z×b_z` |
| **Angle Between Vectors** | `cos(θ) = (a · b) / (\|\|a\|\| × \|\|b\|\|)` |
| **Polar to Cartesian (2D)** | `x = r cos θ, y = r sin θ` |
| **Cartesian to Polar (2D)** | `r = √(x² + y²), θ = atan2(y, x)` |
| **Spherical to Cartesian** | `x = r sin φ cos θ, y = r cos φ, z = r sin φ sin θ` |
| **Matrix Determinant (2×2)** | `det(M) = ad - bc` for `[[a,b],[c,d]]` |
| **Matrix Transpose** | `(M^T)_{ij} = M_{ji}` |
| **Identity Matrix** | `M × I = M` (multiplication by identity = no change) |
| **Matrix Inverse** | `M × M⁻¹ = I` (undo transformation) |
| **Harmonic Motion** | `displacement = A sin(2πft + phase)` |
| **Pendulum Period** | `T = 2π√(L/g)` |
| **Sphere Collision** | Distance ≤ r₁ + r₂ |
| **AABB Collision (3D)** | Overlapping in all three axes |

---

## STUDY TIPS FOR EXAM SUCCESS

### **Conceptual Understanding**
1. **Connect to Games:** Every formula is about moving, rotating, or detecting objects.
2. **Visualize:** Draw diagrams. Sketch rotations, coordinate spaces, vectors.
3. **Understand Why:** Don't memorize—understand the geometry behind formulas.

### **Problem-Solving Strategy**
1. **Identify:** What are you given? What do you need to find?
2. **Choose Method:** Which formula/concept applies?
3. **Substitute:** Plug in numbers carefully.
4. **Compute:** Do the math step-by-step.
5. **Interpret:** What does the answer mean? Does it make sense?

### **Concept Relationships**
- **Vectors** are the foundation for everything (positions, directions, forces).
- **Matrices** transform vectors (rotation, scaling, translation).
- **Coordinate Systems** describe where vectors exist (world, local, camera).
- **Collision** combines vectors and bounding volumes.
- **Harmonic Motion** is a specific application of oscillation + mathematics.

### **Common Exam Mistakes (Avoid These!)**
- ❌ Forgetting to normalize vectors when direction matters
- ❌ Mixing up radians and degrees
- ❌ Using Euler angles without realizing gimbal lock
- ❌ Forgetting matrix multiplication order matters (not commutative)
- ❌ Computing distance but forgetting √ in the formula
- ❌ Confusing w=1 vs w=0 in homogeneous coordinates

### **Quick Review Checklist**

Before the exam, make sure you can:
- [ ] Calculate vector magnitude and dot product
- [ ] Convert between Cartesian, polar, and spherical coordinates
- [ ] Apply matrix multiplication to transform points
- [ ] Explain gimbal lock and why quaternions help
- [ ] Determine collision using spheres or AABB
- [ ] Recognize harmonic motion and calculate period
- [ ] Distinguish between translation, rotation, and scaling
- [ ] Use homogeneous coordinates correctly
- [ ] Compute matrix inverse (or recognize when M⁻¹ = Mᵀ)
- [ ] Apply ray-casting concept

---

## LAST-MINUTE TIPS

**Night Before Exam:**
- Review concept connections (vectors → matrices → transformations)
- Work through 2-3 practice problems from each lecture
- Sleep well!

**Day of Exam:**
- Read questions carefully; identify what's being asked
- Show work (partial credit for correct method)
- Double-check units (radians vs degrees, meters vs units)
- Use rough paper for sketches and calculations
- If stuck: move on, come back later

**During Exam:**
- Multiple choice: Eliminate obvious wrong answers first
- Written: Explain your reasoning, not just final answer
- Problem-solving: Break into smaller steps
- Time management: Don't spend 15 min on one hard problem

---

**Good luck on your exam! Remember: you understand these concepts. Trust your preparation!**
