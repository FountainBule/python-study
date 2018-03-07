import numpy as np
import matplotlib.pyplot as pl

def computation (matrix):
    """y=1/(xn+1)"""
    matrix += 1
    div = np.ones(len(matrix))
    matrix_divide = np.true_divide(1,matrix)
    return matrix_divide
    

def multi_exponent (n) :
    """Write and test a Python script which accepts a list of up to 5 values for the exponent n from input and plots the curves of
    y=1/(xn+1)
    input :
    n is a list of up to 5 exponent 
    """
    #201 evenly spaced values between -10 and 10 (including -10 and 10). 
    x = np.arange(-10,10,0.1)
    add = np.array (10)
    x = np.append(x,add)
    
    """computation"""
    matrix = np.power(x,n[0])
    matrix = computation(matrix)
    if len(n) == 1 :
        return matrix
    for exp in n[1:]:
        row = np.power(x,exp)
        row = computation(row)
        matrix = np.vstack((matrix,row))
        
    return matrix

def plot(x,y,n):
    """
    input :
    x is one dimension array
    y is one or two dimension array, which may contain 1 - 5 rows
    """
    #title and labels
    pl.title("1 / "+r'$(x^n + 1)$'+"   n="+str(n))  
    pl.ylabel("f(x)")
    pl.xlabel("x")
    #eliminate the influence of extremum
    #pl.ylim(-2,2) 
    pl.axis([-11,11,-2,2])
    
    #common property
    lw = 1.2
    
    pl.grid(True)
    if 201 == y.shape[0]:
        pl.plot(x,y,linewidth=lw)
        pl.show()
        return
    
    for y_n in y:
        pl.plot(x,y_n,linewidth=lw)
    pl.show()
    return

def cmd_line():
    """
    interacting with users in command line
    return with a list as output
    """
    exp = []
    while len(exp) < 5 :
        ch = input("Enter exponent n (q to quit)>")
        if 'q' == ch :
            break
        elif 0 == len(ch) :
            print("That's nothing!")
            continue
        elif ord(ch) > ord('9') or ord(ch) < ord('0'):
            print("That's not a number!!!")
            continue

        else:
            fl = float(ch)
            exp.append(fl)
    print("Close plot window to continue...")
    return exp
    
"""
main()
""" 
#expo = [2,4,9,6,7]

x = np.arange(-10,10,0.1)
add = np.array (10)
x = np.append(x,add)
while True:
    expo = cmd_line()
    if [] == expo :
        break
    try:
        """ and possibly a run-time warning about dividing by 0"""
        y = multi_exponent(expo)
    except TypeError as exobj:    
        print("RuntimeWarning: divide by zero encountered in true_divide")
        print(exobj)
    
    plot(x,y,expo)