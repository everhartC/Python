class Underscore:
    def map(self, iterable, callback):
        for i in range(len(iterable)):
            iterable[i] = callback(iterable[i])
        return iterable


    def find(self, iterable, callback):
        for i in range(0, len(iterable)):
            if callback(iterable[i]):
                return iterable[i]
                #print(iterable[i])
                

    def filter(self, iterable, callback):
        new_list = []
        for i in range(len(iterable)):
            if callback(iterable[i]):
                new_list.append(iterable[i])
        return new_list
        #print(new_list)


    def reject(self, iterable, callback):
        new_list = []
        for i in range(len(iterable)):
            if not callback(iterable[i]):
                new_list.append(iterable[i])
        return new_list

# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
m = _.map([1, 2, 3, 4, 5, 6], lambda x: x * 3)
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
f = _.find([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
rej = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print("Map: ", m)
print("Find:",f)
print("Filter:", evens)
print("Reject: ", rej)
# should return [2, 4, 6] after you finish implementing the code above
