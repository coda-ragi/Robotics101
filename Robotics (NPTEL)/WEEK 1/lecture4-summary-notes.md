# Lecture 04 : Introduction to Robots and Robotics(Contd.)

### Introduction

This lecture delves deeper into the fascinating world of robotics, building upon previous discussions to explore the fundamental principles governing robot design and operation. We begin by applying Grubler's criterion, a powerful tool for determining the degrees of freedom (DOF) of complex manipulators, to a spatial parallel robot known as the Stewart platform. Understanding a robot's DOF is crucial as it dictates the range and type of motion an end-effector can achieve, directly impacting its utility in various applications.

Beyond mechanical analysis, the lecture systematically classifies robots based on their operational characteristics, control mechanisms, and structural configurations. From robots designed for precise, discrete tasks to those capable of continuous, intricate movements, and from open-loop systems to sophisticated closed-loop feedback control, this session provides a comprehensive overview. We also explore how different coordinate systems influence robot design and functionality, and the critical concept of a robot's workspace—the physical volume it can access—distinguishing between reachable and dextrous capabilities. This foundational knowledge is essential for anyone looking to understand, design, or apply robotic systems effectively in real-world scenarios.

### Core Concepts

| Term | Definition | Significance |
| :--- | :--- | :--- |
| **`Grubler's Criterion`** | A formula used to calculate the degrees of freedom (mobility) of a mechanism, considering the number of links, joints, and their respective constraints. | Essential for predicting a robot's potential motion capabilities and designing manipulators with desired flexibility. |
| **`Stewart Platform`** | A type of parallel manipulator characterized by a base and a top plate connected by six legs, each typically with a universal, prismatic, and spherical joint. | A prime example of a spatial parallel manipulator with high stiffness and load-carrying capacity, often used in flight simulators. |
| **`Point-to-Point Robot`** | A robot designed to move its end-effector between discrete, pre-specified locations, where the tool is not continuously in contact with the workpiece. | Suitable for tasks like drilling or pick-and-place operations where intermediate path accuracy is less critical than endpoint precision. |
| **`Continuous Path Robot`** | A robot designed to maintain continuous contact with a workpiece while tracing a complex, predefined trajectory. | Ideal for tasks requiring continuous motion and precise path control, such such as welding, painting, or milling. |
| **`Non-Servo-Controlled Robot`** | A robot that operates using an open-loop control system, meaning it does not measure its output for comparison or error compensation. | Simpler and less expensive, but also less accurate due to the lack of feedback to correct for deviations. |
| **`Servo-Controlled Robot`** | A robot that utilizes a closed-loop control system with feedback devices to measure output, compare it to desired input, and correct for errors. | Offers higher accuracy and precision, making it suitable for complex and demanding tasks, though at a higher cost. |
| **`Cartesian Coordinate Robot`** | A robot whose movements are defined along three independent linear axes (X, Y, Z), typically using prismatic or sliding joints. | Known for high rigidity and accuracy, making them excellent for pick-and-place or assembly tasks requiring precise linear motion. |
| **`Revolute Coordinate Robot`** | Also known as an articulated robot, it features three rotary joints, allowing for complex, human-arm-like movements. | Highly versatile and widely used in industries for a variety of tasks, despite potential dynamic performance limitations due to rotary joints. |
| **`Workspace`** | The total volume of space that the end-effector of a manipulator can reach. | Defines the operational envelope of a robot, crucial for task planning and determining if a robot can perform a specific job. |
| **`Reachable Workspace`** | The volume of space that the end-effector can reach with at least one orientation. | Represents the maximum physical extent a robot can cover, often larger than the dextrous workspace. |
| **`Dextrous Workspace`** | The volume of space that the end-effector can reach with any orientation. | A subset of the reachable workspace, indicating areas where the robot has full orientational flexibility, critical for complex manipulation. |

### Detailed Analysis

#### 1. Degrees of Freedom Calculation for a Spatial Parallel Manipulator

The lecture demonstrates the application of Grubler's criterion to determine the degrees of freedom (DOF) for a spatial parallel manipulator, specifically a Stewart platform. This manipulator consists of a top plate and a fixed base connected by six identical legs. Each leg comprises a universal joint, a prismatic joint, and a spherical joint.

