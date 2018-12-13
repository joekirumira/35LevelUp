

# animal = "elephant"
#
# for char in animal:
#     print(char)

# weight = [34,64,28,55,68,20]
# print(weight[-2])
#
# weight.insert(2, 99)
# print(weight)

# capitals = {"Uganda":"Kampala", "Kenya":"Nairobi"}
# capitals["Rwanda"] = "Kigali"
# print(capitals)
# del capitals["Kenya"]

# def drinking_age(age):
#     if age>= 18:
#         return "drink "
#     else:
#         return "try water"
#
# print(drinking_age(12))

def sample(*args):
    z = 0
    for number in args:
        z += number
    return z
print(sample(1,2,3))

# def human(**kwargs):
#     return kwargs
# person = {'name':'Kengo', 'occupation':'Developer'}
# print(human(**person))









