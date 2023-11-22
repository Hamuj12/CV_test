import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def visualize_box_and_keypoints(keypoints_3d, box_dimensions):
    """
    Visualize the 3D keypoints on a box.

    :param keypoints_3d: List of 3D keypoints as tuples (x, y, z).
    :param box_dimensions: Tuple of box dimensions (LxWxH).
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Drawing the box
    for x in [-box_dimensions[0]/2, box_dimensions[0]/2]:
        for y in [-box_dimensions[1]/2, box_dimensions[1]/2]:
            ax.plot([x, x], [y, y], [-box_dimensions[2]/2, box_dimensions[2]/2], color='b')

    for x in [-box_dimensions[0]/2, box_dimensions[0]/2]:
        for z in [-box_dimensions[2]/2, box_dimensions[2]/2]:
            ax.plot([x, x], [-box_dimensions[1]/2, box_dimensions[1]/2], [z, z], color='b')

    for y in [-box_dimensions[1]/2, box_dimensions[1]/2]:
        for z in [-box_dimensions[2]/2, box_dimensions[2]/2]:
            ax.plot([-box_dimensions[0]/2, box_dimensions[0]/2], [y, y], [z, z], color='b')

    # Define colors for each face
    face_colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown']

    # Assuming each face has 5 keypoints
    keypoints_per_face = 5

    # Adding keypoints with different colors for each face
    for i in range(0, len(keypoints_3d), keypoints_per_face):
        face_keypoints = keypoints_3d[i:i+keypoints_per_face]
        color = face_colors[(i // keypoints_per_face) % len(face_colors)]
        xs, ys, zs = zip(*face_keypoints)
        ax.scatter(xs, ys, zs, color=color)

    ax.set_xlim([-200, 200])
    ax.set_ylim([-200, 200])
    ax.set_zlim([-200, 200])

    # Setting labels and title
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title('3D Visualization of Keypoints on a Box')

    plt.show()

# Example usage
keypoints_3d_example = [(51, -10, -10),
                        (51, -146.65, -96.15),
                        (51, -146.65, 96.15),
                        (51, 146.65, -96.15),
                        (51, 146.65, 96.15),

                        (-51, 10, 10),
                        (-51, 146.65, 96.15),
                        (-51, 146.65, -96.15),
                        (-51, -146.65, 96.15),
                        (-51, -146.65, -96.15),

                        (-10, -30, 127),
                        (30.25, 156.67, 127),
                        (-30.25, 156.67, 127),
                        (30.25, -156.67, 127),
                        (-30.25, -156.67, 127),

                        (-10, -30, -127),
                        (30.25, -156.67, -127),
                        (-30.25, -156.67, -127),
                        (30.25, 156.67, -127),
                        (-30.25, 156.67, -127),

                        (0, 177.5, 0),
                        (25.25, 177.5, 101.23),
                        (-25.25, 177.5, 101.23),
                        (25.25, 177.5, -101.23),
                        (-25.25, 177.5, -101.23),

                        (0, -177.5, 0),
                        (25.25, -177.5, 101.23),
                        (-25.25, -177.5, 101.23),
                        (25.25, -177.5, -101.23),
                        (-25.25, -177.5, -101.23),]  

# save these keypoints as a numpy array
np.save('calib_box_large_kps.npy', keypoints_3d_example)

box_dimensions_example = (102, 355, 254)  # your box dimensions
visualize_box_and_keypoints(keypoints_3d_example, box_dimensions_example)


# https://www.festi.info/boxes.py/ClosedBox?FingerJoint_angle=90.0&FingerJoint_style=rectangular&FingerJoint_surroundingspaces=2.0&FingerJoint_bottom_lip=0.0&FingerJoint_edge_width=1.0&FingerJoint_extra_length=0.0&FingerJoint_finger=2.0&FingerJoint_play=0.0&FingerJoint_space=2.0&FingerJoint_width=1.0&x=355&y=254&h=102&outside=0&outside=1&thickness=3.0&format=svg&tabs=0.0&qr_code=0&debug=0&labels=0&labels=1&reference=0&inner_corners=loop&burn=0.1&language=en&render=0