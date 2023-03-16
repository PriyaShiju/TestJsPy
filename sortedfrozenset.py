class sortedfrozenset:
    def __init__(self,items=None):
        self.items =(list(items) if (items is not None) else list())
        
    def __contains__(self,item):
        return item in self.items
        #return self.items.__contains__(item)
        