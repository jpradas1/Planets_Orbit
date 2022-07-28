import pygame
from planets import Planet

pygame.init()

width, height = 1000 , 900
size = [width, height]
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Planet Simulation")

white = (225, 225, 225)
yellow = (225, 225, 0)
blue = (100, 149, 237)
red = (188, 39, 50)
dark_grey = (80, 78, 81)
brown_yellow = (209, 149, 28)
orange = (209, 100, 28)
lulo = (173, 209, 28)
blue2 = (11, 117, 198)
purple = (145, 0, 140)

M_sun = 1.98892 * 10 ** 30 # kg
M_mercury = 3.30 * 10 ** 23
M_venus = 4.8685 * 10 ** 24
M_earth = 5.9742 * 10 ** 24
M_mars = 6.39 * 10 ** 23
M_jupiter = 1.8982 * 10 **27
M_saturn = 5.6834 * 10 ** 26
M_neptune = 1.02413 * 10 ** 26
M_uranus = 8.6810 * 10 ** 25

def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 3, yellow, M_sun, size)
    sun.sun = True

    mercury = Planet(0.387 * Planet.AU, 0 , 8, dark_grey, M_mercury, size)
    mercury.y_vel = -47.4 * 1000 # m / s

    venus = Planet(0.723 * Planet.AU, 0 , 14, brown_yellow, M_venus, size)
    venus.y_vel = -35.02 * 1000

    earth = Planet(1 * Planet.AU, 0 , 16, blue, M_earth, size)
    earth.y_vel = -29.783 * 1000
    
    mars = Planet(1.524 * Planet.AU, 0 , 12, red, M_mars, size)
    mars.y_vel = -24.077 * 1000

    jupiter = Planet(5.2038 * Planet.AU, 0, 20, orange, M_jupiter, size)
    jupiter.y_vel = -13.07 * 1000

    saturn = Planet(9.5826 * Planet.AU, 0, 19, lulo, M_jupiter, size)
    saturn.y_vel = -9.68 * 1000

    uranus = Planet(19.191 * Planet.AU, 0, 19, purple, M_uranus, size)
    uranus.y_vel = -6.80 * 1000

    neptune = Planet(30.07 * Planet.AU, 0, 19, blue2, M_neptune, size )
    neptune.y_vel = -5.43 * 1000


    # planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
    planets = [sun, earth, neptune]

    while run:
        clock.tick(1000)
        WIN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        neptune.draw_flower(earth, WIN, blue2)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__" :
    main()
