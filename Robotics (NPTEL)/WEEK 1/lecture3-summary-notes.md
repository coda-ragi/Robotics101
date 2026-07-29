# Lecture 03 : Introduction to Robots and Robotics(Contd.)

### Introduction

Robots, from industrial manipulators to advanced autonomous systems, are fundamentally defined by their structure and how they move. Understanding these aspects is crucial for their design, control, and application. This lecture delves into the symbolic representation of robot joints, the construction of kinematic diagrams, and the critical concept of Degrees of Freedom (DOF) and mobility. By learning to represent complex robotic systems using simplified symbols, we can systematically analyze their potential movements and capabilities. This foundational knowledge is essential for subsequent studies in kinematics, dynamics, and control, ultimately paving the way for developing intelligent and autonomous robotic systems. The ability to quantify a robot's freedom of movement allows engineers to design manipulators perfectly suited for specific tasks, whether it's a precise surgical robot or a robust industrial arm.

### Core Concepts

| Term | Definition | Significance |
| :--- | :--- | :--- |
| **`Revolute Joint (R)`** | A rotary joint allowing relative rotation between two links about a single axis. | Fundamental for rotational movement in most robot arms, providing 1 degree of freedom. |
| **`Prismatic Joint (P)`** | A linear joint allowing relative translational movement between two links along a single axis. | Essential for linear extension or retraction, providing 1 degree of freedom. |
| **`Cylindrical Joint (C)`** | A joint allowing both rotation about an axis and translation along the same axis. | Combines features of revolute and prismatic joints, offering 2 degrees of freedom. |
| **`Spherical Joint (S')`** | A ball-and-socket joint allowing rotation about three orthogonal axes. | Provides 3 degrees of freedom, crucial for complex orientation changes, often found in wrists. |
| **`Hooke Joint (U)`** | Also known as a universal joint, it allows rotation about two intersecting axes. | Offers 2 degrees of freedom, useful for transmitting torque between shafts at an angle. |
| **`Twisting Joint (T)`** | A type of rotary joint that allows rotation about an axis, often used for wrist movements. | Provides 1 degree of freedom, similar to a revolute joint but specifically named for twisting actions. |
| **`Kinematic Diagram`** | A simplified representation of a robot manipulator using standard symbols for joints and links. | Essential for visualizing robot structure and performing kinematic analysis without physical complexity. |
| **`Degrees of Freedom (DOF)`** | The minimum number of independent parameters (variables or coordinates) required to completely describe the position and orientation of a system. | Defines the robot's ability to move and position its end-effector in space; crucial for task planning. |
| **`Redundant Manipulator`** | A manipulator with more degrees of freedom than strictly necessary to perform a given task. | Offers increased dexterity, obstacle avoidance, and the ability to perform tasks in constrained environments. |
| **`Under-actuated Manipulator`** | A manipulator with fewer degrees of freedom than ideally required for a given task. | May be simpler and cheaper but has limited dexterity and workspace for certain applications. |
| **`Mobility (M)`** | A term often used interchangeably with DOF, especially when the calculated DOF exceeds the ideal maximum (e.g., 6 for spatial, 3 for planar). | Quantifies the total independent movements possible, distinguishing from the "ideal" DOF for a task. |
| **`Grubler's Criterion`** | A formula used to calculate the mobility (or degrees of freedom) of a kinematic chain. | Provides a systematic method to determine a robot's overall freedom of movement based on its links and joints. |

### Detailed Analysis

#### 1. Representing Robot Joints and Kinematic Diagrams

To effectively analyze and design robotic systems, a standardized method for representing their structure is indispensable. This involves using specific symbols for different types of joints.

