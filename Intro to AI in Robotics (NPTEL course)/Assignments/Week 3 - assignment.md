# Swayam Assignment: Introduction to Application of Artificial Intelligence to Robotics (Week 3)

### **Question 1**
If $P_c = [x_c, y_c, z_c]^T$ locates the Center of mass of a rigid body relative to {A}. Then the Parallel-axis Theorem, relates the inertia tensor in a frame {C} with origin at the center of mass to the inertia tensor with respect to another arbitrarily translated reference frame {A} as,

**Solution:**
$$^{A}I_{zz} = ^{C}I_{zz} + m(x_c^2 + y_c^2)$$

**Explanation:** According to the parallel-axis theorem, the moment of inertia around any given axis (AIzz​) is equal to the moment of inertia around a parallel axis that passes through the center of mass (CIzz​), plus the mass of the body (m) multiplied by the square of the perpendicular distance between the two axes.  

In this case, the perpendicular distance squared between the two parallel z-axes is $$x_c^2​+y_c^2​$$.

### **Question 2**
For a Solid Cylinder with radius ($R$) and mass $m$, its moment of inertia about its geometrical axis as shown in Figure is________.

**Solution:**
$$I = (1/2)mR^2$$
**Explanation:**

The moment of inertia measures an object's resistance to changes in its rotation rate. For a uniform solid cylinder rotating about its central, longitudinal axis (its geometrical axis), the mass is distributed evenly outward from the center.
By integrating the mass elements across the volume of the cylinder from radius $0$ to $R$, the standard derived formula for this specific moment of inertia is mathematically proven to be $\frac{1}{2}mR^2$.

---


### **Question 3**
In Euler's equation $N = ^CI\dot{\omega} + \omega \times ^CI\omega$, what does the term $^CI\omega$ physically represent?

**Solution:**
**Angular momentum of the body**

**Explanation:** In rigid body dynamics, Euler's equation describes the rotation of a rigid body under the influence of torque. Let's break down the components of the term in question:

- CI represents the inertia tensor of the body with respect to a frame (C) located at its center of mass.
    
- ω represents the angular velocity vector of the body.
    

In physics, the product of a rigid body's moment of inertia and its angular velocity yields its **angular momentum** (often denoted by the letter L, so L=Iω).

Therefore, the term CIω represents the angular momentum of the body. Euler's full equation fundamentally states that the net applied torque (N) is equal to the rate of change of this angular momentum.

---

### **Question 4**
Using Newton's equation $F = m\dot{v}_c$, if a link has mass $m = 4$ kg and its center-of-mass linear acceleration is $\dot{v}_c = (3, 0, 4)$ m/s$^2$, what is the magnitude of the force $F$ acting at the center of mass?

**Solution:**
**20 N**

**Explanation:**

To find the magnitude of the force acting at the center of mass, you can first calculate the magnitude of the linear acceleration vector, and then multiply it by the mass.

1. **Find the magnitude of the acceleration vector $\dot{v}_c$:**
    
    The magnitude of a 3D vector $(x, y, z)$ is given by $\sqrt{x^2 + y^2 + z^2}$.
    
    $$\vert{}\dot{v}_c\vert{} = \sqrt{3^2 + 0^2 + 4^2}$$
    
    $$\vert{}\dot{v}_c\vert{} = \sqrt{9 + 0 + 16}$$
    
    $$\vert{}\dot{v}_c\vert{} = \sqrt{25}$$
    
    $$\vert{}\dot{v}_c\vert{} = 5 \text{ m/s}^2$$
    
2. **Calculate the magnitude of the force ($F$):**
    
    Using Newton's second law ($F = ma$ or $F = m\vert{}\dot{v}_c\vert{}$):
    
    $$\vert{}F\vert{} = 4 \text{ kg} \times 5 \text{ m/s}^2$$
    
    $$\vert{}F\vert{} = 20 \text{ N}$$
    

Alternatively, you could multiply the mass by the vector first to get the force vector $F = (12, 0, 16)$, and then find its magnitude: $\sqrt{12^2 + 0^2 + 16^2} = \sqrt{144 + 256} = \sqrt{400} = 20 \text{ N}$. Both methods yield the exact same result!

---

### **Question 5**
Which of the following boundary conditions is used in the 2 DOF planar manipulator example shown below to correctly incorporate the effect of gravity into the Newton-Euler recursion?

**Solution:**
**Setting $^0\dot{v}_0 = g\hat{Y}_0$**

**Explanation:** In the Newton-Euler iterative dynamics formulation, the effect of gravity is elegantly handled without needing to calculate separate gravitational forces for each link. Instead, it is incorporated by assigning an initial upward "fictitious" acceleration to the base of the robot.

By setting the linear acceleration of the base frame (0v˙0​) equal to the gravitational acceleration vector (in this planar case, gY^0​), the recursive algorithm automatically propagates the equivalent gravitational forces outward to all the subsequent links in the chain.

---

### **Question 6**
Why is $^3f_3 = 0$ and $^3n_3 = 0$ used as a boundary condition in the inward iteration of 2 DOF planar manipulator example shown below?

