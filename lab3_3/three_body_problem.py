import graphics as gr
window = gr.GraphWin("three body problem", 600, 600)

a = 0
global d12
"""importing characteristics of bodies"""
dt = 0.0001
G = 2000

m1 = 10000
m2 = 10000
m3 = 10000

x1 = 200
y1 = 200

x2 = 400
y2 = 400

x3 = 300
y3 = 300

v1x = 300
v1y = -300

v2x = -300
v2y = 300

v3x = 0
v3y = 0


def drawing_planets():
    global pl1, pl2, pl3 
    """drawing planets"""
    pl1 = gr.Circle(gr.Point(x1, y1), 5)
    pl1.draw(window)
    pl1.setFill('red')

    pl2 = gr.Circle(gr.Point(x2, y2), 5)
    pl2.draw(window)
    pl2.setFill('blue')
     
    pl3 = gr.Circle(gr.Point(x3, y3), 5)
    pl3.draw(window)
    pl3.setFill('green')


def distance():
    global d12, d13, d23
    d12 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    d13 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
    d23 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5


def force_laws():
    global force12x, force12y, force13x, force13y, force23x, force23y
    """force_laws"""
    force12x = G * m1 * m2 / d12 ** 2 * (x2 - x1) / d12
    force12y = G * m1 * m2 / d12 ** 2 * (y2 - y1) / d12

    force13x = G * m1 * m3 / d13 ** 2 * (x3 - x1) / d13
    force13y = G * m1 * m3 / d13 ** 2 * (y3 - y1) / d13

    force23x = G * m2 * m3 / d23 ** 2 * (x3 - x2) / d23
    force23y = G * m2 * m3 / d23 ** 2 * (y3 - y2) / d23


def acceleration():
    global a1x, a2x, a3x, a1y, a2y, a3y 
    """acceleration changing law"""	
    a1x = (force12x + force13x) / m1
    a1y = (force12y + force13y) / m1

    a2x = (-force12x + force23x) / m2
    a2y = (-force12y + force23y) / m2
    
    a3x = (-force13x - force23x) / m3
    a3y = (-force13y - force23y) / m3


def change_of_coordinates(): 
    global x1, y1, x2, y2, x3, y3, dx1, dx2, dx3, dy1, dy2, dy3
    """coordinate changing laws"""
    x1 = x1 + (v1x * dt)
    y1 = y1 + (v1y * dt)

    x2 = x2 + (v2x * dt)
    y2 = y2 + (v2y * dt)

    x3 = x3 + (v3x * dt)
    y3 = y3 + (v3y * dt)

    dx1 = v1x * dt
    dy1 = v1y * dt

    dx2 = v2x * dt
    dy2 = v2y * dt

    dx3 = v3x * dt
    dy3 = v3y * dt


def motion_of_planets():
    global pl1, pl2, pl3

    pl1.move(dx1, dy1)

    pl2.move(dx2, dy2)

    pl3.move(dx3, dy3)


def change_of_velocities():
    global v1x, v1y, v2x, v2y, v3x, v3y 
    """velocity_changing_laws"""
    v1x = v1x + (a1x * dt)
    v1y = v1y + (a1y * dt)

    v2x = v2x + (a2x * dt)
    v2y = v2y + (a2y * dt)

    v3x = v3x + (a3x * dt)
    v3y = v3y + (a3y * dt)


def drawing_trajectories():
    global a
    """trajectoies of planets"""
    if a % 500 == 0:
        trajectory1 = gr.Point(x1, y1)
        trajectory2 = gr.Point(x2, y2)
        trajectory3 = gr.Point(x3, y3)

        trajectory1.draw(window)
        trajectory2.draw(window)
        trajectory3.draw(window)

        trajectory1.setFill('red')
        trajectory2.setFill('blue')
        trajectory3.setFill('green')
        a += 1
    else:
        a += 1

drawing_planets()


def motion():
    distance()
    force_laws()
    acceleration()
    change_of_coordinates()
    motion_of_planets()
    change_of_velocities()
    drawing_trajectories()


for i in range(1000000):
    motion()


window.getMouse()
window.close()