* **Joint Symbols**:
* **Revolute Joint (R)**: Denoted by 'R' or specific graphical symbols indicating rotation. It provides one degree of freedom (DOF).
* **Prismatic Joint (P)**: Denoted by 'P' or symbols indicating linear translation. It also provides one DOF.
* **Cylindrical Joint (C)**: Denoted by 'C', allowing both rotation and translation along the same axis, thus offering two DOFs.
* **Spherical Joint (S')**: Denoted by 'S'' or a symbol representing a ball-and-socket joint. It provides three DOFs, allowing rotation about three orthogonal axes.
* **Hooke Joint (U)**: Denoted by 'U', also known as a universal joint, allowing rotation about two intersecting axes, providing two DOFs.
* **Twisting Joint (T)**: Denoted by 'T', a type of rotary joint specifically for twisting motion, offering one DOF.

* **Constructing a Kinematic Diagram**:
A kinematic diagram simplifies a complex robotic system into its fundamental components: fixed base, links, and joints. The process begins from the fixed base and proceeds through each joint and link to the end-effector.
* **Example**: For a serial manipulator, one might start with a fixed base.
* If the first joint is a twisting joint, it's represented by its 'T' symbol.
* Subsequent joints, such as revolute joints, are added using their respective 'R' symbols.
* The diagram progresses, connecting each joint and link in sequence.
* The final element is the end-effector, often represented by a distinct symbol, connected by the last joint (e.g., a revolute joint).
* This symbolic representation allows engineers to quickly grasp the robot's configuration and prepare for kinematic analysis, which is the starting point for understanding its motion, dynamics, and control.

#### 2. Understanding Degrees of Freedom (DOF)

The Degrees of Freedom (DOF) of a robotic system is defined as the minimum number of independent parameters, variables, or coordinates required to completely describe its position and orientation.

* **Basic Examples of DOF**:
* **Point in 2D Plane**: Requires two coordinates (x, y), hence 2 DOFs.
* **Point in 3D Space**: Requires three coordinates (x, y, z), hence 3 DOFs.
* **Rigid Body in 3D Space**: Requires three parameters for position (x, y, z of its mass center) and three parameters for orientation (e.g., rotations about X, Y, Z axes). Therefore, a rigid body in 3D space has 6 DOFs.
* **Ideal Manipulator DOFs**:
* **Spatial Manipulator**: To manipulate a 3D object in 3D space (e.g., gripping an object in any position and orientation), an ideal spatial manipulator should have 6 DOFs. This is why most industrial robots, like the PUMA (Programmable Universal Machine for Assembly), are designed with 6 DOFs.
* **Planar Manipulator**: For tasks confined to a 2D plane, an ideal planar manipulator should have 3 DOFs (two for position, one for orientation within the plane).

#### 3. Redundant and Under-actuated Manipulators

While ideal manipulators have specific DOFs, real-world applications often necessitate deviations from these ideals, leading to redundant or under-actuated designs.

* **Redundant Manipulators**:
* A spatial manipulator with more than 6 DOFs (e.g., 7 or 8 DOFs) or a planar manipulator with more than 3 DOFs (e.g., 4 or 5 DOFs) is considered redundant.
* **Significance**: Redundancy provides enhanced dexterity, allowing the robot to reach difficult positions, avoid obstacles, or optimize its posture during a task.
* **Example**: Performing welding in a highly constrained and hard-to-reach area might require a serial manipulator with 8 revolute joints, thus having more than 6 DOFs. This extra freedom allows the end-effector to reach the target while navigating complex geometry.
* **Under-actuated Manipulators**:
* A spatial manipulator with less than 6 DOFs or a planar manipulator with less than 3 DOFs is under-actuated.
* **Significance**: These manipulators are often simpler and less expensive but have limited dexterity and workspace. They are suitable for tasks where high accuracy or complex movements are not critical.
* **Example**: A spatial manipulator like the "Minimover" with 5 DOFs is under-actuated. It might be used for pick-and-place operations where the exact orientation of the object is not always critical.
* **Illustrative Analogy (Whiteboard Cleaning)**:
* **Task**: Cleaning a 2D whiteboard.
* **Ideal Planar Manipulator**: A duster that can move along X, Y, and rotate about Z (perpendicular to the board) has 3 DOFs. This is ideal for the task.
* **Under-actuated Planar Manipulator**: A duster that can only move along X and Y has 2 DOFs. It cannot rotate, making it under-actuated for the task.
* **Redundant Planar Manipulator**: A duster that can move along X, Y, Z (even if Z is constrained to the board's surface), and rotate about Z, effectively having 4 DOFs. This provides redundancy, allowing for more flexible cleaning paths or postures.

#### 4. Mobility and Grubler's Criterion

Mobility (M) is a quantitative measure of a robot's degrees of freedom, calculated using Grubler's criterion. It helps determine the total number of independent motions a manipulator can perform.

* **Distinction between DOF and Mobility**: While often used interchangeably, "mobility" is sometimes preferred when the calculated degrees of freedom exceed the "ideal" maximum (e.g., 6 for spatial, 3 for planar). A robot might have a mobility level of 10, rather than saying it has 10 DOFs, to emphasize that 6 is the maximum for full spatial manipulation.

* **Grubler's Criterion for Spatial Manipulators (3D)**:
* Considers a manipulator with `n` rigid moving links and `m` joints.
* Each rigid body in 3D space has 6 DOFs. So, `n` links initially have `6n` total DOFs.
* Each joint `i` has a connectivity `Ci` (number of DOFs it provides).
* A joint with connectivity `Ci` imposes `(6 - Ci)` constraints on the system.
* The total number of constraints from `m` joints is `Σ(6 - Ci)` for `i = 1 to m`.
* The mobility `M` is given by: `M = 6n - Σ(6 - Ci)`

* **Grubler's Criterion for Planar Manipulators (2D)**:
* For a planar manipulator, each rigid body in 2D space has 3 DOFs. So, `n` links initially have `3n` total DOFs.
* Each joint `i` with connectivity `Ci` imposes `(3 - Ci)` constraints on the system.
* The total number of constraints from `m` joints is `Σ(3 - Ci)` for `i = 1 to m`.
* The mobility `M` is given by: `M = 3n - Σ(3 - Ci)`

#### 5. Applying Grubler's Criterion: Examples

Let's apply Grubler's criterion to calculate the mobility of different manipulator types.

* **Example 1: Serial Planar Manipulator**
* **Configuration**: Fixed base, followed by a revolute joint, a second revolute joint, a prismatic joint, and a final revolute joint connected to an end-effector. All joints are planar.

* **Parameters**:
* Number of moving links (`n`): 4 (excluding the fixed base).
* Number of joints (`m`): 4 (R, R, P, R).
* Connectivity of each joint (`Ci`): All revolute and prismatic joints in a planar system have `Ci = 1`.

* **Calculation**:
* Total initial DOFs: `3n = 3 * 4 = 12`.
* Constraints per joint: `(3 - Ci) = (3 - 1) = 2`.
* Total constraints: `Σ(3 - Ci) = 4 * 2 = 8`.
* Mobility `M = 3n - Σ(3 - Ci) = 12 - 8 = 4`.
* **Conclusion**: This planar manipulator has a mobility of 4. Since an ideal planar manipulator has 3 DOFs, this is a **redundant planar serial manipulator**. For serial manipulators, the mobility often equals the sum of the connectivities of its joints (1+1+1+1 = 4 in this case).

* **Example 2: Parallel Planar Manipulator**
* **Configuration**: A fixed base connected to a top plate (end-effector) via three parallel legs. Each leg consists of a revolute joint, a prismatic joint, and another revolute joint.

* **Parameters**:
* Number of moving links (`n`): Each leg has 2 moving links (between the joints), plus the top plate as 1 moving link. So, `n = (3 * 2) + 1 = 7`.
* Number of joints (`m`): Each leg has 3 joints (R, P, R). So, `m = 3 * 3 = 9`.
* Connectivity of each joint (`Ci`): All revolute and prismatic joints in a planar system have `Ci = 1`.

* **Calculation**:
* Total initial DOFs: `3n = 3 * 7 = 21`.
* Constraints per joint: `(3 - Ci) = (3 - 1) = 2`.
* Total constraints: `Σ(3 - Ci) = 9 * 2 = 18`.
* Mobility `M = 3n - Σ(3 - Ci) = 21 - 18 = 3`.
* **Conclusion**: This planar parallel manipulator has a mobility of 3. This indicates it is an **ideal parallel planar manipulator**, capable of controlling 3 DOFs in a plane.

### Key Takeaways
- [ ] Robot joints are represented by specific symbols (R, P, C, S', U, T) to simplify complex manipulator structures.
- [ ] Kinematic diagrams are essential for visualizing robot structure and are the starting point for kinematic analysis.
- [ ] Degrees of Freedom (DOF) define the minimum independent parameters needed to describe a robot's position and orientation.
- [ ] An ideal spatial manipulator requires 6 DOFs, while an ideal planar manipulator requires 3 DOFs.
- [ ] Redundant manipulators have more DOFs than ideal, offering increased dexterity and obstacle avoidance.
- [ ] Under-actuated manipulators have fewer DOFs than ideal, leading to simpler designs but limited capabilities.
- [ ] Mobility is a general term for the number of independent motions, often used when calculated DOFs exceed the ideal maximum.
- [ ] Grubler's Criterion (M = 6n - Σ(6 - Ci) for spatial, M = 3n - Σ(3 - Ci) for planar) is a fundamental formula for calculating a robot's mobility.
- [ ] The application of Grubler's Criterion allows for the classification of manipulators as ideal, redundant, or under-actuated for specific tasks.

### Conclusion

The ability to symbolically represent robot joints and construct kinematic diagrams provides a universal language for robotics engineers. This lecture has laid the groundwork for understanding how a robot's physical structure translates into its potential for movement. By defining and calculating Degrees of Freedom and mobility using tools like Grubler's Criterion, we gain critical insights into a robot's capabilities and limitations. This understanding is not merely theoretical; it directly informs the design choices for industrial robots, surgical instruments, and autonomous vehicles, ensuring they possess the appropriate level of dexterity and control for their intended applications. As we move forward into kinematics, dynamics, and control, these foundational concepts will serve as the essential blueprint for analyzing and predicting robot behavior, ultimately enabling the creation of more intelligent and versatile robotic systems.