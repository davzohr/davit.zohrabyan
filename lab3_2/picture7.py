import graphics as gr

win=gr.GraphWin('pic7_1',600,800)

def draw_background(win):
    ground = gr.Rectangle(gr.Point(0,400), gr.Point(600,800))
    ground.draw(win)
    ground.setFill('black')
    
    sky = gr.Rectangle(gr.Point(0,0), gr.Point(600,400))
    sky.draw(win)
    sky.setFill('#999DA0')	

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
	
	x=42
	for i in range(4):
		window = gr.Rectangle(gr.Point(x,150), gr.Point(x+42,390))
		window.draw(win)
		window.setFill('#997950')
		x+=84

def draw_balcony(win):
	base = gr.Rectangle(gr.Point(0,400), gr.Point(370,440))
	base.draw(win)
	base.setFill('#222021')			

	left_column = gr.Rectangle(gr.Point(5,360), gr.Point(15,400))
	left_column.draw(win)
	left_column.setFill('#222021')		
	
	right_column = gr.Rectangle(gr.Point(355,360), gr.Point(365,400))
	right_column.draw(win)
	right_column.setFill('#222021')
	
	a=42
	for i in range(5):
		column = gr.Rectangle(gr.Point(a,360), gr.Point(a+22,400))
		column.draw(win)
		column.setFill('#222021')
		a+=66		
    
	railing = gr.Rectangle(gr.Point(15,360), gr.Point(355,340))
	railing.draw(win)
	railing.setFill('#222021')	
	
def draw_roof(win):
    roof = gr.Polygon(gr.Point(0,150), gr.Point(30,120), gr.Point(340,120), gr.Point(370,150))
    roof.draw(win)
    roof.setFill('black')
    
    pipe = gr.Rectangle(gr.Point(60,80), gr.Point(70,135))
    pipe.draw(win)
    pipe.setFill('#222021')
    
    pipe = gr.Rectangle(gr.Point(300,80), gr.Point(310,120))
    pipe.draw(win)
    pipe.setFill('#222021')
    
def draw_clouds(win):
	cloud = gr.Oval(gr.Point(20,100), gr.Point(500,50))
	cloud.draw(win)
	cloud.setFill('#48494B')
	
	cloud = gr.Oval(gr.Point(280,80), gr.Point(610,25))
	cloud.draw(win)
	cloud.setFill('#777B7E')
	
	cloud = gr.Oval(gr.Point(370,140), gr.Point(800,100))  
	cloud.draw(win)
	cloud.setFill('#777B7E')  
    
def main(win):
    """draws picture"""
    draw_background(win)
    draw_sun(win)
    draw_black_cloud(win)
    draw_wall_and_windows(win)
    draw_balcony(win)
    draw_roof(win)
    draw_clouds(win)
    #draw_pipes(win)
    #draw_grey_clouds(win)
    #draw_ghost(win)

main(win)

win.getMouse()
win.close()



