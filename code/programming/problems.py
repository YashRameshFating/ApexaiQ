"""
* Program for Fibonacci series, different patterns, palindrome, etc
* Write a program for any external REST API

"""

import os
# Ensure output folder exists
output_folder = "./code/output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

class Fibonacci:
    """
    class for Fibonacci series
    Attributes:
        n (int): The number of terms in the Fibonacci series.
    Methods:
        fib(): Generates the Fibonacci series up to n terms.
    """
    def __init__(self,n):
         """
        Initialize the Fibonacci series generator.

        Args:
            n (int): Number of terms to generate.
        """
         self.n = n

    def fib(self):
        """
        Generate the Fibonacci series up to n terms
        and write it to the output file.
        """
        a,b=0,1
        for i in range(self.n):
           self._write_output(a) 
           a,b=b,a+b
    def _write_output(self, content):
        with open(os.path.join(output_folder, "fibonacci_output.txt"), "a") as f:
            f.write(str(content) + "\n")   




class Palindrome:
    """
    class for checking palindrome
    
    """
    def __init__(self,s):
          """
        Initialize the Palindrome checker.

        Args:
            s (str): String to check.
        """
          self.s=s
    def check_palindrome(self):
          """
          Check if the string is a palindrome
          and write the result to the output file.
          """
          chars=list(self.s)
          chars.reverse()
          rev_s="".join(chars)
          if self.s==rev_s:
             self._write_output(f"{self.s} is a palindrome")
          else:
             self._write_output(f"{self.s} is not a palindrome")
    def _write_output(self, content):
        with open(os.path.join(output_folder, "palindrome_output.txt"), "a") as f:
            f.write(str(content) + "\n")         
class Pattern:
    """
    class for different patterns
    Attributes:
        n (int): The number of rows in the pattern.
    Methods:
        print_pattern(): Generates and prints the pattern.
    """
    def __init__(self,n):
         """
        Initialize the Pattern generator.

        Args:
            n (int): Number of rows in the pattern.
        """
         self.n = n

    def print_pattern(self):
        pattern_lines = []
        for i in range(1, self.n + 1):       
            line = ""
            for j in range(1, i + 1):       
                line += "*"
            pattern_lines.append(line)
        self._write_output("\n".join(pattern_lines))
    def _write_output(self, content):
        with open(os.path.join(output_folder, "pattern_output.txt"), "a") as f:
            f.write(str(content) + "\n")
series=Fibonacci(10)
series.fib()
palindrome=Palindrome("madam")
palindrome.check_palindrome()
pattern=Pattern(5)
pattern.print_pattern()
       