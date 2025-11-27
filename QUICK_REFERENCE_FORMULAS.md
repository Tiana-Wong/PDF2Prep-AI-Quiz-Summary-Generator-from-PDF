# 🧮 Quick Reference: Math Formulas for Games & Animations

## 📐 Essential Formulas by Topic

### 1. VECTORS

#### Vector Magnitude (Norm)
```
2D: |v| = √(x² + y²)
3D: |v| = √(x² + y² + z²)
```

#### Dot Product
```
2D: u · v = u_x * v_x + u_y * v_y
3D: u · v = u_x * v_x + u_y * v_y + u_z * v_z
```

#### Cross Product (3D)
```
u × v = (u_y*v_z - u_z*v_y, u_z*v_x - u_x*v_z, u_x*v_y - u_y*v_x)
```

#### Vector Normalization
```
û = u / |u|
```

#### Linear Interpolation (LERP)
```
result = a + t(b - a), where 0 ≤ t ≤ 1
```

---

### 2. CARTESIAN COORDINATES

#### 2D Point
```
P = (x, y)
```

#### 3D Point
```
P = (x, y, z)
```

#### Distance Between Two Points (2D)
```
distance = √((x₂-x₁)² + (y₂-y₁)²)
```

#### Distance Between Two Points (3D)
```
distance = √((x₂-x₁)² + (y₂-y₁)² + (z₂-z₁)²)
```

#### Midpoint (2D)
```
M = ((x₁+x₂)/2, (y₁+y₂)/2)
```

#### Midpoint (3D)
```
M = ((x₁+x₂)/2, (y₁+y₂)/2, (z₁+z₂)/2)
```

---

### 3. POLAR COORDINATES

#### 2D Polar to Cartesian
```
x = r cos(θ)
y = r sin(θ)
```

#### 2D Cartesian to Polar
```
r = √(x² + y²)
θ = atan2(y, x)
```

#### 3D Spherical to Cartesian
```
x = r sin(φ) cos(θ)
y = r sin(φ) sin(θ)
z = r cos(φ)
```

#### 3D Cylindrical to Cartesian
```
x = r cos(θ)
y = r sin(θ)
z = z
```

---

### 4. MATRICES

#### 2D Translation Matrix
```
[1  0  tx]
[0  1  ty]
[0  0  1 ]
```

#### 2D Scaling Matrix
```
[sx  0  0]
[0  sy  0]
[0   0  1]
```

#### 2D Rotation Matrix (angle θ)
```
[cos(θ)  -sin(θ)  0]
[sin(θ)   cos(θ)  0]
[0        0       1]
```

#### 2D Shear Matrix
```
[1  kx  0]
[ky  1  0]
[0   0  1]
```

#### 3D Translation Matrix
```
[1  0  0  tx]
[0  1  0  ty]
[0  0  1  tz]
[0  0  0  1 ]
```

#### 3D Scaling Matrix
```
[sx  0   0   0]
[0  sy   0   0]
[0   0  sz   0]
[0   0   0   1]
```

#### 3D Rotation X-axis (angle θ)
```
[1    0      0   0]
[0  cos(θ) -sin(θ) 0]
[0  sin(θ)  cos(θ) 0]
[0    0      0   1]
```

#### 3D Rotation Y-axis (angle θ)
```
[cos(θ)  0  sin(θ)  0]
[0       1   0      0]
[-sin(θ) 0  cos(θ)  0]
[0       0   0      1]
```

#### 3D Rotation Z-axis (angle θ)
```
[cos(θ) -sin(θ)  0  0]
[sin(θ)  cos(θ)  0  0]
[0       0       1  0]
[0       0       0  1]
```

#### Matrix Determinant (2x2)
```
det(A) = ad - bc
where A = [a b]
           [c d]
```

#### Matrix Determinant (3x3)
```
det(A) = a(ei-fh) - b(di-fg) + c(dh-eg)
where A = [a b c]
           [d e f]
           [g h i]
```

#### Matrix Inverse (2x2)
```
A⁻¹ = (1/det(A)) * [ d -b]
                    [-c  a]
```

---

### 5. QUATERNIONS (For Rotations)

#### Quaternion Representation
```
q = (x, y, z, w) or (vector_part, scalar_part)
```

#### Quaternion Multiplication (q₁ * q₂)
```
More complex - see specialized resources
```

#### Quaternion to Matrix (3D)
```
[1-2(y²+z²)  2(xy-wz)    2(xz+wy)  ]
[2(xy+wz)    1-2(x²+z²)  2(yz-wx)  ]
[2(xz-wy)    2(yz+wx)    1-2(x²+y²)]
```

#### Quaternion Conjugate
```
q* = (-x, -y, -z, w)
```

#### Quaternion Magnitude
```
|q| = √(x² + y² + z² + w²)
```

---

### 6. COLLISIONS & BOUNDING VOLUMES

#### Circle Collision (2D)
```
Distance between centers: d = √((x₂-x₁)² + (y₂-y₁)²)
Collision if: d < (r₁ + r₂)
```

#### Sphere Collision (3D)
```
Distance: d = √((x₂-x₁)² + (y₂-y₁)² + (z₂-z₁)²)
Collision if: d < (r₁ + r₂)
```

