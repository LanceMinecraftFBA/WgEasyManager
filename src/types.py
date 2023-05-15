import datetime

class WireGuardKey:
  def __init__(self, id, name, enabled, address, publicKey, createdAt, updatedAt, persistentKeepAlive):
    self.id: int = id
    self.name: str = name
    self.enabled: bool = enabled
    self.address: str = address
    self.publicKey: str = publicKey
    self.createdAt: datetime = createdAt
    self.updatedAt: Optional[datetime] = updatedAt
    self.persistentKeepAlive: str = persistentKeepAlive

class LoginStatus:
  def __init__(self, requiresPassword, authenticated):
    self.requiresPassword: bool = requiresPassword
    self.authenticated: bool = authenticated

class WgEasyManagerOptions:
  def __init__(self, url, password):
    self.url: str = url
    self.password: str = password
