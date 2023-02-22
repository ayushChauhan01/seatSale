class Config(Object):
	pass

class ProdConfig(Config):
	pass

class DevConfig(Config):
	DEBUG=True
