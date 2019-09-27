import graphics as gr

win=gr.GraphWin('pic7_1',600,800)

def draw_background(win):
    ground = gr.Rectangle(gr.Point(0,400), gr.Point(600,800))
    ground.draw(win)
    ground.setFill('black')
    
    sky = gr.Rectangle(gr.Point(0,0), gr.Point(600,400))
    sky.draw(win)
    sky.setFill('lightgrey')	

def draw_sun(win):
    sun = gr.Circle(gr.Point(540,60),50)
    sun.draw(win)
    sun.setFill('white')
    
def draw_black_cloud(win):
	black_cloud = gr.Oval(gr.Point(300,150), gr.Point(650,200))    	
	black_cloud.draw(win)
	black_cloud.setFill('black')

def draw_wall_and_windows(win):
	wall = gr.Rectangle(gr.Point(20,150), gr.Point(350,600))
	wall.draw(win)
	wall.setFill('#4B3819')
	
	left_window = gr.Rectangle(gr.Point(60,470), gr.Point(120,550))
	left_window.draw(win)
	left_window.setFill('#492000')
	
	middle_window = gr.Rectangle(gr.Point(150,470), gr.Point(210,550))
	middle_window.draw(win)
	middle_window.setFill('#492000')
	
	right_window = gr.Rectangle(gr.Point(240,470), gr.Point(300,550))
	right_window.draw(win)
	right_window.setFill('#FFD801')
		
	
def main(win):
    """draws picture"""
    draw_background(win)
    draw_sun(win)
    draw_black_cloud(win)
    draw_wall_and_windows(win)
    #draw_pipes(win)
    #draw_grey_clouds(win)
    #draw_ghost(win)

main(win)

win.getMouse()
win.close()







