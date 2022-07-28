import pygame
import math
import numpy as np

class Planet:
    AU = 149.6e6 * 1000 # m
    G = 6.67428e-11 # N*m² / kg²
    #scale = 250 / AU # 1AU = 100 pixels
    scale = 80 / AU
    timestep = 3600 * 24 # 1 day

    def __init__(self, x, y, radius, color, mass, size):
        self.x = x # AU
        self.y = y # AU
        self.radius = radius
        self.color = color
        self.mass = mass # kg
        self.size = size

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.scale + self.size[0] / 2 # rescale onto pixels
        y = self.y * self.scale + self.size[1] / 2
        white = (225, 225, 225)
        FONT = pygame.font.SysFont("comicsans", 16)

        if len(self.orbit) > 2 :
            update_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.scale + self.size[0] / 2
                y = y * self.scale + self.size[1] / 2
                update_points.append((x, y))

            pygame.draw.lines(win, self.color, False, update_points, 2)

        pygame.draw.circle(win, self.color, (x, y), self.radius)

        if not self.sun:
            distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, white)
            win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))
    
    def draw_flower(self, other, win, iro):
        
        if not self.sun and self != other:
            for point in range(len(self.orbit)) :
                if point%10 == 0 :
                    t = 1000
                    relative_dis = []
                    Rela = []
                    relative_dis.append(other.orbit[point])
                    relative_dis.append(self.orbit[point])
                    for position in relative_dis:
                        x, y = position
                        x = x * self.scale + self.size[0] / 2
                        y = y * self.scale + self.size[1] / 2
                        Rela.append((x,y))

                    pygame.draw.lines(win, iro, False, Rela, 1)
                    #pygame.image.save(win,"screenshots/"+str(t)+".jpg")
                    #t += 1 
        
    def attraction(self, other):
        other_x, other_y = other.x , other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        # distance = math.sqrt(distance_x ** 2 + distance_y ** 2) # distance between two planets
        distance2 = distance_x ** 2 + distance_y ** 2

        if other.sun:
            # self.distance_to_sun = distance
            self.distance_to_sun = math.sqrt(distance2)

        force = self.G * self.mass * other.mass / distance2
        theta = math.atan2(distance_y, distance_x)
        forcex = force * math.cos(theta)
        forcey = force * math.sin(theta)
        # force_x = force * (distance_x / distance)
        # force_y = force * (distance_y / distance)
        return forcex, forcey

    def update_position(self, planets):
        total_fx = total_fy = 0

        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx #sum over all force on a planet
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.timestep
        self.y_vel += total_fy / self.mass * self.timestep

        self.x += self.x_vel * self.timestep
        self.y += self.y_vel * self.timestep
        self.orbit.append((self.x, self.y))
