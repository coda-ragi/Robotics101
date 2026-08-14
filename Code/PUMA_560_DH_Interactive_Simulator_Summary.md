# PUMA 560 — DH-Based Interactive Simulator

## 1. What We Built

This project is a small **6-DOF PUMA 560 kinematics simulator built from scratch using NumPy and Matplotlib**.

The overall pipeline is:

```text
                 Joint angles q
                       │
                       ▼
              ┌─────────────────┐
              │   DH parameters │
              └────────┬────────┘
                       │
                       ▼
              DH transformation
                 A₁ A₂ ... A₆
                       │
                       ▼
             Forward Kinematics
                       │
                       ▼
              T₀, T₁, ... T₆
                       │
                       ▼
                Frame origins
                       │
                       ▼
                 3D skeleton
                       ▲
                       │
                  Sliders
                  q₁...q₆
                       │
                       └─────── live update
```

The simulator implements:

\[
q \rightarrow DH \rightarrow FK \rightarrow 3D
\]

where:

- \(q\) = six joint variables
- DH = Denavit–Hartenberg parameters
- FK = forward kinematics
- \(T_i\) = homogeneous transformation matrices
- 3D = visualization of the kinematic skeleton

---

# 2. Imports

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
```

### NumPy

Used for:

- matrices
- vectors
- trigonometry
- matrix multiplication
- numerical calculations

Examples:

```python
np.cos(theta)
np.sin(theta)
np.eye(4)
np.array(...)
```

### Matplotlib

Used to create the 3D visualization.

### Slider

```python
from matplotlib.widgets import Slider
```

Creates the six interactive joint controls:

```text
q1 ─────────●────────
q2 ─────────●────────
q3 ─────────●────────
q4 ─────────●────────
q5 ─────────●────────
q6 ─────────●────────
```

---

# 3. DH Transformation Function

```python
def dh_transform(a, alpha, d, theta):

    ca = np.cos(alpha)
    sa = np.sin(alpha)

    ct = np.cos(theta)
    st = np.sin(theta)

    return np.array([
        [ct, -st * ca,  st * sa, a * ct],
        [st,  ct * ca, -ct * sa, a * st],
        [0,   sa,       ca,       d],
        [0,   0,        0,        1]
    ])
```

This is the mathematical core of the simulator.

It accepts the four standard DH parameters:

\[
(a,\alpha,d,\theta)
\]

and returns the homogeneous transformation:

\[
{}^{i-1}T_i
\]

The matrix is:

\[
{}^{i-1}T_i =
\begin{bmatrix}
c_\theta & -s_\theta c_\alpha & s_\theta s_\alpha & a c_\theta\\
s_\theta & c_\theta c_\alpha & -c_\theta s_\alpha & a s_\theta\\
0&s_\alpha&c_\alpha&d\\
0&0&0&1
\end{bmatrix}
\]

The variables:

```python
ca = np.cos(alpha)
sa = np.sin(alpha)
ct = np.cos(theta)
st = np.sin(theta)
```

simply calculate the required sine and cosine terms.

### Conceptually

```text
(a, α, d, θ)
      │
      ▼
┌──────────────────┐
│ DH transformation│
└────────┬─────────┘
         ▼
        Aᵢ
```

The transformation tells us how frame \(i\) is positioned and oriented relative to frame \(i-1\).

---

# 4. PUMA 560 DH Parameters

```python
DH = [
    [0,      np.pi/2,  0.6718],
    [0.4318, 0,        0],
    [0.0203, -np.pi/2, 0.15],
    [0,      np.pi/2,  0.4318],
    [0,      -np.pi/2, 0],
    [0,      0,        0]
]
```

Each row stores:

```text
[aᵢ, αᵢ, dᵢ]
```

The joint variable \(\theta_i=q_i\) is supplied separately.

The table is:

| Joint | \(a_i\) | \(\alpha_i\) | \(d_i\) | \(\theta_i\) |
|---|---:|---:|---:|---|
| 1 | 0 | \(90^\circ\) | 0.6718 | \(q_1\) |
| 2 | 0.4318 | \(0^\circ\) | 0 | \(q_2\) |
| 3 | 0.0203 | \(-90^\circ\) | 0.15 | \(q_3\) |
| 4 | 0 | \(90^\circ\) | 0.4318 | \(q_4\) |
| 5 | 0 | \(-90^\circ\) | 0 | \(q_5\) |
| 6 | 0 | \(0^\circ\) | 0 | \(q_6\) |

The DH table is the mathematical description of the robot's kinematic structure.

---

# 5. Forward Kinematics

```python
def forward_kinematics(q):

    T = np.eye(4)

    frames = [T.copy()]

    for i in range(6):

        a = DH[i][0]
        alpha = DH[i][1]
        d = DH[i][2]
        theta = q[i]

        A = dh_transform(a, alpha, d, theta)

        T = T @ A

        frames.append(T.copy())

    return frames
