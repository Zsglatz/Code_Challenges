# For numbers in a range 0:9 return the string value of that number example 1 == 'One'

def switch_it_up(number):
  number_converter={0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
  return number_converter[number]