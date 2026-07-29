# Lecture 01 : Introduction to Robots and Robotics

### Introduction

Have you ever wondered about the machines that perform complex tasks with precision, or the science behind their creation? This lecture embarks on a journey into the fascinating realm of robots and robotics, addressing fundamental questions that often arise when contemplating these advanced technologies. We will explore what defines a robot, the multidisciplinary field of robotics, the compelling motivations behind its study, and how these intelligent machines are instructed to execute diverse tasks. From their historical origins to their modern-day applications and the intricate components that enable their functionality, this session lays the groundwork for understanding the profound impact of robotics on our world. By the end, you will grasp the core concepts and appreciate why robotics is an indispensable area of study in today's dynamic landscape.

### Core Concepts

| Term | Definition | Significance |
| :--- | :--- | :--- |
| **`robot`** | Derived from the Czech word 'robota' meaning 'forced or slave laborer', it refers to a machine capable of carrying out complex actions automatically, often programmable by a computer. | This foundational term highlights the historical perception of robots as automated servants and their evolution into sophisticated, programmable machines. |
| **`robotics`** | The science concerned with the design, development, and application of robots to perform a variety of tasks, drawing from multiple engineering and scientific disciplines. | It defines the academic and industrial field dedicated to creating and utilizing robots, emphasizing its multidisciplinary nature and broad scope. |
| **`manipulator`** | A type of robot characterized by a fixed base, designed to mimic the functions of a human hand, often used for tasks requiring precise movement and handling. | This term describes a common configuration of industrial robots, focusing on their mechanical arm-like structure and its role in performing physical tasks. |
| **`reprogrammability`** | The ability of a robot to be adapted to perform different tasks by simply changing its software program, rather than requiring physical retooling. | This feature is crucial for the versatility and economic viability of robots, allowing them to be used for a wide range of applications without significant hardware changes. |
| **`multifunctional`** | Describes a robot's capacity to perform various types of operations, such as machining, assembly, or pick-and-place tasks, using the same core hardware. | This characteristic underscores the adaptability of robots, making them valuable assets in environments requiring diverse operational capabilities. |
| **`flexible automation`** | An automation strategy that uses programmable machines, like robots, to handle a variety of products or tasks, particularly suited for batch production. | It represents a key advantage of robotics in manufacturing, enabling efficient production of different items in moderate quantities, unlike rigid fixed automation. |
| **`linear joint`** | A type of robotic joint that allows relative linear motion between two connected links, facilitating movement along a straight line. | These joints are fundamental for achieving translational movements in a robot's workspace, enabling precise positioning along an axis. |
| **`rotary joint`** | A type of robotic joint that allows relative rotational motion between two connected links, enabling movement around an axis. | These joints are essential for achieving angular movements and orientations, providing the robot with dexterity and reach. |
| **`revolute joint`** | A specific type of rotary joint where the axis of rotation is perpendicular to the axis of the output link, similar to a hinge. | This joint type is commonly found in robotic arms, allowing for bending and sweeping motions that mimic human limb movements. |
| **`twisting joint`** | A specific type of rotary joint where the axis of rotation coincides with the axis of the output link, allowing for a twisting motion. | This joint type provides rotational capability along the length of a link, crucial for orienting end-effectors or tools. |

### Detailed Analysis

#### 1. Defining Robots and the Field of Robotics

The journey into robotics begins with understanding its core terminology. The term "robot" itself has a rich history, originating from the Czech word 'robota', meaning "forced or slave laborer." This concept was popularized in 1921 by Czech playwright Karel Capek in his drama "Rossum’s Universal Robot (R.U.R)," where robots were depicted as human-like figures. However, modern definitions have evolved significantly.

- **Contemporary Definitions of a Robot**:
- **Oxford English Dictionary**: Defines a robot as "a machine capable of carrying out a complex series of actions automatically, especially one programmable by a computer." This highlights its autonomous and programmable nature.

- **International Organization for Standardization (ISO)**: Describes a robot as "an automatically controlled, reprogrammable, multifunctional manipulator, programmable in three or more axes, which can be either fixed in place or mobile for use in industrial automation applications." This definition emphasizes control, adaptability, versatility, and structural characteristics.

- **Robot Institute of America (RIA)**: Defines it as "a reprogrammable multi-functional manipulator designed to move materials, parts, tools or specialized devices through variable programmed motions for the performance of a variety of tasks." This definition underscores its purpose in material handling and task execution.