```

This function takes:

\[
q=[q_1,q_2,q_3,q_4,q_5,q_6]
\]

and calculates all the transformations in the robot.

---

## 5.1 Start with the Identity Matrix

```python
T = np.eye(4)
```

This represents the base frame:

\[
{}^0T_0=I
\]

---

## 5.2 Save Frame 0

```python
frames = [T.copy()]
```

So:

```text
frames[0] = T₀
```

---

## 5.3 Loop Through the Six Joints

```python
for i in range(6):
```

This gives:

```text
i = 0 → Joint 1
i = 1 → Joint 2
i = 2 → Joint 3
i = 3 → Joint 4
i = 4 → Joint 5
i = 5 → Joint 6
```

For each joint:

```python
a = DH[i][0]
alpha = DH[i][1]
d = DH[i][2]
theta = q[i]
```

The fixed DH parameters are retrieved and the current joint angle is supplied as \(\theta_i\).

---

# 6. Calculate Each Link Transformation

```python
A = dh_transform(a, alpha, d, theta)
```

This gives:

\[
A_i = {}^{i-1}T_i
\]

For example:

\[
A_1={}^0T_1
\]

\[
A_2={}^1T_2
\]

and so on.

---

# 7. Chain the Transformations

The most important line in the FK function is:

```python
T = T @ A
```

`@` performs matrix multiplication.

Initially:

\[
T=I
\]

After joint 1:

\[
T={}^0T_1
\]

After joint 2:

\[
T={}^0T_1{}^1T_2={}^0T_2
\]

After joint 3:

\[
T={}^0T_2{}^2T_3={}^0T_3
\]

Eventually:

\[
\boxed{
{}^0T_6 =
{}^0T_1
{}^1T_2
{}^2T_3
{}^3T_4
{}^4T_5
{}^5T_6
}
\]

This is forward kinematics.

---

# 8. Save Every Frame

```python
frames.append(T.copy())
```

Instead of storing only the end-effector pose, we store every frame:

```text
frames[0] → Frame 0
frames[1] → Frame 1
frames[2] → Frame 2
frames[3] → Frame 3
frames[4] → Frame 4
frames[5] → Frame 5
frames[6] → Frame 6
```

This lets us visualize the entire kinematic chain and eventually draw the DH coordinate frames.

---

# 9. Initial Joint Configuration

```python
q = np.zeros(6)
```

This creates:

\[
q=[0,0,0,0,0,0]
\]

So initially all six joints are at:

\[
0^\circ
\]

---

# 10. Calculate the Initial FK

```python
frames = forward_kinematics(q)
```

This calculates:

\[
T_0,T_1,T_2,\ldots,T_6
\]

The overall process is:

```text
[0,0,0,0,0,0]
       │
       ▼
      DH
       │
       ▼
A₁ A₂ A₃ A₄ A₅ A₆
       │
       ▼
T₀ T₁ T₂ T₃ T₄ T₅ T₆
```

---

# 11. Print the Transformation Matrices

```python
for i, T in enumerate(frames):

    print(f"\nFrame {i}")
    print(T)
