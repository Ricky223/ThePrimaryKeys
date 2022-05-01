from typing import NamedTuple


# select G_p, G_c, G_1b, G_2b, G_3b, G_ss, G_lf, G_cf, G_of, G_dh, G_ph, G_pr
# 'Pitcher', 'Catcher', 'First Base Man', 'Second Base Man', 'Third Base Man', 'Short Stop',
#                  'Left Fielder'
#                  'Center Fielder', 'Right Fielder', 'OutFielder', 'Designated Hitter', 'Pinch Hitter', 'Pinch Runner'
class Player(NamedTuple):
    name: str
    pitched: int
    catcher: int
    firstBase: int
    secondBase: int
    thirdBase: int
    shortStop: int
    leftField: int
    centerField: int
    outField: int
    designatedHitter: int
    pinchHitter: int
    pinchRunner: int