- **Key Characteristics of Robots**:
- **Automatically Controlled**: Robots operate without continuous human intervention, executing pre-programmed sequences.
- **Reprogrammable**: A single robot can perform diverse tasks by simply altering its software program. This offers a higher degree of flexibility compared to Computer Numerical Control (CNC) machines, which, while programmable, have a more limited scope of re-programmability. A CNC machine is not considered a robot due to this difference in flexibility.
- **Multifunctional**: Robots can perform various operations, such as machining, assembly, or pick-and-place, making them highly versatile.
- **Manipulator**: Often refers to a robot with a fixed base, designed to function like a mechanical hand. These can be serial or parallel manipulators.

- **Robotics as a Multidisciplinary Science**:
- The term "robotics" was coined by Isaac Asimov in 1942 in his story "Runaround."
- Robotics is a science that encompasses the design, development, and application of robots.
- It is inherently multidisciplinary, integrating principles from physics, mathematics, mechanical engineering, electrical and electronics engineering, and computer science. Becoming an expert in robotics requires a strong foundation across these diverse fields.
- A core ambition in robotics is to emulate human capabilities, often referred to as the "3 Hs": Hand (mechanical manipulators), Head (intelligence), and Heart (emotions), aiming for future robots that are both intelligent and emotional.

#### 2. Motivation and Applications of Robotics

The drive behind the development and study of robotics stems from critical demands in today's competitive global market. Businesses strive to achieve three primary objectives simultaneously: reduced production cost, increased productivity, and improved product quality. These goals are often conflicting, but automation, particularly flexible automation, provides a viable solution.

- **Market Imperatives Driving Robotics**:
- **Reduced Production Cost**: Automation can streamline processes, minimize waste, and optimize resource utilization.
- **Increased Productivity**: Robots can operate continuously, faster, and with greater consistency than human labor, leading to higher output.
- **Improved Product Quality**: Precision and repeatability inherent in robotic operations result in consistent, high-quality products.
- **Automation in Production**:
- **Piece Production**: Involves manufacturing small numbers of many different designs; typically not suitable for automation.
- **Batch Production**: Involves producing moderate numbers of a few designs; ideal for flexible automation, where robots can be reprogrammed for different batches.
- **Mass Production**: Involves producing large numbers of a single design; typically uses fixed or hard automation.
- **Robotics as Flexible Automation**:
- Robotics is a prime example of flexible automation, making it indispensable for batch production, especially in manufacturing units seeking to remain competitive.
- **Expanding Applications of Robots**:
- While initially prominent in manufacturing, robots now have diverse applications across various sectors:
- **Space Science**: Exploration and maintenance in extraterrestrial environments.
- **Medical Science**: Surgery, rehabilitation, and diagnostics.
- **Sea-bed Mining**: Exploration and extraction in harsh underwater conditions.
- **Agriculture**: Planting, harvesting, and monitoring crops.
- **Fire-fighting**: Operating in dangerous environments to suppress fires.
- **Logistics and Warehousing**: Material handling, sorting, and packaging.

#### 3. A Brief History of Robotics

The evolution of robotics is marked by significant milestones, from theoretical concepts to sophisticated intelligent machines.

- **Key Historical Developments**:
- **1950**: Numerical Controlled (NC) machines were first developed, preceding the first robot.
- **1954**: George Devol filed the first patent for a manipulator, earning him the title "father of robot."
- **1956**: Joseph Engelberger founded Unimation, the world's first robotics company.
- **1962**: General Motors deployed the Unimate manipulator for die-casting applications.
- **1967**: General Electric Operation demonstrated a functional 4-legged vehicle.
- **1969**: NASA built the SAM robot; Stanford Research Institute (SRI) developed Shakey, recognized as the first intelligent mobile robot.
- **1970**: Victor Scheinman demonstrated the Stanford Arm manipulator; the USSR sent Lunokhod 1 to the moon; Odetics built ODEX 1.
- **1973**: Richard Hohn of Cincinnati Milacron Corporation manufactured the T^3 (The Tomorrow Tool) robot.
- **1975**: Raibart at Carnegie Mellon University built a one-legged hopping machine, the first dynamically stable machine, and is known as the father of multi-legged robots.
- **1978**: Unimation developed PUMA (Programmable Universal Machine for Assembly), a widely used 6-degrees-of-freedom manipulator.
- **1983**: Odetics introduced a unique experimental six-legged device.
- **1986**: The Adaptive Suspension Vehicle (ASV) was developed by Ohio State University.
- **1997**: NASA's Pathfinder and Sojourner robots were sent to Mars, though the mission faced challenges.
- **2000**: Honda developed the Asimo humanoid robot.
- **2004**: Spirit and Opportunity successfully explored the surface of Mars.
- **2012**: NASA's Curiosity, an intelligent autonomous robot, successfully landed on Mars.
- **2015**: Hanson Robotics (Hong Kong) built Sophia, an advanced intelligent and emotional humanoid robot, capable of communication and interaction.

