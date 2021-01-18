#%%

def randInt(min=0, max=100):
    import random
    num = random.random() * (max - min) + min
    return int(num)
randInt() 		    # should print a random integer between 0 to 100
randInt(max=50) 	   # should print a random integer between 0 to 50
randInt(min=50) 	    # should print a random integer between 50 to 100
randInt(min=50, max=500)    # should print a random integer between 50 and 500
# %%