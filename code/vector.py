# -----------------------------------------------------------------------------
# vector.py
#
# A simple calculator with vector.
# -----------------------------------------------------------------------------

import math

tokens = (
    'VECTOR', 'VECTOR2',
    'NAME', 'NUMBER',
    'EQUALS', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN','RPAREN','LBRACKET', 'RBRACKET',
    'COMMA',
    'NORMA', 'ISPER', 'DET', 'CRUZ', 'ANGULO',
    )

#Tokens
t_EQUALS  = r'='
t_PLUS    = r'\+'
t_MINUS   = r'\-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA   = r','   
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_VECTOR  = r'\([-|+]?[0-9]+(\.[0-9][0-9]?)?\,[-|+]?[0-9]+(\.[0-9][0-9]?)?\,[-|+]?[0-9]+(\.[0-9][0-9]?)?\)'
t_VECTOR2  = r'\([-|+]?[0-9]+(\.[0-9][0-9]?)?\,[-|+]?[0-9]+(\.[0-9][0-9]?)?\)'


def t_NUMBER(t):
    r'\d+(\.\d{1,2})?'    
    t.value = float(t.value)
    return t

def t_NORMA(t):
    r'norma'
    return t

def t_ANGULO(t):
    r'angulo'
    return t

def t_ISPER(t):
    r'isper'
    return t

def t_DET(t):
    r'det'
    return t
    
def t_CRUZ(t):
    r'cruz'
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()

# Class vector (auxiliar para realizar las operaciones con vectores)
class Vector (object):
    def __init__ (self, p):        
        if (len(p)== 7):
			self.dim = 3
			self.x = float(p[1])
			self.y = float(p[3])
			self.z = float(p[5])    
        elif(len(p)== 5):
            self.dim = 2
            self.x = float(p[1])
            self.y = float(p[3])

    def __repr__(self):               
        if (self.dim==3):
            a='(%s, %s, %s)' % (self.x, self.y, self.z)
        elif(self.dim==2):
            a='(%s, %s)' % (self.x, self.y)
        return a
    
    def __add__(self, other):
        if (self.dim == 3 and other.dim == 3):
            x = self.x + other.x
            y = self.y + other.y
            z = self.z + other.z          
            return Vector(['[',x,',',y,',',z,']'])
        elif (self.dim == 2 and other.dim == 2):
            x = self.x + other.x
            y = self.y + other.y                      
            return Vector(['[',x,',',y,']'])

    def __sub__(self, other):
        if (self.dim == 3 and other.dim == 3):
            x = self.x - other.x
            y = self.y - other.y
            z = self.z - other.z          
            return Vector(['[',x,',',y,',',z,']'])
        elif (self.dim == 2 and other.dim == 2):
            x = self.x - other.x
            y = self.y - other.y                      
            return Vector(['[',x,',',y,']'])

    def inner(self, other):
        """ Returns the dot product (inner product) of self and other vector
        """
        if (self.dim == 3 and other.dim == 3):
            suma = 0
            suma += self.x*other.x
            suma += self.y*other.y
            suma += self.z*other.z
            return suma
        elif (self.dim == 2 and other.dim == 2):
            suma = 0
            suma += self.x*other.x
            suma += self.y*other.y            
            return suma
        

    def __mul__(self, other):
       """ Returns the dot product of self and other if multiplied
           by another Vector.  If multiplied by an int or float,
           multiplies each component by other.
       """
       if (self.dim == 3):
            if type(other) == type(self):
                return self.inner(other)
            elif type(other) == type(1.0):
                x = self.x*other
                y = self.y*other
                z = self.z*other       
                return Vector(['[',x,',',y,',',z,']'])
       elif (self.dim == 2):
          if type(other) == type(self):
              return self.inner(other)
          elif type(other) == type(1.0):
              x = self.x*other
              y = self.y*other              
              return Vector(['[',x,',',y,']'])

    def __div__(self, other):
        if (self.dim == 3):
            if type(other) == type(1.0):
                x = self.x/other
                y = self.y/other
                z = self.z/other
                return Vector(['[',x,',',y,',',z,']'])            
        elif (self.dim == 2):
            if type(other) == type(1.0):
                x = self.x/other
                y = self.y/other                
                return Vector(['[',x,',',y,']'])           

    def __neg__(self):
        if (self.dim == 3):
            x = -self.x
            y = -self.y
            z = -self.z
            return Vector(['[',x,',',y,',',z,']'])
        elif (self.dim == 2):
            x = -self.x
            y = -self.y            
            return Vector(['[',x,',',y,']'])

    def __pos__(self):
        if (self.dim == 3):
            x = self.x
            y = self.y
            z = self.z
            return Vector(['[',x,',',y,',',z,']'])
        elif (self.dim == 2):
            x = self.x
            y = self.y            
            return Vector(['[',x,',',y,']'])        
        
    def norma(self):
        if (self.dim == 3):
            aux = 0
            aux += self.x**2
            aux += self.y**2
            aux += self.z**2
            a = math.sqrt(aux)
            return a
        elif (self.dim == 2):
            aux = 0
            aux += self.x**2
            aux += self.y**2            
            a = math.sqrt(aux)
            return a
    
    def posicion (self, pos):
		if (self.dim == 3):
			if pos == 1:
				return self.x
			if pos == 2:
				return self.y
			if pos == 3:
				return self.z
		if (self.dim == 2):
			if pos == 1:
				return self.x
			if pos == 2:
				return self.y
			    
    def pro_cruz(self,other):
		if type(other) == type(self):
			x = determinante(self.y,self.z,other.y,other.z)
			y = (-1)*determinante(self.x,self.z,other.x,other.z)
			z = determinante(self.x,self.y,other.x,other.y)
		return Vector(['[',x,',',y,',',z,']']) 
	
    def det(self,other):
        if (self.dim == 2 and other.dim == 2):
            return self.x*other.y - self.y*other.x
        if (self.dim == 3 and other.dim == 3):
            return 'No se puede'
    
    def angulo(self,other):
		if (self.dim == 2 and other.dim == 2):
			dot = self.inner(other)
			nor1 = self.norma()
			nor2 = other.norma()
			aux = math.acos(dot/(nor1*nor2))
			return math.degrees(aux)
		if (self.dim == 3 and other.dim == 3):
			dot = self.inner(other)
			nor1 = self.norma()
			nor2 = other.norma()
			aux = math.acos(dot/(nor1*nor2))
			return math.degrees(aux)
		
		
