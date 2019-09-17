import graphics as gr

window = gr.GraphWin("Jenkslex and Ganzz project", 1000, 600)


ground = gr.Line(gr.Point(0,450), gr.Point(1000,450))
ground.setWidth(300)
ground.setOutline('green')
ground.draw(window)


sky = gr.Line(gr.Point(0,150), gr.Point(1000,150))
sky.setWidth(300)
sky.setOutline('blue')
sky.draw(window)

cloud1_4 = gr.Circle(gr.Point(155,170),20)
cloud1_4.setFill('white')
cloud1_4.draw(window)
cloud1_5 = gr.Circle(gr.Point(165,170),20)
cloud1_5.setFill('white')
cloud1_5.draw(window)
cloud1_1 = gr.Circle(gr.Point(150,180),20)
cloud1_1.setFill('white')
cloud1_1.draw(window)
cloud1_2 = gr.Circle(gr.Point(160,180),20)
cloud1_2.setFill('white')
cloud1_2.draw(window)
cloud1_3 = gr.Circle(gr.Point(170,180),20)
cloud1_3.setFill('white')
cloud1_3.draw(window)

tree = gr.Line(gr.Point(800,500), gr.Point(800,200))
tree.setWidth(50)
tree.setOutline('brown')
tree.draw(window)

leaves1 = gr.Circle(gr.Point(800,200),30)
leaves1.setFill('green')
leaves1.draw(window)

window.getMouse()

window.close()