To apply Grubler's criterion (DOF = 6n - Σ(6-Ci)), we first identify the key parameters:
* **Number of Moving Links (n):** Each of the six legs has two moving links (between the universal and prismatic, and between the prismatic and spherical joints). Additionally, the top plate is considered one moving link. Thus, n = (6 legs * 2 links/leg) + 1 top plate = 12 + 1 = 13.
* **Number of Joints (m):** Each leg has three joints (universal, prismatic, spherical). With six legs, the total number of joints is m = 6 legs * 3 joints/leg = 18.
* **Constraints per Joint (6-Ci):**
* **Universal Joint:** Has 2 degrees of freedom, so it imposes 6 - 2 = 4 constraints.
* **Prismatic Joint:** Has 1 degree of freedom, so it imposes 6 - 1 = 5 constraints.
* **Spherical Joint:** Has 3 degrees of freedom, so it imposes 6 - 3 = 3 constraints.
* **Total Constraints per Leg:** For one leg, the total constraints are 4 (universal) + 5 (prismatic) + 3 (spherical) = 12 constraints.
* **Total Constraints for the Manipulator:** Since there are six such legs, the total constraints imposed by all joints are 12 constraints/leg * 6 legs = 72 constraints.

Finally, applying Grubler's criterion:
DOF = (6 * n) - (Total Constraints)
DOF = (6 * 13) - 72
DOF = 78 - 72 = 6

This calculation reveals that the Stewart platform has 6 degrees of freedom, meaning its top plate can achieve three independent translations and three independent rotations relative to the fixed base. This makes it an ideal spatial manipulator, often used in applications like flight simulators for pilot training.

#### 2. Robot Classification by Task

Robots are often categorized based on the nature of the tasks they perform:

* **Point-to-Point (PTP) Robots:** These robots are designed to move their end-effector to a series of discrete, pre-defined points. The path taken between these points is not critical, as the tool is typically withdrawn from the workpiece during transit. An example is a robot drilling holes at specific locations on a steel plate; it drills at point 1, withdraws, moves to point 2, drills, and so on. Examples include Unimate 2000 and T3 (The Tomorrow Tool).
* **Continuous Path (CP) Robots:** In contrast, CP robots are required to maintain continuous contact with the workpiece while tracing a precise, complex trajectory. The accuracy of the entire path is crucial. An example is a robot using a milling cutter to cut a complicated profile on a steel plate, where the cutter must rotate and follow the contour continuously. Examples include PUMA and CRS robots. A key distinction is that a continuous path robot can perform point-to-point tasks, but a point-to-point robot cannot typically perform continuous path tasks due to its control limitations.

#### 3. Robot Classification by Controller Type

The control system employed is another fundamental way to classify robots:

* **Non-Servo-Controlled Robots:** These robots utilize an open-loop control system. In this setup, an input command is sent to the robot, but there is no feedback mechanism to measure the actual output or compare it with the desired input. Consequently, there is no error detection or compensation. While simpler and less expensive (e.g., Seiko PN-100), they are inherently less accurate because they cannot correct for disturbances or inaccuracies in their movements.
* **Servo-Controlled Robots:** These robots employ a closed-loop control system, which is characterized by the presence of feedback. The system measures the robot's actual output (e.g., position, velocity), compares it to the desired input, calculates the error, and then uses this error signal to adjust the robot's actuators. This continuous feedback loop allows for precise control and error minimization, making servo-controlled robots (e.g., Unimate 2000, PUMA, T3) more accurate and suitable for demanding tasks, albeit at a higher cost.

#### 4. Robot Classification by Coordinate System

The geometric configuration of a robot's joints and links, often described by the coordinate system it operates within, leads to several common types:

* **Cartesian Coordinate Robot:** These robots feature three independent linear movements along the X, Y, and Z axes, typically achieved using prismatic or sliding joints. They are often referred to as PPP (Prismatic-Prismatic-Prismatic) or SSS (Sliding-Sliding-Sliding) robots. Cartesian robots are known for their high rigidity and accuracy, making them suitable for tasks requiring precise linear motion, such as pick-and-place operations or assembly. Examples include IBM's RS-1 and Olivetti's Sigma robot.
* **Cylindrical Coordinate Robot:** This type combines two linear joints and one rotary (twisting) joint. For instance, a TSS (Twisting-Sliding-Sliding) or TPP (Twisting-Prismatic-Prismatic) configuration. They offer horizontal and vertical reach, but their rotary joint can lead to poorer dynamic performance compared to Cartesian robots. They may also have limitations in reaching objects directly on the floor. Versatran 600 is a typical example.
* **Spherical Coordinate Robot (Polar Coordinate Robot):** These robots typically have one linear joint and two rotary joints (one twisting, one revolute). This configuration allows for a spherical workspace. While capable of reaching objects on the floor, they also suffer from dynamic performance issues due to the presence of rotary joints. An example is Unimate 2000B.
* **Revolute Coordinate Robot (Articulated Robot):** Characterized by three rotary joints, often configured as a TRR (Twisting-Revolute-Revolute) robot, mimicking the structure of a human arm. These robots are highly versatile and widely used in industries for tasks like drilling, milling, and complex pick-and-place operations. Despite their flexibility, the multiple rotary joints can sometimes lead to dynamic performance challenges. PUMA, T3, and CRS are prominent examples.