**Solution:**
**Because there is no external force or moment applied by the environment at the end-effector**

**Explanation:** In the Newton-Euler formulation, the dynamic equations are solved iteratively. The outward iterations compute velocities and accelerations from the base out to the end-effector. The inward iterations compute the forces ($f$) and torques/moments ($n$) starting from the end-effector back down to the base. The initial boundary condition for this inward pass represents the forces acting on the very tip of the robot. If the manipulator is moving freely in space and not pushing against an object or payload, the external force and torque exerted by the environment on the end-effector are zero.

---

### **Question 7**
In the final torque expression $\tau = M(\theta)\ddot{\theta} + V(\theta, \dot{\theta}) + G(\theta)$ derived for the RP manipulator, what distinguishes the vector $V(\theta, \dot{\theta})$ from $G(\theta)$?

**Solution:**
**$V(\theta, \dot{\theta})$ represents centrifugal and Coriolis terms depending on joint velocities, while $G(\theta)$ represents gravity terms depending only on joint position.**

**Explanation:**

This is the standard Euler-Lagrange equation of motion for a robotic manipulator.

- **$V(\theta, \dot{\theta})$** is the velocity-coupling vector. It captures the complex dynamic effects that occur when the joints are in motion, specifically the Coriolis forces (which arise from the interaction of two moving joints) and centrifugal forces (which arise from the rotation of a single joint). These forces scale with the square of the joint velocities.
    
- **$G(\theta)$** is the gravitational vector. It calculates the torques required simply to hold the manipulator up against gravity at any given static configuration, meaning it is strictly a function of the joint positions ($\theta$).

---

### **Question 8**
In the expression for the kinetic energy of the i-th link, $k_i = \frac{1}{2}m_i \cdot v_{Ci}^T \cdot v_{Ci} + \frac{1}{2} \cdot ^i\omega_i^T \cdot ^{Ci}I_i \cdot ^i\omega_i$, what do the two terms physically represent?

**Solution:**
**The first term is KE due to linear velocity of the link's center of mass; the second term is KE due to angular velocity of the link**

**Explanation:**

The total kinetic energy of a rigid body is the sum of its translational and rotational kinetic energy.

- The first term ($\frac{1}{2}m v^2$) calculates the translational kinetic energy of the link, treating all its mass ($m_i$) as if it were concentrated at its center of mass moving at linear velocity $v_{Ci}$.
    
- The second term ($\frac{1}{2}I \omega^2$) calculates the rotational kinetic energy of the link as it rotates with angular velocity $\omega_i$ around that center of mass, utilizing the inertia tensor ($I_i$).

---

### **Question 9**
For the manipulator shown below, the mass matrix, $M(\theta)$ is given by

**Solution:**
$$ \begin{bmatrix} m_2l_2^2 + 2m_2l_1l_2c_2 + (m_1+m_2)l_1^2 & m_2l_2^2 + m_2l_1l_2c_2 \\ m_2l_2^2 + m_2l_1l_2c_2 & m_2l_2^2 \end{bmatrix} $$
**Explanation:**

For a standard 2-DOF planar revolute-revolute (2R) manipulator where the mass of the links is concentrated at their distal ends (acting as point masses $m_1$ and $m_2$ at the ends of lengths $l_1$ and $l_2$), this is the standard derived inertia matrix.

- $M_{11}$ represents the total inertia felt by the first joint, which involves both masses and depends heavily on the elbow angle ($\theta_2$, represented by $c_2 = \cos(\theta_2)$) because extending the arm increases the rotational inertia.
    
- $M_{22}$ is simply $m_2l_2^2$, representing the inertia of the second link moving around its own joint.
    
- $M_{12}$ and $M_{21}$ are the off-diagonal terms representing the dynamic coupling between the two joints (note that mass matrices are always symmetric, so $M_{12} = M_{21}$).
---

### **Question 10**
In $\tau = M(\theta)\ddot{\theta} + B(\theta)[\dot{\theta}\dot{\theta}] + C(\theta)[\dot{\theta}^2] + G(\theta)$, the matrix $B(\theta)$ has dimension:

**Solution:**
**$n \times n(n-1)/2$**

**Explanation:**

In this expanded form of the dynamic equations, the velocity-dependent terms are split into Coriolis effects ($B$) and centrifugal effects ($C$).

- The system has $n$ joints, so the resulting torque vector $\tau$ must be $n \times 1$.
    
- The vector $[\dot{\theta}\dot{\theta}]$ represents all unique pairs of joint velocities multiplied together ($\dot{\theta}_i \dot{\theta}_j$ where $i \neq j$). Using combinations, the number of unique pairs in an $n$-joint robot is $\frac{n(n-1)}{2}$. So, this is a column vector of dimension $\frac{n(n-1)}{2} \times 1$.
    
- In order to multiply matrix $B(\theta)$ by a $\frac{n(n-1)}{2} \times 1$ vector and get an $n \times 1$ torque output, matrix $B(\theta)$ must have dimensions $n \times \frac{n(n-1)}{2}$.