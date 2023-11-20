#Write a python program using functions to find the largest number in a list.
def largest_in_list(a):
  maxno=a[0]
  for i in range (1,5):
    if(a[i]>maxno):
      max=a[i];
  print("Largest element is ", maxno)
a1=[10,2,5,7,8]
largest_in_list(a1)
