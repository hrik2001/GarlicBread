import os
if not (os.path.isfile("bin/config.py")):
    print("creating config file (bin/config.py) with default password \"password\"")
    f = open("bin/config.py" , "w")
    f.write("password='password'")