#### Sphere Equation
```
2D Circle: (x - cx)² + (y - cy)² = r²
3D Sphere: (x - cx)² + (y - cy)² + (z - cz)² = r²
```

#### AABB (Axis-Aligned Bounding Box) Collision (2D)
```
Collision if:
x₁_min < x₂_max AND x₁_max > x₂_min AND
y₁_min < y₂_max AND y₁_max > y₂_min
```

#### Ray-Sphere Intersection
```
Parametric ray: P(t) = O + t*D (t ≥ 0)
Sphere: |P - C|² = r²
Solve for t to find intersection points
```

---

### 7. HARMONIC MOTION & OSCILLATION

#### Simple Harmonic Motion
```
x(t) = A cos(ωt + φ)
where:
- A = amplitude
- ω = angular frequency (2π*frequency)
- φ = phase shift
- t = time
```

#### Velocity in SHM
```
v(t) = -Aω sin(ωt + φ)
```

#### Acceleration in SHM
```
a(t) = -Aω² cos(ωt + φ)
```

#### Period of Oscillation
```
T = 2π/ω = 1/f
```

#### Frequency
```
f = 1/T = ω/(2π)
```

#### Angular Frequency
```
ω = 2πf
```

#### Pendulum Period
```
T = 2π√(L/g)
where:
- L = length of pendulum
- g = gravitational acceleration
```

---

### 8. INTERPOLATION & EASING

#### Linear Interpolation
```
result = a + t(b - a), where 0 ≤ t ≤ 1
```

#### Quadratic Easing In
```
value = t²
```

#### Quadratic Easing Out
```
value = 1 - (1-t)²
```

#### Cubic Easing In
```
value = t³
```

#### Ease-In-Out Cubic
```
if t < 0.5:
  value = 4t³
else:
  value = 1 - (-2t + 2)³/2
```

#### Sine Easing In
```
value = 1 - cos(t * π/2)
```

#### Sine Easing Out
```
value = sin(t * π/2)
```

---

### 9. RANDOM NUMBERS & PROBABILITY

#### Uniform Distribution (0 to 1)
```
Common in most programming languages
rand() or random()
```

#### Random Range (a to b)
```
value = a + random() * (b - a)
```

#### Gaussian (Normal) Distribution
```
Use Box-Muller transform or similar
```

#### Weighted Random Selection
```
Accumulate weights and select based on threshold
```

---

### 10. ANGULAR MEASUREMENTS

#### Degrees to Radians
```
radians = degrees * π/180
```

#### Radians to Degrees
```
degrees = radians * 180/π
```

#### Angular Velocity
```
ω = Δθ/Δt (radians per second)
```

#### Angular Acceleration
```
α = Δω/Δt (radians per second²)
```

---

## 🎯 Key Identities & Relationships

### Trigonometric Identities
```
sin²(θ) + cos²(θ) = 1
tan(θ) = sin(θ)/cos(θ)
sin(2θ) = 2sin(θ)cos(θ)
cos(2θ) = cos²(θ) - sin²(θ)
```

### Dot Product Properties
```
u · v = |u||v|cos(θ)  // angle between vectors
If u · v = 0, vectors are perpendicular
If u · v > 0, angle < 90°
If u · v < 0, angle > 90°
```

### Cross Product Properties
```
u × v is perpendicular to both u and v
|u × v| = |u||v|sin(θ)  // area of parallelogram
Right-hand rule determines direction
```

---

## 💾 Memory Tips

### Formulas to Memorize
1. **Distance formula** (2D and 3D)
2. **Rotation matrices** (at least one axis)
3. **Dot and cross products**
4. **Quaternion basics** for game dev
5. **Circle/Sphere collision** formulas
6. **SHM equations** (position, velocity)
7. **Degrees to radians** conversion
8. **LERP** for interpolation

### Common Mistakes to Avoid
- ❌ Forgetting to normalize vectors
- ❌ Using degrees instead of radians
- ❌ Mixing up matrix multiplication order
- ❌ Incorrect collision distance comparison
- ❌ Off-by-one errors in array indexing
- ❌ Not accounting for z-axis in 3D
- ❌ Assuming order of operations for matrix transforms

---

## 📊 Reference Table

| Concept | 2D | 3D |
|---------|----|----|
| **Coordinates** | (x, y) | (x, y, z) |
| **Distance** | √((x₂-x₁)² + (y₂-y₁)²) | √((x₂-x₁)² + (y₂-y₁)² + (z₂-z₁)²) |
| **Polar** | (r, θ) | (r, θ, φ) |
| **Vector Ops** | 2 components | 3 components |
| **Rotation Matrix** | 3x3 | 4x4 (homogeneous) |
| **Collision** | Circle/Box | Sphere/Box |

---

## 🔍 Quick Lookup by Application

### Animation
- LERP, Easing functions, Quaternions, Matrices

### Physics
- Vectors, Forces, Acceleration, SHM, Pendulum

### Collision
- Distance formulas, Spheres, AABB, Ray casting

### Transformations
- Matrices, Quaternions, Euler angles

### Graphics
- Matrices, Projections, Rotations, Polar coords

---

**Print this page or bookmark it for quick reference during your exam!**

*Good luck! 🍀*
