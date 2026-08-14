import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

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

DH = [
    [0,      np.pi/2,  0.6718],
    [0.4318, 0,        0],
    [0.0203, -np.pi/2, 0.15],
    [0,      np.pi/2,  0.4318],
    [0,      -np.pi/2, 0],
    [0,      0,        0]
]

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


q = np.zeros(6)

frames = forward_kinematics(q)

for i, T in enumerate(frames):

    print(f"\nFrame {i}")
    print(T)



points = np.array([
    T[:3, 3]
    for T in frames
])

print(points)

fig = plt.figure()

ax = fig.add_subplot(111, projection="3d")

ax.plot(
    points[:, 0],
    points[:, 1],
    points[:, 2],
    marker="o"
)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()

plt.subplots_adjust(bottom=0.30)

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

    q = np.zeros(6)

def update(val):

    for i in range(6):

        q[i] = np.radians(sliders[i].val)

    frames = forward_kinematics(q)

    points = np.array([
        T[:3, 3]
        for T in frames
    ])

    line.set_data(
        points[:, 0],
        points[:, 1]
    )

    line.set_3d_properties(
        points[:, 2]
    )

    fig.canvas.draw_idle()

for slider in sliders:

    slider.on_changed(update)
    plt.show()