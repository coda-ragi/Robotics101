## 1. Which of the following is not a property of a rotation matrix R

Based on the properties of a rotation matrix in robotics and linear algebra:

- **$R^T R = R R^T = I$**: True. A rotation matrix is an orthogonal matrix.
    
- **$\det(R) = 1$**: True. The determinant of a valid rotation matrix is always $+1$ (it preserves orientation and does not reflect).
    
- **$R^{-1} = R^T$**: True. Since it is an orthogonal matrix, its inverse is equal to its transpose.
    
- **$\det(R) = 0$**: **NOT a property.** A rotation matrix is always full rank and invertible, so its determinant can never be zero.
    

Therefore, the correct answer is **$\det(R) = 0$**.

## 2. What does the bottom row contain in the transformation matrix..

In a standard $4 \times 4$ homogeneous transformation matrix, the bottom row contains:

- **`[0 0 0 1]`**
    

This perspective/scaling row ensures that matrix multiplication preserves affine transformations and allows combined rotation and translation operations to be represented in a single matrix.

## 3. A serial manipulator has 4 revolute joints and 2 prismatic joints in its kinematic chain. what is its total degree of freedom?

For a serial manipulator, the total Degrees of Freedom (DOF) is equal to the sum of the degrees of freedom provided by all individual joints in its kinematic chain.

Since revolute joints and prismatic joints each contribute **1 DOF** to the mechanism:

$$\text{Total DOF} = (\text{Number of Revolute Joints}) + (\text{Number of Prismatic Joints})$$

For a chain with 4 revolute joints and 2 prismatic joints:

$$\text{Total DOF} = 4 + 2 = 6$$

Therefore, the total DOF is **6**.

## 4. For a 2-link planar arm robot with link length $L_1 = L_2 = 2\text{ m}$ and joint angle $\theta_1 = 0^\circ, \theta_2 = 90^\circ$ degree. The end-effector position $(x,y)$ is ________m, ________m

To find the end-effector position $(x, y)$ for a 2-link planar arm, we use the forward kinematics equations:

$$x = L_1 \cos(\theta_1) + L_2 \cos(\theta_1 + \theta_2)$$

$$y = L_1 \sin(\theta_1) + L_2 \sin(\theta_1 + \theta_2)$$

Substituting the given values ($L_1 = 2\text{ m}$, $L_2 = 2\text{ m}$, $\theta_1 = 0^\circ$, and $\theta_2 = 90^\circ$):

- **$x$-coordinate:**
    
    $$x = 2 \cos(0^\circ) + 2 \cos(0^\circ + 90^\circ)$$
    
    $$x = 2(1) + 2(0) = 2\text{ m}$$
    
- **$y$-coordinate:**
    
    $$y = 2 \sin(0^\circ) + 2 \sin(0^\circ + 90^\circ)$$
    
    $$y = 2(0) + 2(1) = 2\text{ m}$$
    

Therefore, the end-effector position is **(2, 2)**.

## 5. For a 6-DOF manipulator with link parameters $a_3 = a_5 = 0$ (other $a_i \neq 0$), what is the maximum number of inverse kinematics solutions?

For a general 6-DOF manipulator with spherical wrist, there can be up to 16 inverse kinematics solutions, but under specific kinematic configurations—such as when certain link parameters (like $a_3$ and $a_5$) are zero, which often introduces structural simplifications (such as intersecting joint axes)—the maximum number of inverse kinematics solutions reduces to **$\le 8$**.

Therefore, the correct option is **$\le 8$**.

## 6. Using Algebraic solution, For a 2-link planar arm with $l_1 = 3\text{ m}$, $l_2 = 2\text{ m}$, and goal point $(x,y) = (4, 0)$, compute $\cos \theta_2$.

To find $\cos \theta_2$ for a 2-link planar arm using the algebraic method, we use the law of cosines relating the end-effector position $(x, y)$ to the link lengths $l_1$ and $l_2$:

$$x^2 + y^2 = l_1^2 + l_2^2 + 2 l_1 l_2 \cos(\theta_2)$$

Substitute the given values into the equation:

- $l_1 = 3$
    
- $l_2 = 2$
    
- $x = 4$
    
- $y = 0$
    

$$4^2 + 0^2 = 3^2 + 2^2 + 2(3)(2) \cos(\theta_2)$$

$$16 = 9 + 4 + 12 \cos(\theta_2)$$

$$16 = 13 + 12 \cos(\theta_2)$$

$$3 = 12 \cos(\theta_2)$$

