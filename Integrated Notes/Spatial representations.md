---
tags:
  - notes
---
> Integrated notes from NPTEL lectures and John J. Craig textbook.

## CH: 2 -- Spatial descriptions and transformations

### Coordinate frame: 
A **coordinate frame** is simply a reference used to measure **position** and **orientation**.

A frame consists of:

- An origin
- An x-axis
- A y-axis
- A z-axis

coordinate frame is **not the object**.

It is a mathematical reference attached to the object so that we can describe its position and orientation relative to other frames.

### Coordinate frame and position vector & rotation matrix 

The **coordinate frame itself** consists only of:

- An **origin**
- Three mutually perpendicular axes (**x, y, z**)

Everything else is **used to describe that frame relative to another frame**.

So if you have two frames:

- {A} (reference frame)
- {B} (frame attached to an object)

then:

- **Position vector** tells you **where the origin of {B} is with respect to {A}.**
- **Orientation matrix (rotation matrix)** tells you **how the axes of {B} are oriented with respect to the axes of {A}.**

Coordinate Frame {B}
│
├── Origin
├── x-axis
├── y-axis
└── z-axis

Description of {B} relative to {A}
│
├── Position vector
└── Rotation matrix
### A useful sentence to remember

> A **coordinate frame** is a physical/mathematical reference attached to an object.

> A **position vector** and a **rotation matrix** are the quantities that **describe that frame relative to another frame**.

![image](Pasted%20image%2020260729115101.png)

---
### Position Vectors

- Once a coordinate system is established, we can locate any point in the universe
with a 3 x 1 position vector.
- Each of these distances along an axis can be thought of as the result of projecting
the vector onto the corresponding axis.
- We will describe the position of a point in space with a position vector.
- The position of a point P relative to a coordinate frame {A} is represented by a
vector:

![image](Pasted%20image%2020260729131710.png)

![image|697](Pasted%20image%2020260728142832.png)

### Orientation Representation

- To describe an object in space, we need to specify its
position as well as its orientation.
- While position describes where an object or manipulation
is located, orientation describes how it is rotated relative to
another coordinate frame.
- Assuming that the manipulator has sufficient number of
joints to orient the object in desired orientation while
keeping the fingertip at same position in space.
- To describe the orientation of a body, we attach a
coordinate system to the body and then give a description
of this coordinate system relative to the reference system.
- One way to describe the body attached coordinate system
{B} is to write the unit vectors of its three principal axes in
terms of the coordinate system {A}.

![[Pasted image 20260729132254 1.png]]
![image](Pasted%20image%2020260728142915.png)
![image|697](Pasted%20image%2020260729132254%201.png)

