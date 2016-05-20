from character_repr import Char_Repr
from picture import Picture

def main():
    p = Picture("training_data/a1.png")
    c = Char_Repr(p)
    print(c.points)
