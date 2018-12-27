def twoBallDistance(ballA, ballB):
    delta_x_square = (ballA.position[0] - ballB.position[0]) ** 2
    delta_y_square = (ballA.position[1] - ballB.position[1]) ** 2
    return (delta_x_square + delta_y_square) ** 0.5


def twoBallCollided(ballA, ballB):
    return twoBallDistance(ballA, ballB) <= ballA.RADIUS + ballB.RADIUS


def ballGroupCollided(ballGroup):
    num_balls = len(ballGroup.sprites())
    for i in range(num_balls):
        for j in range(i + 1, num_balls):
            ballA = ballGroup.sprites()[i]
            ballB = ballGroup.sprites()[j]
            if twoBallCollided(ballA, ballB):
                return True
    return False
