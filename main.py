class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Lexer:
    def __init__(self, code):
        self.code = code
        self.pos = 0
        self.tokens = []

    def tokenize(self):
        while self.pos < len(self.code):
            if self.code[self.pos].isspace():
                self.pos += 1
            elif self.code[self.pos].isdigit():
                self.tokenize_number()
            elif self.code[self.pos].isalpha():
                self.tokenize_identifier()
            elif self.code[self.pos] in '+-*/()':
                self.tokens.append(Token(self.code[self.pos], self.code[self.pos]))
                self.pos += 1
            else:
                raise Exception("Invalid character")
        return self.tokens

    def tokenize_number(self):
        num = ''
        while self.pos < len(self.code) and self.code[self.pos].isdigit():
            num += self.code[self.pos]
            self.pos += 1
        self.tokens.append(Token('NUMBER', int(num)))

    def tokenize_identifier(self):
        id = ''
        while self.pos < len(self.code) and self.code[self.pos].isalpha():
            id += self.code[self.pos]
            self.pos += 1
        self.tokens.append(Token('IDENTIFIER', id))

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        return self.parse_expr()

    def parse_expr(self):
        left = self.parse_term()
        while self.pos < len(self.tokens) and self.tokens[self.pos].value in '+-':
            op = self.tokens[self.pos].value
            self.pos += 1
            right = self.parse_term()
            left = (op, left, right)
        return left

    def parse_term(self):
        left = self.parse_factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos].value in '*/':
            op = self.tokens[self.pos].value
            self.pos += 1
            right = self.parse_factor()
            left = (op, left, right)
        return left

    def parse_factor(self):
        if self.tokens[self.pos].type == 'NUMBER':
            num = self.tokens[self.pos].value
            self.pos += 1
            return num
        elif self.tokens[self.pos].type == 'IDENTIFIER':
            id = self.tokens[self.pos].value
            self.pos += 1
            return id
        elif self.tokens[self.pos].value == '(':
            self.pos += 1
            expr = self.parse_expr()
            self.pos += 1
            return expr
        else:
            raise Exception("Invalid syntax")

lexer = Lexer("2 + 3 * 4")
tokens = lexer.tokenize()
parser = Parser(tokens)
result = parser.parse()
print(result)