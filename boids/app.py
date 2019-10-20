from vispy import (
    app as vapp,
    gloo
)

class BoidsCanvas(vapp.Canvas):
    def __init__(self):
        super().__init__(size=(600, 600), title='2-D Boids')
