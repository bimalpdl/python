https://replit.com/@mebimalpdl1/day4100-days#main.py 


# everything enclose inside "\033[<number>m" will be colored accoring to color value. 0 is the color number by default and color value starts from 30 and ranges upto 37. If you change the color, you need to change back to the default ie. 0 as done below.

print("Hello, there", "\033[31m","This is a warning !","\033[0m", "And this is normal text.")