```

This is mainly for debugging and learning.

It allows us to inspect:

\[
{}^0T_0,\ {}^0T_1,\ {}^0T_2,\ldots,{}^0T_6
\]

and verify that the mathematics is producing sensible results.

---

# 12. Extract Frame Origins

A homogeneous transformation has the structure:

\[
T=
\begin{bmatrix}
R&p\\
0&1
\end{bmatrix}
\]

where:

- \(R\) = rotation/orientation
- \(p\) = position

The position is:

\[
p=
\begin{bmatrix}
x\\y\\z
\end{bmatrix}
\]

The code:

```python
points = np.array([
    T[:3, 3]
    for T in frames
])
```

extracts the position from every frame.

`T[:3, 3]` means:

> Take rows 0–2 of column 3.

The result is:

```text
[x, y, z]
```

for each frame.

Therefore:

```text
points =
[
    [x0, y0, z0],
    [x1, y1, z1],
    ...
    [x6, y6, z6]
]
```

These are the seven frame origins.

---

# 13. Create the 3D Figure

```python
fig = plt.figure()

ax = fig.add_subplot(111, projection="3d")
```

This creates the Matplotlib 3D environment.

---

# 14. Plot the Kinematic Skeleton

```python
ax.plot(
    points[:, 0],
    points[:, 1],
    points[:, 2],
    marker="o"
)
```

This connects:

\[
(x_0,y_0,z_0)
\rightarrow
(x_1,y_1,z_1)
\rightarrow
\ldots
\rightarrow
(x_6,y_6,z_6)
\]

The markers indicate the frame/joint origins.

At this stage, this is not a detailed physical model of the PUMA.

It is the robot's **kinematic skeleton**.

---

# 15. Label the 3D Axes

```python
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
```

These labels make the world coordinate system clear.

---

# 16. Reserve Space for Sliders

```python
plt.subplots_adjust(bottom=0.30)
```

This moves the plotting area upward and reserves space for six sliders at the bottom.

---

# 17. Create Slider Locations

```python
slider_axes = []

for i in range(6):

    slider_axes.append(
        plt.axes([
            0.20,
            0.25 - i * 0.035,
            0.65,
            0.025
        ])
    )
```

This creates six rectangular regions where the sliders will be placed.

---

# 18. Create the Six Joint Sliders

```python
sliders = []

for i in range(6):

    slider = Slider(
        slider_axes[i],
        f"q{i+1}",
        -180,
        180,
        valinit=0
    )

    sliders.append(slider)
```

This creates:

```text
q1   -180 ─────●───── +180
q2   -180 ─────●───── +180
q3   -180 ─────●───── +180
q4   -180 ─────●───── +180
q5   -180 ─────●───── +180
q6   -180 ─────●───── +180
```

Each slider represents one joint angle.

The sliders use degrees because that is easier to interact with visually.

---

# 19. `update()` — The Live Simulation Loop

```python
def update(val):
```

This function executes whenever a slider changes.

---

## 19.1 Read the Slider Values

```python
for i in range(6):

    q[i] = np.radians(sliders[i].val)
```

The sliders produce degrees.

For example:

\[
45^\circ
\]

But NumPy's trigonometric functions use radians.

Therefore:

```python
np.radians(45)
```

produces approximately:

\[
0.7854\text{ rad}
\]

The internal `q` array therefore stays in radians.

---

# 20. Recalculate Forward Kinematics

```python
frames = forward_kinematics(q)
```

This is where the robot actually responds to the slider.

Suppose:

\[
q_2:0^\circ\rightarrow45^\circ
\]

Then:

```text
q changes
 ↓
DH transformation changes
 ↓
A₂ changes
 ↓
T₂ changes
 ↓
T₃ changes
 ↓
T₄ changes
 ↓
T₅ changes
 ↓
T₆ changes
 ↓
Robot moves
```

This is the core of the interactive simulation.

---

# 21. Extract New Positions

```python
points = np.array([
    T[:3, 3]
    for T in frames
])
```

Again, the position \((x,y,z)\) of each frame is extracted from its transformation matrix.

---

# 22. Update the Existing Plot

```python
line.set_data(
    points[:, 0],
    points[:, 1]
)

line.set_3d_properties(
    points[:, 2]
)
```

Instead of deleting and recreating the robot, the existing plotted line is updated with new coordinates.

This is more efficient.

The `line` object must be created **before** the sliders can call `update()`:

```python
line, = ax.plot(
    points[:, 0],
    points[:, 1],
    points[:, 2],
    marker="o"
)
```

---

# 23. Redraw the Figure

```python
fig.canvas.draw_idle()
```

This tells Matplotlib:

> The data changed. Refresh the visualization.

---

# 24. Connect Sliders to the Update Function

```python
for slider in sliders:

    slider.on_changed(update)
