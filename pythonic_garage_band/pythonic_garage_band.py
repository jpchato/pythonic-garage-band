class Band():
  def __init__(self, name, members):
    self.name = name 
    self.members = members
    # self.play_solos = play_solos
    # Passing a function for play_solos
  
  def play_solos(self):
    pass

  
class Musician():
  # dunder init function
  # each class gets a dunder init
  def __init__(self, name):
    self.name = name
    
# template for other members
class Guitarist(Musician):
  def __init__(self, name):
    super().__init__(name)

  def __repr__(self):
    return f"Guitarist, {self.name}"

  def get_instrument(self):
    return "guitar"

  def play_solo(self):
    return "shred"

class Bassist():
  def __init__(self, name):
    self.name = name

  def get_instrument():
    return "bass"

  def play_solo():
    return "womp"


class Drummer():
  def __init__(self, name):
    self.name = name

  def get_instrument():
   return "drums"

  def play_solo():
    return "ba-dum-tss"


