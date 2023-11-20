#Create a function "get_palindrome" that is given a string and returns a list
#of all palindromes in the string
def get_palindromes(input_string):
  def is_palin(s):
    return s==s[::-1]
  words=input_string.split()
  palindromes=[i for i in words if is_palin(i)]
  return palindromes

ip="level radar madam english oops"
print(get_palindromes(ip))
