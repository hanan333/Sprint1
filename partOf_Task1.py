#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[17]:


# Question 2:

  #  Write a method which can calculate square value of number

   # Hints:

    #Using the ** operator


# In[18]:


class calc:
    def square (n):
       print(n**2)
a=calc
a.square(10)


# In[20]:


## Question 1 :
#Define a function which can compute the sum of two numbers.

#Hints:
#Define a function with two numbers as arguments. You can compute the sum in the function and return the value.


# In[21]:


total =0
def sum( num1, num2 ):
  
   total = num1+num2

   return total


# In[16]:



summ = sum( 10, 20 )
print ("Outside the function  total is: ", total )
print ("the sum is : ", summ )


# In[23]:


##question 3
#Define a function that can convert a integer into a string and print it in console.

#Hints:

#Use str() to convert a number to string.


# In[27]:


num = 10
 
# check  and print type of num variable
print(type(num))
 
# convert the num into string
converted_num = str(num)
 
# check  and print type converted_num variable
print(type(converted_num))


# In[ ]:


# Question 4 :
Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.

Hints:

Use int() to convert a string to integer.


# In[3]:


# function to calculate and return the sum
# parameters:
# a, b - integral numbers in string format
# return: sum of the numbers in integer format

def calculateSum (a,b):
	s = int(a) + int(b)
	return s 

# Main code 
# take two integral numbers as strings
num1 = "10"
num2 = "20"

# calculate sum
sum = calculateSum (num1, num2)

# print sum
print (" the Sum  ya gadaa = ", sum)


# In[5]:


# Question 5 :
#Define a function that can accept two strings as input and concatenate them and then print it in console.

#Hints:

#Use + to concatenate the strings


# In[ ]:





# In[ ]:


#Question 6 :
#Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

#Hints:

#Use len() function to get the length of a string


# In[7]:


#Question 7 :
#Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

#Hints:
#Use % operator to check if a number is even or odd.


# In[9]:


def check(num):
	if num%2 == 0:
		print("It is an even number")
	else:
		print("It is an odd number")

check(3)
check(4)


# In[14]:


num = int (input ("Enter any number to test whether it is odd or even: "))

if (num % 2) == 0 :

             print ("The number is even")

else:

             print ("The provided number is odd")


# In[ ]:




