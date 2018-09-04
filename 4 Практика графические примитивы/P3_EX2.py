import graphics as gr

window = gr.GraphWin("window", 1000, 500)

def draw_sky(y=300):
	sky = gr.Rectangle(gr.Point(0,0), gr.Point(1000,y))
	sky.setFill('blue')
	sky.draw(window)


def draw_cloud(x=45,y=45):
	cloud_1 = gr.Circle(gr.Point(5+x, 20+y), 20)
	cloud_2 = gr.Circle(gr.Point(25+x, 15+y), 20)
	cloud_3 = gr.Circle(gr.Point(45+x, 25+y), 20)
	cloud_4 = gr.Circle(gr.Point(65+x, 15+y), 20)
	cloud_5 = gr.Circle(gr.Point(15+x, 5+y), 20)
	cloud_6 = gr.Circle(gr.Point(35+x, 0+y), 20)
	cloud_7 = gr.Circle(gr.Point(55+x, 5+y), 20)
	for x in [cloud_1, cloud_2, cloud_3, cloud_4, cloud_5, cloud_6, cloud_7]:
		x.setFill('white')
		x.setOutline('white')
	cloud_1.draw(window)
	cloud_2.draw(window)
	cloud_3.draw(window)
	cloud_4.draw(window)
	cloud_5.draw(window)
	cloud_6.draw(window)
	cloud_7.draw(window)

def draw_vigvam(x=90, y=90):
	vigvam_1 = gr.Polygon(gr.Point(60+x,310+y), gr.Point(185+x,60+y), gr.Point(310+x,310+y))
	vigvam_1.setFill('red')
	vigvam_1.setWidth(3)
	vigvam_2 = gr.Circle(gr.Point(185+x, 260+y), 30)
	vigvam_2.setFill('black')
	vigvam_3 = gr.Line(gr.Point(185+x, 60+y), gr.Point(210+x, 10+y))
	vigvam_3.setOutline('black')
	vigvam_3.setWidth(3)
	vigvam_4 = gr.Line(gr.Point(185+x, 60+y), gr.Point(160+x, 0+y))
	vigvam_4.setOutline('black')
	vigvam_4.setWidth(3)
	vigvam_1.draw(window)
	vigvam_2.draw(window)
	vigvam_3.draw(window)
	vigvam_4.draw(window)


def draw_tree(x=150, y=150):
	tree_1 = gr.Rectangle(gr.Point(290+x,50+y), gr.Point(310+x,200+y))
	tree_1.setFill('brown')
	tree_2 = gr.Polygon(gr.Point(250+x,0+y), gr.Point(300+x,100+y), gr.Point(350+x,0+y))
	tree_2.setFill('green')
	tree_1.draw(window)
	tree_2.draw(window)


def draw_totem():
	totem_1 = gr.Rectangle(gr.Point(720,400), gr.Point(800,450))
	totem_1.setFill('brown')
	totem_2 = gr.Circle(gr.Point(760, 400), 40)
	totem_2.setFill('brown')
	totem_3 = gr.Polygon(gr.Point(720,320), gr.Point(760,420), gr.Point(800,320))
	totem_3.setFill('brown')
	totem_4 = gr.Rectangle(gr.Point(720,250), gr.Point(800,320))
	totem_4.setFill('brown')
	totem_5 = gr.Polygon(gr.Point(720,250), gr.Point(760,150), gr.Point(800,250))
	totem_5.setFill('brown')
	totem_6 = gr.Circle(gr.Point(760,150), 40)
	totem_6.setFill('brown')
	totem_7 = gr.Rectangle(gr.Point(720,120), gr.Point(800,100))
	totem_7.setFill('brown')
	totem_1.draw(window)
	totem_2.draw(window)
	totem_3.draw(window)
	totem_4.draw(window)
	totem_5.draw(window)
	totem_6.draw(window)
	totem_7.draw(window)


def draw_sun(x=900,y=70):
	sun = gr.Circle(gr.Point(x, y), 40)
	sun.setFill('yellow')
	sun.setOutline('yellow')
	sun.draw(window)



draw_sky()

draw_cloud()
draw_cloud(300,80)
draw_cloud(600,60)

draw_vigvam(100,150)

draw_tree()
draw_tree(300,200)
draw_tree(200,250)

draw_totem()

draw_sun(900,100)

window.getMouse()

window.close()