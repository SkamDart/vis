"""
Python implementation of 2-D Boids using a KD-Tree for optimal nearest-neighbor
lookups.

Using scipy.spatial.KDTree for our the KDTree implementation.
"""

import numpy as np
import scipy as sp

class Boid:
    """Single n-dimensional space and velocity vectored Bird-oid (Boid).
    However, since our simulation is in 2-D space. We will default to n = 2.
    """

    def __init__(self, n=2):
        self.x = np.zeros((n, 1))
        self.dx = np.zeros((n, 1))

    def __repr__(self):
        return '<Boid id={} x={} dx={}>'.format(id(self), self.x, self.dx)

    @classmethod
    def create_random(cls, max_width, max_height, dims):
        pass


class Boids:
    """Pythonic encoding of Boids algorithm."""

    def __init__(self, max_height, max_width, dims=2, flock_size=10):
        self.flock = np.array([Boid.create_random(max_height, max_width, dims)
                               for _ in range(flock_size)])

    def cohesion(self):
        """Steers to move towards the average position of local boids."""
        pass

    def separation(self):
        """Steers to avoid colliding with local boids."""
        pass

    def alignment(self):
        """Steers to average heading of local boids."""
        pass

