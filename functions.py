def create_fleet(Pygame, s):
    Pygame.newItemByImg("alien.png", 0, 0, "alien")
    alien = Pygame.objects["alien"]
    del Pygame.objects["alien"]
    ship_height = Pygame.objects["rocket"].rect.height
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    available_space_x = s.screen["width"] - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    available_space_y = (s.screen["height"] - (3 * alien_height) - ship_height)
    number_aliens_y = int(available_space_y / (2 * alien_height))
    for row_num in range(number_aliens_y):
        for alien_number in range(number_aliens_x):
            x_pos = alien_width + 2 * alien_width * alien_number
            y_pos = alien_height+ 2 * alien_height* row_num
            name = "alien"+str(alien_number)+"/"+str(row_num)
            Pygame.newItemByImg("alien.png", x_pos, y_pos, name)
            Pygame.add2group(name=name, group="aliens")
            Pygame.objects[name].rightM = s.alien["speed_factor"]
