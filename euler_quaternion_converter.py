import math


def euler_to_quaternion(roll, pitch, yaw):
    """
    Convert Euler angles (roll, pitch, yaw) to quaternion (x, y, z, w)
    Angles must be in radians
    """

    cy = math.cos(yaw * 0.5)
    sy = math.sin(yaw * 0.5)
    cp = math.cos(pitch * 0.5)
    sp = math.sin(pitch * 0.5)
    cr = math.cos(roll * 0.5)
    sr = math.sin(roll * 0.5)

    w = cr * cp * cy + sr * sp * sy
    x = sr * cp * cy - cr * sp * sy
    y = cr * sp * cy + sr * cp * sy
    z = cr * cp * sy - sr * sp * cy

    return x, y, z, w


def quaternion_to_euler(x, y, z, w):
    """
    Convert quaternion (x, y, z, w) to Euler angles (roll, pitch, yaw)
    Returns radians
    """

    # Roll
    sinr_cosp = 2 * (w * x + y * z)
    cosr_cosp = 1 - 2 * (x * x + y * y)
    roll = math.atan2(sinr_cosp, cosr_cosp)

    # Pitch
    sinp = 2 * (w * y - z * x)

    if abs(sinp) >= 1:
        pitch = math.copysign(math.pi / 2, sinp)  # gimbal lock
    else:
        pitch = math.asin(sinp)

    # Yaw
    siny_cosp = 2 * (w * z + x * y)
    cosy_cosp = 1 - 2 * (y * y + z * z)
    yaw = math.atan2(siny_cosp, cosy_cosp)

    return roll, pitch, yaw


def main():

    print("\nChoose input format:")
    print("1 → Euler angles (roll, pitch, yaw)")
    print("2 → Quaternion (x, y, z, w)")

    choice = input("Enter choice (1 or 2): ")

    if choice == "1":

        print("\nEnter Euler angles in radians")

        roll = float(input("Roll: "))
        pitch = float(input("Pitch: "))
        yaw = float(input("Yaw: "))

        x, y, z, w = euler_to_quaternion(roll, pitch, yaw)

        print("\nQuaternion result:")
        print("x =", x)
        print("y =", y)
        print("z =", z)
        print("w =", w)

    elif choice == "2":

        print("\nEnter quaternion values")

        x = float(input("x: "))
        y = float(input("y: "))
        z = float(input("z: "))
        w = float(input("w: "))

        roll, pitch, yaw = quaternion_to_euler(x, y, z, w)

        print("\nEuler angles result (radians):")
        print("roll =", roll)
        print("pitch =", pitch)
        print("yaw =", yaw)

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()