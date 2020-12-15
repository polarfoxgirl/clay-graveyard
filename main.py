tiles.set_tilemap(tilemap("""level"""))

my_sprite = sprites.create(img("""
    . . . . . . . . . . . . . .
    e e e . . . . e e e . . . .
    c d d c . . c d d c . . . .
    c b d d f f d d b c . . . .
    c 3 b d d b d b 3 c . . . .
    f b 3 d d d d 3 b f . . . .
    e d d d d d d d d e . . . .
    e d f d d d d f d e . b f b
    f d d f d d f d d f . f d f
    f b d d b b d d 2 b f f d f
    . f 2 2 2 2 2 2 d b b d b f
    . f d d d d d d d f f f f .
    . . f d b d f d f . . . . .
    . . . f f f f f f . . . . .
"""))
controller.move_sprite(my_sprite)