#### 5. Robot Classification by Mobility Levels

Robots can also be classified based on whether their base is fixed or mobile:

* **Robots with Fixed Base (Manipulators):** These are stationary robots, often referred to as manipulators. They can be further divided into:
* **Serial Manipulators:** Links and joints are arranged in a series, like the PUMA or CRS robots. They generally have a larger workspace but lower load-carrying capacity.
* **Parallel Manipulators:** Links are arranged in parallel, like the Stewart platform. They typically have higher stiffness and load-carrying capacity but a smaller workspace.
* **Robots with Moving Base (Mobile Robots):** These robots are designed for locomotion and can move across different terrains. They include:
* **Wheeled Robots:** Suitable for smooth terrains, often used for navigation and transport. A simple example is a two-wheeled, one-caster robot.
* **Tracked Robots:** Designed for terrains that are neither perfectly smooth nor extremely rough, offering good traction.
* **Multi-legged Robots:** Best suited for very rough or uneven terrains, including stairs, as they can adapt their gait. Examples include 4-legged or 6-legged robots, where each leg typically has 3 degrees of freedom.

#### 6. Understanding Robot Workspace

The **workspace** of a manipulator is the volume of space that its end-effector can reach. It's a critical concept for determining a robot's operational capabilities. The lecture distinguishes between two types of workspace:

* **Reachable Workspace:** This is the total volume of space that the robot's end-effector can reach with at least one possible orientation. For a simple 2-DOF planar manipulator, this might be a large circle defined by the maximum extension of its links.
* **Dextrous Workspace:** This is a more restrictive volume within the reachable workspace, representing the space where the end-effector can reach with *any* desired orientation. The dextrous workspace is always a subset of the reachable workspace. For the 2-DOF example, a point on the outer boundary of the reachable circle might only be reachable with one specific orientation, while a point inside the circle could be reached with multiple orientations, thus falling within the dextrous workspace. Understanding this distinction is vital for tasks requiring complex manipulation and orientation changes.

### Key Takeaways
- [ ] Grubler's criterion is a fundamental tool for calculating a robot's degrees of freedom, crucial for understanding its motion capabilities.
- [ ] The Stewart platform is a 6-DOF spatial parallel manipulator, known for its high load capacity and use in applications like flight simulators.
- [ ] Robots are classified by task into point-to-point (discrete movements) and continuous path (continuous contact, precise trajectory) types.
- [ ] Control systems differentiate robots into non-servo-controlled (open-loop, less accurate) and servo-controlled (closed-loop, more accurate with feedback).
- [ ] Robot configurations are categorized by coordinate systems: Cartesian (linear, rigid), Cylindrical (linear + rotary), Spherical (linear + 2 rotary), and Revolute (3 rotary, versatile).
- [ ] Robots can have a fixed base (manipulators like serial or parallel types) or a moving base (mobile robots like wheeled, tracked, or multi-legged).
- [ ] The workspace defines the operational volume of a robot's end-effector, critical for task planning.
- [ ] Reachable workspace is the total volume reachable with any orientation, while dextrous workspace is a subset where all orientations are possible.

### Conclusion

This lecture has provided a comprehensive framework for understanding the intricate world of robotics, moving from the foundational mechanics of degrees of freedom to the diverse classifications that define robot capabilities and applications. By applying Grubler's criterion, we demystified the mobility of complex systems like the Stewart platform, highlighting how structural design directly translates into functional potential. The detailed exploration of robot types—categorized by task, control system, coordinate geometry, and mobility—underscores the vast spectrum of robotic solutions available today.

From the precision of servo-controlled Cartesian robots in manufacturing to the adaptability of multi-legged mobile robots navigating challenging terrains, each classification serves a unique purpose. The critical distinction between reachable and dextrous workspaces further refines our understanding of a robot's true operational envelope. This knowledge is not merely academic; it forms the bedrock for selecting the right robot for a specific industrial task, designing innovative new robotic systems, or even conceptualizing future autonomous agents. As robotics continues to evolve, a firm grasp of these core principles will remain indispensable for engineers, researchers, and enthusiasts alike.