```

This establishes the event connection.

It means:

> Whenever any slider changes, call `update()`.

Without this connection, the sliders would exist but would not move the robot.

---

# 25. Start the GUI Event Loop

```python
plt.show()
```

This displays the simulator and waits for user interaction.

---

# 26. Complete Interactive Simulation Pipeline

The complete process is:

```text
                  USER
                   │
                   ▼
             Move slider
                   │
                   ▼
             q₁ ... q₆
                   │
                   ▼
          forward_kinematics()
                   │
                   ▼
           DH transformations
                   │
                   ▼
          A₁ A₂ A₃ A₄ A₅ A₆
                   │
                   ▼
             T₀ ... T₆
                   │
                   ▼
            Frame origins
                   │
                   ▼
              x, y, z
                   │
                   ▼
             3D Matplotlib
                   │
                   └──────► visual update
```

---

# 27. The Robotics Concepts You've Implemented

Your code is now implementing several fundamental robotics concepts.

## Configuration

\[
\boxed{
q=[q_1,q_2,q_3,q_4,q_5,q_6]
}
\]

This describes the robot's current configuration.

↓

## DH Model

\[
\boxed{
(a_i,\alpha_i,d_i,\theta_i)
}
\]

This describes the kinematic structure.

↓

## Homogeneous Transformations

\[
\boxed{
{}^{i-1}T_i
}
\]

These describe the relationship between consecutive coordinate frames.

↓

## Forward Kinematics

\[
\boxed{
{}^0T_6=
\prod_{i=1}^{6}{}^{i-1}T_i
}
\]

This determines the pose of the end effector.

↓

## Position

\[
\boxed{
p_{EE}={}^0T_6[0:3,3]
}
\]

This extracts the end-effector position.

↓

## Visualization

The transformations are converted into frame origins and plotted in 3D.

---

# 28. What the Simulator Is Actually Doing

At a deeper level, you've built:

```text
           q
           │
           ▼
    ┌──────────────┐
    │ DH Parameters│
    └──────┬───────┘
           │
           ▼
      A₁, A₂, ..., A₆
           │
           ▼
     ┌─────────────┐
     │     FK      │
     └──────┬──────┘
            │
            ▼
      T₀,T₁,...,T₆
            │
            ▼
       Robot pose
            │
            ▼
       Visualization
```

And because the sliders continuously modify \(q\):

```text
Slider
  ↓
q changes
  ↓
FK recalculates
  ↓
Pose changes
  ↓
Plot updates
```

That is what makes it an **interactive kinematic simulator** rather than a static plot.

---

# 29. Current Limitations

The current simulator is deliberately simple.

It currently visualizes:

- joint/frame origins
- links as straight lines
- six joint variables
- forward kinematics

It does **not yet** show:

- coordinate axes \(x_i,y_i,z_i\)
- frame labels
- the actual PUMA mechanical geometry
- end-effector orientation indicators
- inverse kinematics
- Jacobian
- workspace
- trajectory generation
- velocity/acceleration
- dynamics

These can be added progressively.

---

# 30. Recommended Next Step

The next useful upgrade is to visualize the actual DH coordinate frames:

```text
Frame 0 → x₀ y₀ z₀
Frame 1 → x₁ y₁ z₁
Frame 2 → x₂ y₂ z₂
...
Frame 6 → x₆ y₆ z₆
```

Because:

\[
T_i=
\begin{bmatrix}
R_i&p_i\\
0&1
\end{bmatrix}
\]

contains both:

- \(p_i\) → frame origin
- \(R_i\) → frame orientation

The columns of \(R_i\) give the frame axes:

\[
x_i = T_i[0:3,0]
\]

\[
y_i = T_i[0:3,1]
\]

\[
z_i = T_i[0:3,2]
\]

Adding these to the simulator will let you **visually compare the moving DH frame assignments with the PUMA 560 diagram from Craig**.

That is the natural next step before moving on to inverse kinematics, Jacobians, or trajectory planning.