#### 4. Components of a Robotic System: Focus on Joints

A typical robotic system comprises several key components working in concert. At its heart is the robot itself, often a manipulator, supported by a drive unit and a controller. The manipulator's structure is defined by its links and the joints connecting them.

- **Basic Robotic System Architecture**:
- **Robot (Manipulator)**: The mechanical structure, often with a fixed base, designed to perform physical tasks.
- **Drive Unit**: Provides the power and motion to the manipulator's joints.
- **Controller**: The "brain" of the robot, directing its movements and operations based on programmed instructions.
- **Manipulator Structure**:
- **Fixed Base**: The stationary foundation of the manipulator.
- **Links**: Rigid components that transmit mechanical power and form the robot's "limbs."
- **Joints**: Connect the links and allow for relative motion between them.
- **Types of Robotic Joints**: Joints are crucial for a robot's movement and dexterity, categorized into linear and rotary types.
- **Linear Joints**: Allow movement along a straight line.
- **Prismatic Joint**: Enables linear sliding motion, where one part moves along an axis within another, similar to a key sliding in a slot.
- **Sliding Joint**: Allows linear movement of a component, such as a pin sliding within a block.
- **Rotary Joints**: Allow rotational movement around an axis.
- **Twisting Joint (T)**: The axis of rotation is aligned with (coincides with) the axis of the output link, causing a twisting motion along the link's length.
- **Revolute Joint (R)**: The axis of rotation is perpendicular to the axis of the output link, allowing for a hinge-like or sweeping motion.

### Key Takeaways
- [ ] Robots are automatically controlled, reprogrammable, and multifunctional machines, distinct from simpler automated systems like CNC machines due to their higher level of flexibility.
- [ ] Robotics is a multidisciplinary science encompassing physics, mathematics, and various engineering fields, aiming to replicate human capabilities like hand dexterity, intelligence, and emotion.
- [ ] The primary motivations for studying robotics include reducing production costs, increasing productivity, and improving product quality in competitive markets.
- [ ] Robotics is a key enabler of flexible automation, making it particularly valuable for batch production in manufacturing and a wide array of other applications.
- [ ] The history of robotics spans from early theoretical concepts and patents in the mid-20th century to the development of sophisticated intelligent and emotional humanoid robots today.
- [ ] A typical robotic system consists of a manipulator (the robot arm), a drive unit, and a controller, with the manipulator's movement facilitated by various types of joints.
- [ ] Robotic joints are categorized into linear (prismatic and sliding) and rotary (twisting and revolute) types, each enabling specific forms of motion critical for a robot's functionality.
- [ ] Understanding the distinction between revolute and twisting joints based on the orientation of the rotation axis relative to the output link is fundamental to robot kinematics.

### Conclusion

This introductory lecture has provided a foundational understanding of robots and robotics, tracing their origins from a concept of "forced labor" to their current status as sophisticated, intelligent, and increasingly emotional machines. We've explored the precise definitions offered by leading organizations, highlighting the core characteristics of automatic control, reprogrammability, and multifunctionality that set robots apart. The compelling motivations for robotics, driven by the need for cost-efficiency, high productivity, and superior quality in a dynamic market, underscore its critical role in modern industry. From the historical milestones that shaped its development to the intricate mechanics of robotic joints, it's clear that robotics is a rapidly evolving field. As we move forward, the integration of intelligence and emotion into robotic design promises to create machines that not only perform tasks but also interact with the world in increasingly human-like ways, pushing the boundaries of what is possible and addressing complex challenges across diverse sectors.