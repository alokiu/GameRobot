# from moved.entity.platform import Platform
#
# class Rendering:
#     @staticmethod
#     def renderLevel(level, x, y):
#         for row in level:
#             for col in row:
#                 if col == '*':
#                     pl = Platform(x, y)
#                     sprite_group.add(pl)
#                     platforms.append(pl)
#                 if col == "|":
#                     if y == 320:
#                         y += 10
#                     else:
#                         y += 5
#                     pl = Block(x, y)
#                     sprite_group.add(pl)
#                     platforms.append(pl)
#                     kill_group.append(pl)
#                     if y == 330:
#                         y -= 10
#                     else:
#                         y -= 5
#                 x += 40
#             y += 40
#             x = 0