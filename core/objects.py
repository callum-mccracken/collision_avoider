import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

"""
Module for definitions of objects like DebrisObject, ActiveObject
and superclass PhysicalObject (not just definitions, functions too)
"""

def distance(xyz1, xyz2):
    return np.linalg.norm(xyz1-xyz2)

class PhysicalObject():
    """
    General class for objects with physical properties,
    e.g. debris and active object
    """
    def __init__(self, position_xyz):
        # save initial position if needed later
        self._init_x, self._init_y, self._init_z = position_xyz
        # set current coordinates
        self._x, self._y, self._z = position_xyz
        # store position as np array for quicker operations later
        self.position_xyz = np.array(position_xyz)

    def print_position(self):
        print(self.position_xyz)

class DebrisObject(PhysicalObject):
    """
    Class for describing debris objects

    On initialization, gets a well-defined path,
    which will not be visible to active object
    """
    def __init__(self, position_xyz):
        super(DebrisObject, self).__init__(position_xyz)
        # calculate path somehow? We'll probably need more info than position
        # TODO: Mujtaba calculate this

class ActiveObject(PhysicalObject):
    """
    Has distances to nearby objects from a few frames in the past

    Has endpoints of trip

    Has fuel which gets depleted based on motion

    Tries to minimize/maximize hitting stuff
    while also minimizing fuel
    """

    def __init__(self, A_xyz, B_xyz, radius=1, fuel=1):
        # radius that we can scan for debris
        self.scan_radius = radius

        # set initial position
        super(ActiveObject, self).__init__(A_xyz)

        # set destination
        self.destination_xyz = B_xyz

        # fuel amount
        self.initial_fuel = fuel
        self.current_fual = fuel

        # nothing is visible yet
        self.visible_debris_positions = None

    def scan(self, debris_list):
        """
            parameters:
                debris_list is a list of DebrisObjects
            returns:
                positions of visible (distance <= radius) debris,
                list of (x,y,z) tuples.
        """
        # look around to see if there is debris nearby
        visible_debris_positions = np.array([
            d.position_xyz for d in debris_list
            if distance(self.position_xyz, d.position_xyz) <= self.scan_radius
        ])
        # set visible_debris_positions
        self.visible_debris_positions = visible_debris_positions

    def view(self, debris_list):
        """make 3d view of active object and debris"""
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # plot active object at origin
        ax.scatter(self.position_xyz[0],
                   self.position_xyz[1],
                   self.position_xyz[2],
                   c='g', s=5)

        # plot all debris objects, visible in one color, invisible in another
        for d in debris_list:
            ax.scatter(d.position_xyz[0],
                       d.position_xyz[1],
                       d.position_xyz[2],
                       c='k', s=5)
        # cover invisible with visible in a different color
        for vdp in self.visible_debris_positions:
            ax.scatter(vdp[0],
                       vdp[1],
                       vdp[2],
                       c='r', s=5)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()