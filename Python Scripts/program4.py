s = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

i=int(input("enter the number:\n"))

while(i!=s):
    print("Ha ha! You're stuck in my loop!")
    i=int(input("enter the number:\n"))
    
print("Well done, muggle! You are free now.")
