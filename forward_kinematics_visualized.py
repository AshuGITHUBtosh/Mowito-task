import math
import matplotlib.pyplot as plt


def forward_kinematics(j1, j2, j3, j4, L=1):
    """
    Compute positions of each joint and the end-effector
    """

    # cumulative angles
    a1 = j1
    a2 = j1 + j2
    a3 = j1 + j2 + j3
    a4 = j1 + j2 + j3 + j4

    # joint positions
    x0, y0 = 0, 0

    x1 = x0 + L * math.cos(a1)
    y1 = y0 + L * math.sin(a1)

    x2 = x1 + L * math.cos(a2)
    y2 = y1 + L * math.sin(a2)

    x3 = x2 + L * math.cos(a3)
    y3 = y2 + L * math.sin(a3)

    x4 = x3 + L * math.cos(a4)
    y4 = y3 + L * math.sin(a4)

    return [x0, x1, x2, x3, x4], [y0, y1, y2, y3, y4]


def plot_arm(xs, ys):
    """
    Plot the robot arm configuration
    """

    plt.figure()
    plt.plot(xs, ys, marker='o', linewidth=3)

    plt.title("4-Link Robot Arm Forward Kinematics")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")

    plt.grid(True)
    plt.axis('equal')

    plt.show()


def main():

    print("Forward Kinematics for 4-Link Robot Arm")

    j1 = float(input("Enter joint angle j1 (radians): "))
    j2 = float(input("Enter joint angle j2 (radians): "))
    j3 = float(input("Enter joint angle j3 (radians): "))
    j4 = float(input("Enter joint angle j4 (radians): "))

    xs, ys = forward_kinematics(j1, j2, j3, j4)

    end_x = xs[-1]
    end_y = ys[-1]

    print("\nEnd Effector Position:")
    print("x =", end_x)
    print("y =", end_y)
    print("z = 0")

    plot_arm(xs, ys)


if __name__ == "__main__":
    main()