$$\cos(\theta_2) = \frac{3}{12} = 0.25$$

Therefore, the correct option is **0.25**.

## 7. A manipulator's Jacobian at a given instant is the $2\times 2$ matrix $[1, 2; 2, 4]$. Determine its rank.

To determine the rank of the matrix:

$$J = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$$

We can check its determinant:

$$\det(J) = (1)(4) - (2)(2) = 4 - 4 = 0$$

Since the determinant is zero, the two rows (and columns) are linearly dependent (the second row is twice the first row). Therefore, the matrix is singular and does not have full rank.

- The rank is **1** because there is only one linearly independent row/column.
    

Therefore, the correct option is **1**.

## 8. What are the two common types of singularities that occur in manipulator?

In robotic manipulators, singularities are generally categorized based on where they occur within the robot's configuration space:

- **Workspace interior singularities (two joints lining up):** These occur inside the workspace when two or more joint axes align, causing the loss of one or more degrees of freedom (e.g., when a shoulder and wrist align).
    
- **Singularities at the edge of the workspace:** These occur at the boundary of the manipulator's workspace when the arm is fully stretched or folded back onto itself, rendering it unable to move further in a specific direction.
    

Therefore, the correct option is **Workspace interior singularities (two joints lining up) and singularities at the edge of the workspace**.

## 9. For a 2-link manipulator with $l_1 = 0.4\text{ m}$, $l_2 = 0.3\text{ m}$, $\theta_2 = 45^\circ$, and applied end-effector force $(f_x, f_y) = (10\text{ N}, 5\text{ N})$. The value of second joint torque $\tau_2$ is __________Nm.

The relationship between the joint torques ($\tau$) and the end-effector force vector ($F = [f_x, f_y]^T$) for a planar manipulator is given by the transpose of the Jacobian matrix:

$$\tau = J^T F$$

For a 2-link planar arm, the Jacobian transpose mapping the end-effector force to joint torques is expressed as:

$$\begin{bmatrix} \tau_1 \\ \tau_2 \end{bmatrix} = \begin{bmatrix} -l_1 \sin(\theta_1) - l_2 \sin(\theta_1 + \theta_2) & l_1 \cos(\theta_1) + l_2 \cos(\theta_1 + \theta_2) \\ -l_2 \sin(\theta_1 + \theta_2) & l_2 \cos(\theta_1 + \theta_2) \end{bmatrix} \begin{bmatrix} f_x \\ f_y \end{bmatrix}$$

The second joint torque ($\tau_2$) depends only on $l_2$, $\theta_1 + \theta_2$, and the forces:

$$\tau_2 = -l_2 \sin(\theta_1 + \theta_2) f_x + l_2 \cos(\theta_1 + \theta_2) f_y$$

Alternatively, using the principle of virtual work or standard static force analysis where $\theta_1$ can be set to $0^\circ$ as a reference baseline unless specified otherwise:

- Let $\theta_1 = 0^\circ$
    
- $\theta_2 = 45^\circ \implies \theta_1 + \theta_2 = 45^\circ$
    
- $l_2 = 0.3\text{ m}$
    
- $f_x = 10\text{ N}$, $f_y = 5\text{ N}$
    

$$\sin(45^\circ) = \frac{\sqrt{2}}{2} \approx 0.7071$$

$$\cos(45^\circ) = \frac{\sqrt{2}}{2} \approx 0.7071$$

$$\tau_2 = -0.3 \left(\frac{\sqrt{2}}{2}\right)(10) + 0.3 \left(\frac{\sqrt{2}}{2}\right)(5)$$

$$\tau_2 = 0.3 \left(\frac{\sqrt{2}}{2}\right) (-10 + 5) = 0.3 \left(\frac{\sqrt{2}}{2}\right) (-5)$$

$$\tau_2 = -1.5 \left(\frac{\sqrt{2}}{2}\right) = -0.75 \sqrt{2} \approx -1.06\text{ Nm}$$

Therefore, the value of the second joint torque $\tau_2$ is approximately **-1.06**.

## 10. In the force balance equation $^{i}f_i - ^{i}f_{i+1} = 0$ used for static analysis, what assumptions are made regarding the links themselves?

In robotic manipulator static force propagation and balance equations (such as those derived via the Newton-Euler recursive formulation), internal link statics assume that the link is in a quasi-static equilibrium where accelerations and gravitational effects on the link segments themselves are typically isolated or neglected for that specific internal force transmission step.

Therefore, the correct option is **Gravity and inertial forces on the links are neglected**.