class Env(dict):
    def __init__(self, env = None):
        self.env = env
    
    def get(self, word):
        try:
            return self[word]
        except KeyError:
            if(None == self.env):
                return None
            else:
                return self.env.get(word)


a = Env()
b = Env(a)
c = Env(b)

a['x'] = 'int'
a['y'] = 'char'
b['y'] = 'bool'
a['z'] = 'float'

print(b.get('x'), b.get('y'), c.get('z'), a.get('x'), a.get('y'))