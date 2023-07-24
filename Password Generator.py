import random

#Create lists contain numbers, letters and symbols
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N', 'O', 
           'P', 'Q', 'R''S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c','e', 'f', 'g', 'h',
           'j', 'k', 'l', 'm', 'n','p','q','r','s','t','u','v','w','x','y','z']

numbers = ['1','2','3','4','5','6','7','8','9','0']

symbols = ['!', '@','#', '$','%','^','&','*','(',')', '_', '+','-', '/', '*']


#Get required information
number_of_letters = int(input("How many letters would you like in your password? \n"))
number_of_numbers = int(input("How many numbers would you like in your password? \n"))
number_of_symbols = int(input("How many symbols would you like in your password? \n"))
length_of_password = number_of_letters + number_of_symbols + number_of_numbers
