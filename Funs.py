class Pygame():
    class PygameError(Exception):
        def __init__(self, message=None):
            self.message = message
            super().__init__(message)
    def __init__(self):
        try:
            import pygame
            import Object
        except:
            raise self.PygameError("Pygame is not installed.")
        pygame.init()
        self.object = Object
        self.pygame = pygame
        self.objects = {}
        self.groups = {}
    def screen(self,width=0,height=0,caption="",color=(255,255,255)):
        self.screen = self.pygame.display.set_mode((width,height))
        self.pygame.display.set_caption(caption)
        self.screen.fill(color)
        self.color = color
        self.pygame.display.flip()
    def update(self, items2update=[], groups2update=[]):
        items2update += sum([self.groups[group] for group in groups2update],[])
        for o in [self.objects[ob] for ob in items2update]:
            o.move()
    def display(self, items2show=[], groups2show=[]):
        self.screen.fill(self.color)
        items2show += sum([self.groups[group] for group in groups2show],[])
        for o in [self.objects[ob] for ob in items2show]:
            o.blitme()
        self.pygame.display.flip()
    def handleItemEvents(self,triggers={}):
        def doSearch(Dict, pos, item):
            d = {}
            for key in Dict.keys():
                if key.split(" ")[pos] == item:
                    d[key] = Dict[key]
            return d
        for key, value in doSearch(triggers,0,"ONRIGHTEDGE").items():
            k = " ".join(key.split(" ")[1:])
            if self.objects[k].onrightedge():
                value(self)
        for key, value in doSearch(triggers,0,"ONLEFTEDGE").items():
            k = " ".join(key.split(" ")[1:])
            if self.objects[k].onleftedge():
                value(self)
        for key, value in doSearch(triggers,0,"ONTOPEDGE").items():
            k = " ".join(key.split(" ")[1:])
            if self.objects[k].ontopedge():
                value(self)
        for key, value in doSearch(triggers,0,"ONBOTTOMEDGE").items():
            k = " ".join(key.split(" ")[1:])
            if self.objects[k].onbottomedge():
                value(self)
        for key, value in doSearch(triggers,0,"COLLIDE").items():
            k = key.split(" ")[1:]
            if self.objects[k[0]].rect.colliderect(self.objects[k[1]]):
                value(self)
    def handleItem_GroupEvents(self, triggers={}):
        t2 = {}
        for key, value in triggers.items():
            k = key.split(" ")
            group = self.groups[k[-1]]
            for item in group:
                t2[" ".join(k[:-1])+" "+item] = value
        self.handleItemEvents(t2)
    def handleGroup_GroupEvents(self, triggers={}):
        def doSearch(Dict, pos, item):
            d = {}
            for key in Dict.keys():
                if key.split(" ")[pos] == item:
                    d[key] = Dict[key]
            return d
        for key, value in doSearch(triggers,0,"COLLIDE").items():
            k = key.split(" ")[1:]
            for i1 in [self.objects[name] for name in self.groups[k[0]]]:
                for i2 in [self.objects[name] for name in self.groups[k[1]]]:
                    if i1.rect.colliderect(i2):
                        value(self, i1.name, i2.name)
    def handleKeyEvents(self,triggers={}):
        def doSearch(Dict, pos, item):
            d = {}
            for key in Dict.keys():
                if key.split(" ")[pos] == item:
                    d[key] = Dict[key]
            return d
        def keys(Dict, pyg):
            ips = {"LEFT":pyg.K_LEFT, "RIGHT":pyg.K_RIGHT, "UP":pyg.K_UP, "DOWN":pyg.K_DOWN, "a":pyg.K_a,
                   "b":pyg.K_b, "c":pyg.K_c, "d":pyg.K_d, "e":pyg.K_e, "f":pyg.K_f, "g":pyg.K_g,
                   "h":pyg.K_h, "i":pyg.K_i, "j":pyg.K_j, "k":pyg.K_k, "l":pyg.K_l, "m":pyg.K_m,
                   "n":pyg.K_n, "o":pyg.K_o, "p":pyg.K_p, "q":pyg.K_q, "r":pyg.K_r, "s":pyg.K_s,
                   "t":pyg.K_b, "u":pyg.K_c, "v":pyg.K_d, "w":pyg.K_e, "x":pyg.K_f, "y":pyg.K_g,
                   "z":pyg.K_z, "1":pyg.K_1, "2":pyg.K_2, "3":pyg.K_3, "4":pyg.K_4, "5":pyg.K_5,
                   "6":pyg.K_6, "7":pyg.K_7, "8":pyg.K_8, "9":pyg.K_9, "0":pyg.K_0, "f1":pyg.K_F1,
                   "f2":pyg.K_F2, "f3":pyg.K_F3, "f4":pyg.K_F4, "f5":pyg.K_F5, "f6":pyg.K_F6,
                   "f7":pyg.K_F7, "f8":pyg.K_F8, "f9":pyg.K_F9, "f10":pyg.K_F10, "f11":pyg.K_F11,
                   "f12":pyg.K_F12, "Lshift":pyg.K_LSHIFT, "Rshift":pyg.K_RSHIFT,
                   "Lctrl":pyg.K_LCTRL, "Rctrl":pyg.K_RCTRL, "Lalt":pyg.K_LALT, "Ralt":pyg.K_RALT,
                   "Backspace":pyg.K_BACKSPACE, "Tab":pyg.K_TAB, "Clear":pyg.K_CLEAR,
                   "Return":pyg.K_RETURN, "Pause":pyg.K_PAUSE, "Escape":pyg.K_ESCAPE,
                   "Space":pyg.K_SPACE, "!":pyg.K_EXCLAIM, "\"":pyg.K_QUOTEDBL, "#":pyg.K_HASH,
                   "$":pyg.K_DOLLAR, "&":pyg.K_AMPERSAND, "'":pyg.K_QUOTE, "(":pyg.K_LEFTPAREN,
                   ")":pyg.K_RIGHTPAREN, "*":pyg.K_ASTERISK, "+":pyg.K_PLUS, ",":pyg.K_COMMA,
                   "-":pyg.K_MINUS, ".":pyg.K_PERIOD, "/":pyg.K_SLASH, "=":pyg.K_EQUALS,
                   "Home":pyg.K_HOME, "End":pyg.K_END, "pg up":pyg.K_PAGEUP, "pg dn":pyg.K_PAGEDOWN,
                   "Insert":pyg.K_INSERT, "Delete":pyg.K_DELETE}
            for item, pygame in ips.items():
                if event.key == pygame and doSearch(t2,1,item):
                    for fun in doSearch(t2,1,item).values():
                        fun(self)
        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT and doSearch(triggers,0,"QUIT"):
                for value in doSearch(triggers,0,"QUIT").values():
                    value(self)
            elif event.type == self.pygame.KEYDOWN and doSearch(triggers,0,"KEYDOWN"):
                t2 = doSearch(triggers,0,"KEYDOWN")
                keys(t2, self.pygame)
            elif event.type == self.pygame.KEYUP and doSearch(triggers,0,"KEYUP"):
                t2 = doSearch(triggers,0,"KEYUP")
                keys(t2, self.pygame)
    def newItemByImg(self, img, x, y, name, offscreen=False):
        self.objects[name] = self.object.Img(self.screen, img, x, y, name,
                                             offscreen)
    def newItemByRect(self, x, y, width, height, color, name, offscreen=False):
        self.objects[name] = self.object.Rect(self.screen, x, y, width, height,
                                              color, name, offscreen)
    def newGroup(self, name):
        self.groups[name] = []
    def add2group(self, name, group):
        try:
            self.groups[group].append(name)
            self.objects[name].myGroups.append(group)
        except KeyError:
            raise self.PygameError(f"Group {group} does not exist.")
    def destroyItem(self, name):
        for group in self.objects[name].myGroups:
            self.removeFromGroup(name, group)
        self.objects[name].kill()
        del self.objects[name]
    def removeFromGroup(self, name, group):
        try:
            self.groups[group].remove(name)
        except KeyError:
            raise self.PygameError(f"Group {group} does not exist.")
        except ValueError:
            raise self.PygameError(f"Item {name} does not exist.")
