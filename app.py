#Contrast-Pong-Game in python
# @LucaMaggio
# @mayday24

import turtle as t

import models.player as pl
import models.scene as sc
import models.ball as b
import models.pen as pe

import controllers.paddle as pad
import controllers.keyboard_binding as keybn

scene = sc.Scene()

pen = pe.Pen()

player_a = pl.Player(-370,0)
player_b = pl.Player(370,0)

def up_a():
    y = player_a.player.ycor()
    if y < 240:
      y += 20
      player_a.player.sety(y)

def down_a():
    y = player_a.player.ycor()
    if y > -240:
      y -= 20
      player_a.player.sety(y)

def up_b():
    y = player_b.player.ycor()
    if y < 240:
      y += 20
      player_b.player.sety(y)

def down_b():
    y = player_b.player.ycor()
    if y > -240:
      y -= 20
      player_b.player.sety(y)

scene.window.listen()

keybn.binding(scene.window,up_a,'w')
keybn.binding(scene.window,down_a,'s')

keybn.binding(scene.window,up_b,'Up')
keybn.binding(scene.window,down_b,'Down')

ball = b.Ball(0,0)

ball.ball.dx = 0.1
ball.ball.dy = -0.1

while True:
  scene.window.update()

  ball.ball.setx(ball.ball.xcor()+ball.ball.dx)
  ball.ball.sety(ball.ball.ycor()+ball.ball.dy)

  if(ball.ball.ycor() > 290):
    ball.ball.sety(290)
    ball.ball.dy *= -1

  if(ball.ball.ycor() < -290):
    ball.ball.sety(-290)
    ball.ball.dy *= -1

  if(ball.ball.xcor() > 380):
    ball.ball.goto(0,0)
    ball.ball.dx *= -1
    player_a.score += 1
    pen.pen.clear()
    pen.pen.write("Player A: {}\t\tPlayer B: {}".format(player_a.score, player_b.score),align="center",font=("Courier",24,"normal"))

  if(ball.ball.xcor() < -380):
    ball.ball.goto(0,0)
    ball.ball.dx *= -1
    player_b.score += 1
    pen.pen.clear()
    pen.pen.write("Player A: {}\t\tPlayer B: {}".format(player_a.score, player_b.score),align="center",font=("Courier",24,"normal"))


  if(ball.ball.xcor() > 360 and pad.collide(ball,player_b)):
    ball.ball.setx(360)
    ball.ball.dx *= -1

  if(ball.ball.xcor() < -360 and pad.collide(ball,player_a)):
    ball.ball.setx(-360)
    ball.ball.dx *= -1