def determinante (a1,a2,b1,b2):
    return a1*b2-a2*b1




precedence = (
    ('left','PLUS', 'MINUS'),
    ('right','UMINUS','UPLUS'),
    )

# dictionary of names (for storing variables)
names = { }

def p_statement_assign(p):
    'statement : NAME EQUALS expression'
    names[p[1]] = p[3]

def p_statement_expr(p):
    'statement : expression'
    print(p[1])

def p_expression_vector(p):
    '''expression : VECTOR
                  | VECTOR2'''
    a=list(p[1])
    if (a.count(',') == 2):
		x=''
		y=''
		z=''
		flag = 1
		flag1 = 1
		flag2 = 1
		i = 1    
		while (flag):
			if a[i] != ',':
				x +=a[i]
				i +=1
			else:
				flag=0
				i +=1       
		
		while (flag1):
			if a[i] != ',':
				y +=a[i]
				i +=1
			else:
				flag1=0
				i +=1
				
		while (flag2):
			if a[i] != ')':
				z +=a[i]
				i +=1
			else:
				flag2=0
				i +=1
		x = float(x)
		y = float(y)
		z = float(z)
		p[0] = Vector(['[',x,',',y,',',z,']'])
    elif(a.count(',') == 1):        
        x=''
        y=''
        flag = 1		
        flag2 = 1
        i = 1    
        while (flag):
        	if a[i] != ',':
        		x +=a[i]
        		i +=1
        	else:
        		flag=0
        		i +=1
        		
        while (flag2):
        	if a[i] != ')':
        		y +=a[i]
        		i +=1
        	else:
        		flag2=0
        		i +=1
        x = float(x)
        y = float(y)        
        p[0] = Vector(['[',x,',',y,']'])       
        

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression 
                  | NUMBER TIMES expression
                  | expression DIVIDE expression'''
    if p[2] == '+'  :
        p[0]=p[1]+p[3] 
    elif p[2] == '-'  :
        p[0]=p[1]-p[3]
    elif p[2] == '*'  :
        p[0]=p[1]*p[3]
    elif p[2] == '/'  :
        p[0]=p[1]/p[3]    

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]

def p_expression_uplus(p):
    'expression : PLUS expression %prec UPLUS'
    p[0] = +p[2]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'    
    p[0] = p[2]

def p_expression_norma(p):
    'expression : NORMA LPAREN expression RPAREN'
    if p[1] == 'norma':
        try:
            p[0] = p[3].norma()
        except:
            print("Undefined type '%s'" % p[3])


def p_expression_isper(p):
    'expression : ISPER LPAREN expression COMMA expression RPAREN'
    if p[1] == 'isper':
        if (p[3]*p[5]==0):
            p[0] = 'True'
        else:
            p[0] = 'False'    

def p_expression_cruz(p):
    'expression : CRUZ LPAREN expression COMMA expression RPAREN'
    if p[1] == 'cruz':
        p[0] = p[3].pro_cruz(p[5])

def p_expression_det(p):
    'expression : DET LPAREN expression COMMA expression RPAREN'
    if p[1] == 'det':
        p[0] = p[3].det(p[5])

def p_expression_angulo(p):
	'expression : ANGULO LPAREN expression COMMA expression RPAREN'
	if p[1] == 'angulo':
		p[0] = p[3].angulo(p[5])


def p_expression_posicion(p):
    'expression : expression LBRACKET NUMBER RBRACKET'
    if (type(p[1]) is Vector):
        p[0] = p[1].posicion(p[3])


def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_error(p):
    print("Syntax error at '%s'" % p.value)

def p_expression_name(p):
    'expression : NAME'
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0


import ply.yacc as yacc

yacc.yacc()

#Desacomentar esta parte y comentar la seccion de codigo de abajo
#para utilizar el modo interactivo

#while True:
#    try:
#        s = raw_input('(+_+) > ')   # use input() on Python 3
#    except EOFError:
#        break
#    yacc.parse(s)

infile = open('prueba.txt', 'r')
# Mostramos por pantalla lo que leemos desde el fichero
print 'Probando Vector'
for line in infile:
	yacc.parse(line)
	
    
# Cerramos el fichero.
infile.close()

