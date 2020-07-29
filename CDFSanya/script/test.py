class A():
    def __init__(self,b):
        self.b = b

a = A('wgy')
print(hasattr(a, 'b'))
print(isinstance(a, A))

