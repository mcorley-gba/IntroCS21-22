#Intro CS -- Test 3 -- Version 2

#For this version of the test, you will be making two functions:
#my_prod and my_square. 

#my_prod should take two integers as parameters
#my_prod(a,b) should return a*b, but it should calculate a*b by 
#repeated addition, not just using the * operator. For example,
#my_prod(5,3) should return 15, but the calculation inside the 
#funciton should be 5+5+5 NOT 5*3. 

#my_exponent should take a two integer parameters.
#my_exponent(a,b) should return a**b, but it should calculate a**b
#by repeated, nested application of the my_prod function (simulating
#repeated multiplication). For example, my_square(5,4) should return
#625, but it should calculate it by doing the calculation
#my_prod(my_prod(my_prod(5,5),5),5) which simulates multiplying
#5 by itself 4 times.