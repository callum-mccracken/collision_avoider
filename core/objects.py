"""For things related to debris simulation"""

class PhysicalObject():
    """fill me in"""
    # shape and whatnot


class DebrisObject(PhysicalObject):
    """fill me in"""
    # has a path determined, which will be hidden from rocket


class ActiveObject(PhysicalObject):
    """
    Has distances to nearby objects from a few frames in the past

    Has endpoints of trip

    Has fuel which gets depleted based on motion

    Tries to minimize/maximize hitting stuff
    while also minimizing fuel
    """

