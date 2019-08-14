class st:
	def __init__(self,state,hn,gn,fn,parent):
		self.state=state
		self.hn=hn
		self.gn=gn
		self.fn=fn
		self.parent=parent
	def __gt__(self, other):
		return self.fn > other.fn

