class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        print(f"Adding: {num}, Total: {self.result}")
        return self
    def subtract(self, num, *nums):
        self.result -= num
        print(f"Subtracting: {num}, Total: {self.result}")
        return self
# create an instance:
md = MathDojo()
x = md.add(4).add(3).add(2)
y = md.subtract(1).subtract(2).subtract(2)

# to test:
#x = md.add(2).add(2,5,1).subtract(3,2).result
#print(x)	# should print 5
# run each of the methods a few more times and check the result!

if "__name__" == "__main__":
    md = MathDojo()