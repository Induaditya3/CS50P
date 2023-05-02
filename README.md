# CS50P
My CS50P project.
# Solution of Simultaneous Equations by Matrices
#### Video Demo:  https://vimeo.com/822926920
#### Description:

As title suggests, my project implements various mathematical functions and non-mathematical functions as well, to solve system of simultaneous equations by using concept of matrices (system must consist of atleast 2 equations in two unknowns). Plus I tried give nice looking interface to interact with application using tkinter framework. (Apparently, I did not succeed.)

Given below is a short overview with the help of an example of how this works.

The procedure for solving linear simultaneous equations in three

unknowns using matrices is:

 (i) write the equations in the form

a1 * x + b1 * y + c1 * z = d1

a2 * x + b2 * y + c2 * z = d2

a3 * x + b3 * y + c3 * z = d3

 (ii) write the matrix equation corresponding to these equations,
 i.e.

 A * X = B

 where,

A = [[ a1,b1,c1],[ a2,b2,c2],[ a3,b3,c3]]

X = [ x,y,z]

B = [ d1,d2,d3]

 (iii) determine the inverse matrix of A

 (iv) multiply each side of
 A * X = B
 by the inverse matrix of A, and


 (v) solve for x, y and z by equating the corresponding elements.
 Solution can be summed by following equation,
 X = (A ** (-1)) * B

Important thing to note is that though example illustrates procedure for solution of a system of equations in three unknowns, it can be extended to any system of equations which has unique solutions.


### How to Run the Project

One can either type "python project.py" by making current directory same as where program is stored or press "F5" after opening the file.
Also, one should make sure that tkinter is installed.

### How to Use the Project

It can be used to solve any consistent system of linear equations which arise in math, analysing electric circuit, or any other applications.
It first prompts the user for number of unknowns and then generates entry boxes of entering the coefficient of equations.
Programs then solves equations by using matrix methods.
After that, in the new frame it displays the solution.

### Included Tests

test_multiplication()
It verifies the implementeed algorithm for performing matrix multiplication.

test_determinant()
It verifies the implementeed algorithm for computing determinant of square matrix.

test_deepcopy()
It verifies if new list object is returned.

test_cofactor()
It verifies if correct cofactor is returned.

test_adjoint()
It verifies if correct adjoint is computed.

test_transpose()
It verifies if correct transpose of matrix is returned or not.

Eagle eyes amongst you might notice that tkinter functions are left out as if they cannot have bugs. But reality is I do not know how to test gui application using pytest framework.
