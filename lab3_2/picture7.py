import graphics as gr

win=gr.GraphWin('pic7_1',600,800)

def draw_background(win):
    ground = gr.Rectangle(gr.Point(0,400), gr.Point(600,800))
    ground.draw(win)
    ground.setFill('black')
    
    sky = gr.Rectangle(gr.Point(0,0), gr.Point(600,400))
    sky.draw(win)
    sky.setFill('lightgrey')	

def main(win):
    """draws picture"""
    draw_background(win)
    #draw_sun()
    #draw_black_cloud(win)
    #draw_house(win)
    #draw_pipes(win)
    #draw_grey_clouds(win)
    #draw_ghost(win)

main(win)

win.getMouse()
win.close()

