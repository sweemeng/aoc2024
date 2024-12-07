import pygame

map_size = 10

rect_size = 10


def main():
    surface = pygame.display.set_mode((map_size * rect_size, map_size * rect_size))
    maps = {(10, 10): "#", (10,11): "X"}
    guard = (5, 5)
    obs_color = (255, 0, 0)
    guard_color = (0, 255, 0)
    track_color = (0, 0, 255)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        surface.fill((0, 0, 0))
        for i in range(map_size):
            for j in range(map_size):
                if (i, j) in maps:
                    print(i * rect_size, j * rect_size, rect_size, rect_size)
                    if maps[(i, j)] == "#":

                        pygame.draw.rect(surface, obs_color, (i * rect_size, j * rect_size, rect_size, rect_size))
                    elif maps[(i, j)] == "X":
                        pygame.draw.rect(surface, track_color, (i * rect_size, j * rect_size, rect_size, rect_size))
                elif (i, j) == guard:
                    pygame.draw.rect(surface, guard_color, (i * rect_size, j * rect_size, rect_size, rect_size))
        pygame.display.flip()


if __name__ == "__main__":
    main()

