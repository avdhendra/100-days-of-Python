#Error Handling

while(True):

  try:
      age=int(input('What is your age'))
      vote=10/age
      print(age)
     #throw error
      raise ValueError('hey Cut is out')
  except ValueError:
      print("please enter a number")
      continue
  except ZeroDivisionError:
     print("Please enter age greater than 0")
     break
  else:
     print("Thank you")
     break
  finally:
     print('ok i am finally done') # it calls no matter what
  print('Can you hear me')



def sum(num1,num2):
   try:
      return num1+num2
   except TypeError:
      print('Something is Wrong')


print(sum('1',2))
