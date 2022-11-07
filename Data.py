class TokenType:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


TokenTypes = {
    "String": TokenType("String"),
    "Number": TokenType("Number"),
    "Keyword": TokenType("Keyword"),
    "Operator": TokenType("Operator"),
    "Identifier": TokenType("Identifier"),
    "Delimiter": TokenType("Delimiter"),
    "Indent": TokenType("Indent"),
    "Comment": TokenType("Comment"),
    "LineBreak": TokenType("LineBreak"),
    "Boolean": TokenType("Boolean")
}


class Group:

    def __init__(self, t):
        self.type = t
        self.tokens = [[]]

    def append(self, token, line=-1):
        self.tokens[line].append(token)

    def newline(self):
        self.tokens.append([])


Booleans = {"true", "false"}

PureOperators = {
    "=",  #equals
    "!",  #not, and factorial
    '~', #about
    "<",  #less than
    ">",  #more than
    "==",
    "<=",  #less than or equal to
    ">=",  #more than or equal to
    "!=",  #not equal to
    "~=", #about equal to
    "&",  #and
    "|",  #or
    "x|",  #xor (exculsive or)
    "+",  #add
    "-",  #subtract
    "/",  #divide
    "*",  #multiplication
    "^",  #exponet 
    "%",  #mod
    "@",  #at. reference
    "?",  # x.y? will be null if x.y doesn't exist or if it is null
    "->",  # For defining a function return type
    #"$",  #idk
    #"<-",  #idk, we can use it for something maybe.
}
#!& should be valid, not and.
#!| should be valid, not or.
#!x| should be valid, not xor.
#!= should be valid, not equal.
Operators = PureOperators | {
    'not',  #not operator
    'and',  #and operator
    'or',  #or operATOR
    'xor',  #XOR
    'in'
}
OrderOfOps = {
  0: ['?'],
  1: ['~', '!', '@'],
  2: ['^'],
  3: ['*', '/'],
  4: ['-', '+'],
  5: ['%'],
  6: ['=', '~=', '<', '>', '<=', '>=', '!=', 'in', '=='],
  7: ['&', '|', 'x|', 'and', 'or', 'xor'],
  8: ['->'],
  9: [],
  10: [],
  11: [],
  12: [],
  13: [],
} #USE: https://stackoverflow.com/questions/28256/equation-expression-parser-with-precedence

Quotes = {'"', "'", '`'}

Groups = (('(', ')'), ('[', ']'), ('{', '}'))

Whitespaces = {
    ' ',  #Space
    '\t',  #Tab
    '​',  #zero width space
    ' ',  #hair space
    ' ',  #six per em space
    ' ',  #thin space
    ' ',  #punctuation space
    ' ',  #four per em space
    ' ',  #three per em space
    ' ',  #figure space
    ' ',  #en space
    ' ',  #em space
    '⠀',  #braile blank
}

Delimiters = {
    ":",  #Colon, used for defining blocks and for types
    "(",  #lparen
    ")",  #rparen
    ",",  #comma
    "{",  #lbrace
    "}",  #rbrace
    "[",  #lbracket
    "]",  #rbracket
    ".",  #period,
    ';',  #newline
}

Keywords = {
    'class',
    'extends',
    'type',
    'extending',
    'function',
    'for',
    'while',
    'if',
    'else',  #Blocks
    'return',
    'delete',
    'static',
    'include',
    'async',
    'yield',  
    'let', #Statements
    'as',
    'from',#other
}


#https://replit.com/@Programit/Redesign