def collide(ball,player):
    if(ball.ball.ycor() < player.player.ycor() + 40 and ball.ball.ycor() > player.player.ycor() -40):
      return True
    return False
