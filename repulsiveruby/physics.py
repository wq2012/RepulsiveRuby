def norm(vec):
    sum = 0.0
    for x in vec:
        sum += x * x
    return sum ** 0.5


def twoBallDistance(ballA, ballB):
    return norm((ballA.position[0] - ballB.position[0],
                 ballA.position[1] - ballB.position[1]))


def twoBallCollided(ballA, ballB):
    return twoBallDistance(ballA, ballB) <= ballA.radius + ballB.radius


def ballGroupCollided(ballGroup):
    num_balls = len(ballGroup.sprites())
    for i in range(num_balls):
        for j in range(i + 1, num_balls):
            ballA = ballGroup.sprites()[i]
            ballB = ballGroup.sprites()[j]
            if twoBallCollided(ballA, ballB):
                return True
    return False
