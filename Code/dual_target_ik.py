import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML, display

plt.ioff()

# 2-Link Planar Arm Inverse Kinematics with Animation - TWO TARGETS VERSION

def simulate_2link_planar_arm_ik_dual_targets(L1, L2, target_x1, target_y1, target_x2, target_y2, fps=30, duration=4):
    """Animate a 2-link planar arm solving inverse kinematics for two sequential targets."""
    
    # Initialize joint angles
    q = np.array([np.deg2rad(30), np.deg2rad(30)])
    target1 = np.array([target_x1, target_y1])
    target2 = np.array([target_x2, target_y2])
    
    # IK parameters
    alpha = 0.01  # Step size
    tolerance = 1e-3
    max_iterations = 1000
    
    # Store history for animation
    q_history = [q.copy()]
    error_history_1 = []
    error_history_2 = []
    
    # ===== SOLVE IK FOR TARGET 1 =====
    print(f"\n🎯 Solving IK for Target 1: ({target1[0]:.2f}, {target1[1]:.2f})")
    for i in range(max_iterations):
        # Forward kinematics
        theta1, theta2 = q
        x1 = L1 * np.cos(theta1)
        y1 = L1 * np.sin(theta1)
        x2 = x1 + L2 * np.cos(theta1 + theta2)
        y2 = y1 + L2 * np.sin(theta1 + theta2)
        
        current_position = np.array([x2, y2])
        error = target1 - current_position
        error_norm = np.linalg.norm(error)
        error_history_1.append(error_norm)
        
        if error_norm < tolerance:
            print(f"   ✓ Target 1 reached in {len(error_history_1)} iterations")
            break
        
        # Jacobian
        J = np.array([
            [-L1 * np.sin(theta1) - L2 * np.sin(theta1 + theta2),
             -L2 * np.sin(theta1 + theta2)],
            [L1 * np.cos(theta1) + L2 * np.cos(theta1 + theta2),
             L2 * np.cos(theta1 + theta2)]
        ])
        
        # Pseudoinverse and update
        J_pinv = np.linalg.pinv(J)
        delta_q = J_pinv @ error
        q = q + alpha * delta_q
        q_history.append(q.copy())

    # ===== SOLVE IK FOR TARGET 2 =====
    print(f"\n🎯 Solving IK for Target 2: ({target2[0]:.2f}, {target2[1]:.2f})")
    for i in range(max_iterations):
        # Forward kinematics
        theta1, theta2 = q
        x1 = L1 * np.cos(theta1)
        y1 = L1 * np.sin(theta1)
        x2 = x1 + L2 * np.cos(theta1 + theta2)
        y2 = y1 + L2 * np.sin(theta1 + theta2)
        
        current_position = np.array([x2, y2])
        error = target2 - current_position
        error_norm = np.linalg.norm(error)
        error_history_2.append(error_norm)
        
        if error_norm < tolerance:
            print(f"   ✓ Target 2 reached in {len(error_history_2)} iterations")
            break
        
        # Jacobian
        J = np.array([
            [-L1 * np.sin(theta1) - L2 * np.sin(theta1 + theta2),
             -L2 * np.sin(theta1 + theta2)],
            [L1 * np.cos(theta1) + L2 * np.cos(theta1 + theta2),
             L2 * np.cos(theta1 + theta2)]
        ])
        
        # Pseudoinverse and update
        J_pinv = np.linalg.pinv(J)
        delta_q = J_pinv @ error
        q = q + alpha * delta_q
        q_history.append(q.copy())

    # Final configuration
    theta1_final, theta2_final = q
    x1_final = L1 * np.cos(theta1_final)
    y1_final = L1 * np.sin(theta1_final)
    x2_final = x1_final + L2 * np.cos(theta1_final + theta2_final)
    y2_final = y1_final + L2 * np.sin(theta1_final + theta2_final)

    # Static notebook-friendly plot
    static_fig, ax_axes = plt.subplots(1, 3, figsize=(16, 5))
    
    reach = L1 + L2
    
    # Plot 1: Arm final configuration
    ax_static_arm = ax_axes[0]
    ax_static_arm.plot([0, x1_final, x2_final], [0, y1_final, y2_final], '-o', linewidth=3, markersize=8, color='tab:blue', label='Robot Arm')
    ax_static_arm.plot([0], [0], 'ks', markersize=10, label='Base')
    ax_static_arm.plot([target1[0]], [target1[1]], 'b*', markersize=18, label='Target 1')
    ax_static_arm.plot([target2[0]], [target2[1]], 'g*', markersize=18, label='Target 2')
    ax_static_arm.plot([x2_final], [y2_final], 'ro', markersize=8, label='Final End-Effector')
    
    ax_static_arm.set_xlim(-reach - 0.5, reach + 0.5)
    ax_static_arm.set_ylim(-reach - 0.5, reach + 0.5)
    ax_static_arm.set_aspect('equal', adjustable='box')
    ax_static_arm.grid(True, alpha=0.3)
    ax_static_arm.set_xlabel('X Position')
    ax_static_arm.set_ylabel('Y Position')
    ax_static_arm.set_title('Final Configuration (Target 2)')
    ax_static_arm.legend(loc='upper left', fontsize=9)

    # Plot 2: Target 1 convergence
    ax_err1 = ax_axes[1]
    if error_history_1:
        ax_err1.plot(range(len(error_history_1)), error_history_1, 'b-', linewidth=2)
        ax_err1.set_title('IK Convergence - Target 1')
        ax_err1.set_xlabel('Iteration')
        ax_err1.set_ylabel('Euclidean error')
        ax_err1.grid(True, alpha=0.3)

    # Plot 3: Target 2 convergence
    ax_err2 = ax_axes[2]
    if error_history_2:
        ax_err2.plot(range(len(error_history_2)), error_history_2, 'g-', linewidth=2)
        ax_err2.set_title('IK Convergence - Target 2')
        ax_err2.set_xlabel('Iteration')
        ax_err2.set_ylabel('Euclidean error')
        ax_err2.grid(True, alpha=0.3)
    
    static_fig.tight_layout()
    display(static_fig)
    
    # Prepare animation
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Left plot: arm configuration
    line, = ax1.plot([], [], '-o', linewidth=3, markersize=8, color='tab:blue', label='Robot Arm')
    base_point, = ax1.plot([], [], 'ks', markersize=10, label='Base (Joint 1)')
    end_point, = ax1.plot([], [], 'ro', markersize=8, label='End-Effector')
    target1_point, = ax1.plot([], [], 'b*', markersize=20, label='Target 1')
    target2_point, = ax1.plot([], [], 'g*', markersize=20, label='Target 2')
    
    # Right plot: error convergence (dual)
    error_line1, = ax2.plot([], [], 'b-', linewidth=2, label='Target 1 Error')
    error_line2, = ax2.plot([], [], 'g-', linewidth=2, label='Target 2 Error')
    
    def update(frame):
        # Interpolate between iterations for smooth animation
        total_frames = int(duration * fps)
        iteration_idx = min(int(frame * len(q_history) / total_frames), len(q_history) - 1)
        q_current = q_history[iteration_idx]
        
        # Forward kinematics
        theta1, theta2 = q_current
        x0, y0 = 0, 0
        x1 = L1 * np.cos(theta1)
        y1 = L1 * np.sin(theta1)
        x2 = x1 + L2 * np.cos(theta1 + theta2)
        y2 = y1 + L2 * np.sin(theta1 + theta2)
        
        # Update left plot
        x_coords = [x0, x1, x2]
        y_coords = [y0, y1, y2]
        
        line.set_data(x_coords, y_coords)
        base_point.set_data([x0], [y0])
        end_point.set_data([x2], [y2])
        target1_point.set_data([target1[0]], [target1[1]])
        target2_point.set_data([target2[0]], [target2[1]])
        
        ax1.set_title(
            f'2-Link Planar Arm - Dual Target IK\n'
            f'$\\theta_1$={np.rad2deg(theta1):.1f}°, '
            f'$\\theta_2$={np.rad2deg(theta2):.1f}°',
            fontsize=11
        )
        
        # Update right plot (error convergence)
        total_iterations = len(error_history_1) + len(error_history_2)
        
        # Shift target 2 errors to align with x-axis
        current_iterations_1 = min(iteration_idx + 1, len(error_history_1))
        if iteration_idx >= len(error_history_1):
            current_iterations_2 = min(iteration_idx - len(error_history_1) + 1, len(error_history_2))
            error_line1.set_data(range(len(error_history_1)), error_history_1)
            error_line2.set_data(range(len(error_history_1), len(error_history_1) + current_iterations_2), error_history_2[:current_iterations_2])
        else:
            error_line1.set_data(range(current_iterations_1), error_history_1[:current_iterations_1])
            error_line2.set_data([], [])
        
        ax2.set_title('IK Error Convergence', fontsize=11)
        ax2.set_xlabel('Total Iteration')
        ax2.set_ylabel('Error (Euclidean distance)')
        
        return line, base_point, end_point, target1_point, target2_point, error_line1, error_line2
    
    # Configure left plot (arm visualization)
    reach = L1 + L2
    ax1.set_xlim(-reach - 0.5, reach + 0.5)
    ax1.set_ylim(-reach - 0.5, reach + 0.5)
    ax1.set_aspect('equal', adjustable='box')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlabel('X Position')
    ax1.set_ylabel('Y Position')
    ax1.legend(loc='upper left', fontsize=9)
    
    # Configure right plot (error plot)
    total_iterations = len(error_history_1) + len(error_history_2)
    if total_iterations > 0:
        all_errors = error_history_1 + error_history_2
        ax2.set_xlim(0, total_iterations)
        ax2.set_ylim(0, max(all_errors) * 1.1)
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='upper right', fontsize=9)
    
    frames = int(duration * fps)
    animation = FuncAnimation(fig, update, frames=frames, interval=1000 / fps, blit=False, repeat=True)
    
    plt.tight_layout()
    display(HTML(animation.to_jshtml()))
    plt.close()
    
    print(f"\n✓ Dual-Target IK Solution Complete")
    print(f"  - Final angles: θ₁={np.rad2deg(q[0]):.2f}°, θ₂={np.rad2deg(q[1]):.2f}°")
    print(f"  - Target 1: ({target1[0]:.2f}, {target1[1]:.2f})")
    print(f"  - Target 2: ({target2[0]:.2f}, {target2[1]:.2f})")
    print(f"  - Final position: ({x2_final:.4f}, {y2_final:.4f})")
    print(f"  - Final error: {error_history_2[-1]:.6f}")
    print(f"  - Total iterations: {len(q_history) - 1}")


# ========================================
# Example: Solve 2-Link Planar Arm IK for TWO TARGETS
# ========================================

if __name__ == "__main__":
    LINK_1_LENGTH = 2.0
    LINK_2_LENGTH = 1.5

    TARGET_1_X = 1.0
    TARGET_1_Y = 1.0

    TARGET_2_X = 2.0
    TARGET_2_Y = 0.5

    simulate_2link_planar_arm_ik_dual_targets(
        LINK_1_LENGTH, 
        LINK_2_LENGTH, 
        TARGET_1_X, 
        TARGET_1_Y,
        TARGET_2_X,
        TARGET_2_Y,
        fps=30,
        duration=4
    )
