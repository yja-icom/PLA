# PLA

# Introduction

Programming languages are created to help design applications that will enhance and facilitate the work of human beings. 
They are important to communicate with the machine in an easier and faster way. Nowadays there is a great number of 
languages to address different needs, but as other problems arise, many languages evolve or new ones are created.

For the class project, we decided to base our programming language to simplify problems in linear algebra. Linear
algebra is a branch of mathematics that is studied, used, and applied in many fields. People such as engineers, 
mathematicians, scientists, or students can utilize this language which will cater specifically to the topic of linear
algebra. Through our time in university, many engineering courses have topics that are related to this subject.
Our goal for this language is to create a tool that will allow to verify results, and to help in the understanding
of the different concepts studied in linear algebra. We plan to implement highly studied topics such as: vector 
addition and subtraction, vector multiplication by a scalar, magnitude and length of a vector, dot product, etc.

# Language features

The main feature of this language is to act as a calculator, and determine the result for various linear algebra concepts.
Some of the language features are the following:

1. Vector addition and subtraction (Two and three dimensions)
  - Magnitude or length of a vector (Two and three dimensions)
  - Dot product (Two and three dimensions)
  - Cross product (Three dimensions)
  - Angle between two vectors
  - Orthogonality of a vector
  - Scalar product
  - Vector division by scalar
  - Unary operations
  - Determinant
  - Variable assignment
  - Agroupation with assignment
2. Basic arithmetic
  - Addition, subtraction, multiplication, division
3. Integration with other environments:
  - Python
4. Data Structures
  - Vectors
5. Data Types
  - Numeric

# Example of Program

Vector Addition:  
(+\_+) > (1,2,1)+(1,1,1)  
Result:  
(+\_+) > (2,3,2)  

Vector Subtraction:  
(+\_+) > (1,2,0)-(1,1,1)  
Result:  
(+\_+) > (0,1,-1)  

Dot Product:  
(+\_+) > (1,2,1)*(1,1,1)  
Result:  
(+\_+) > 4  

Scalar Product:  
(+\_+) > (1,2,1)*2  
Result:  
(+\_+) > (2,4,2)  

Vector Division by Scalar:  
(+\_+) > (1,2,1)/2  
Result:  
(+\_+) > (0.5,1.5,0.5)  

Unary Operators  
Operator +:  
(+\_+) > + (1,2,1)  
Result:  
(+\_+) > (1,2,1)  

Operator -:  
(+\_+) > -(1,2,-1)  
Result:  
(+\_+) > (-1,-2,1)  

Norm of a vector:  
(+\_+) > norm((1,1,1))  
Result:  
(+\_+) > 1.73  

Perpendicular vectors:  
(+\_+) > isper((1,2,1),(1,0,1))  
Result:  
(+\_+) > false  

Assignation:  
(+\_+) > x=(1,2,1)  
(+\_+) > x  
Result:  
(+\_+) > (1,2,1)  

Agrupation:  
(+\_+) > ((1,2,1)+(1,1,1))-(2,2,2)  
Result:  
(+\_+) > (0,1,0)  

Agrupation with assignation:  
(+\_+) > x=(1,2,1)  
(+\_+) > y=(1,1,1)  
(+\_+) > z=(2,2,2)  
(+\_+) > (x+y)-z  
Resultado:  
(+\_+) > (0,1,0)  

Cross product:  
(+\_+) > x=(1,2,3)  
(+\_+) > y=(-1,1,2)  
(+\_+) > cruz(x,y)  
Result:  
(+\_+) > (1.0,-5.0,3.0)  

# Software Requirements and Specifications

This programming language is intended to support vector calculations. This will focus in an easy-to-use
format, in which the user will input the vector or vectors with an operator, and they will receive a 
result. The user will be any person who acquires the product in a need to make vector operations.

The language we will be using for developing our proposed programming language is Python. As for the parsing 
tool, we will be using PLY, an implementation of lex and yacc which are Python modules. Lex deals with the
lexical analysis part, whereas yacc is a module for creating the parser. This proposed language will be able
to run in any operating system that supports Python i.e. Windows, OS X, Linux, etc.

# Demo

A continuación se encuentran una serie de enlaces a videos que muestran las funcionalidades de la calculadora vectorial


[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/7CI66sy1ZFk/0.jpg)](http://www.youtube.com/watch?v=7CI66sy1ZFk)
