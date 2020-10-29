from core.objects import ActiveObject, DebrisObject
import numpy as np

# constants unknown to the active object
# TODO: maybe generalize these later
initial_debris_positions = [
    (0.5,0,0),
    (1.5,0,0)
]

# endpoints of active object journey
A_xyz = np.array([0,0,0])
B_xyz = np.array([1,0,0])

# active object parameters
scan_radius = 1
fuel = 1

# initialize active object
active_object = ActiveObject(A_xyz, B_xyz, radius=scan_radius, fuel=fuel)

# initialize debris
debris_objects = [
    DebrisObject(xyztuple) for xyztuple in initial_debris_positions
]

arrival_tolerance = 1e-2
while np.linalg.norm(active_object.position_xyz-B_xyz) > arrival_tolerance:
    # get visible debris
    active_object.scan(debris_objects)
    print('visible debris positions:', active_object.visible_debris_positions)

    # make a plot of debris objects
    active_object.view(debris_objects)

    # adjust position based on available info

    # move
    
