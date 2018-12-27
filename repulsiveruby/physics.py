def twoBallDistance(ballA, ballB):
    distance = ((ballA.position[0]-ballB.position[0])
                ** 2+(ballA.position[1]-ballB.position[1])**2)**0.5
    return distance


def collide(ball1, ball2, ball3, ball4):
    collide0 = False
    if twoBallDistance(ball1, ball2) < 65:
        collide0 = True
    if twoBallDistance(ball1, ball3) < 65:
        collide0 = True
    if twoBallDistance(ball1, ball4) < 65:
        collide0 = True
    if twoBallDistance(ball2, ball3) < 65:
        collide0 = True
    if twoBallDistance(ball2, ball4) < 65:
        collide0 = True
    if twoBallDistance(ball3, ball4) < 65:
        collide0 = True
    return collide0
