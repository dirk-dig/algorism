class cell:
	def  __init__(self, x, y=none):
		self.data=x
		sef.next=y
	#値の取り出し
	def first(self):
		return self.data
	def rest(self):
		return self.next
	#値の書き換え
def set_first(self, x): self.data=x
def set_rest(self, x): self.next=x