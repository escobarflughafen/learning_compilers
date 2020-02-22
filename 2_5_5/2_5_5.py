class Parser:
    lookahead = ''
    expression = ''
    postfix = ''

    def __init__(self, expression):
        self.expression = expression
    
    def expr(self):
        term()
        while(True):
            if '+' == self.lookahead