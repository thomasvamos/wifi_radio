class MenuMode(AbstractMode):

  def __init__(self, lcd, mpc):
    super().__init__(lcd, mpc)

  @abstractmethod
  def tick(self):
    pass

  @abstractmethod
  def handleMenuLeftTurn(self):
    pass
  
  @abstractmethod
  def handleMenuRightTurn(self):
    pass
  
  @abstractmethod
  def handleMenuPress(self):
    pass

  @abstractmethod
  def handleVolumeLeftTurn(self):
    pass

  @abstractmethod
  def handleVolumeRightTurn(self):
    pass

  @abstractmethod
  def handleVolumePress(self):
    pass