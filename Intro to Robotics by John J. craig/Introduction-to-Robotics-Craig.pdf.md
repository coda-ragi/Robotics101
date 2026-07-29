
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

![image](PNGs\Pasted image 20260729115101.png)










![image](PNGs\Pasted image 20260728142832.png)
![image](PNGs\Pasted image 20260728142915.png)