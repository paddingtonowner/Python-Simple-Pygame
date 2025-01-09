import Funs as pyg
from settings import Settings
import functions as f

s = Settings()
p = pyg.Pygame()

p.screen(s.screen["width"],s.screen["height"],
         s.screen["title"],s.screen["bgcolor"])

p.newItemByImg("rocket.png", s.screen["width"]/2, s.screen["height"], "rocket")
p.newGroup("aliens")
p.newGroup("bullets")
f.create_fleet(p, s)

def end_game(Pygame):
    Pygame.pygame.display.quit()
    raise SystemExit
def old_bullets(s, p):
    for name in p.groups["bullets"][:]:
        bullet = p.objects[name]
        if bullet.rect.bottom < 0:
            bullet.kill()
            del p.objects[name]
            p.removeFromGroup(name=name,group="bullets")
def new_bullet(Pygame):
    global s
    if len(Pygame.groups["bullets"]) < s.bullet["allowed"]:
        bulletname = "bullet"+str(s.bullet["num"])
        s.bullet["num"] += 1
        rocket = Pygame.objects["rocket"]
        p.newItemByRect(rocket.rect.centerx, rocket.rect.top, s.bullet["width"],
                        s.bullet["height"], s.bullet["color"], bulletname, True)
        p.objects[bulletname].upM = s.bullet["speed_factor"]
        Pygame.add2group(name=bulletname,group="bullets")
def ship_left_on(Pygame):
    global s
    Pygame.objects["rocket"].leftM = s.ship["speed_factor"]
def ship_left_off(Pygame):
    Pygame.objects["rocket"].leftM = 0
def ship_right_on(Pygame):
    global s
    Pygame.objects["rocket"].rightM = s.ship["speed_factor"]
def ship_right_off(Pygame):
    Pygame.objects["rocket"].rightM = 0
def on_left_edge(Pygame):
    global s
    for alien in [Pygame.objects[name] for name in Pygame.groups["aliens"]]:
        alien.rect.centery += s.alien["drop_speed"]
        alien.rightM = s.alien["speed_factor"]
        alien.leftM = 0
def on_right_edge(Pygame):
    global s
    for alien in [Pygame.objects[name] for name in Pygame.groups["aliens"]]:
        alien.rect.centery += s.alien["drop_speed"]
        alien.leftM = s.alien["speed_factor"]
        alien.rightM = 0
def collide(Pygame):
    print("Game Over!")
    end_game(Pygame)
def alien_hit(Pygame, alien, bullet):
    try:
        Pygame.removeFromGroup(name=alien, group="aliens")
        Pygame.removeFromGroup(name=bullet, group="bullets")
    except:
        pass

while True:
    events = {}
    p.display(["rocket"],["bullets","aliens"])
    p.update(["rocket"],["bullets","aliens"])
    old_bullets(s, p)
    p.handleItemEvents(events)
    p.handleItem_GroupEvents({"ONLEFTEDGE aliens":on_left_edge,
                         "ONRIGHTEDGE aliens":on_right_edge,
                         "COLLIDE rocket aliens":collide})
    p.handleGroup_GroupEvents({"COLLIDE aliens bullets":alien_hit})
    p.handleKeyEvents({"KEYDOWN LEFT":ship_left_on,"KEYDOWN RIGHT":ship_right_on,
          "KEYUP LEFT":ship_left_off,"KEYUP RIGHT":ship_right_off,
          "KEYDOWN Space":new_bullet, "KEYDOWN q":end_game, "QUIT":end_game})
