# input , processing , output

# input : name , add to info_name , search in info_name to get any name

num_of_names = input("please enter your number of names : ")
counter = 0
stor_names = []

while counter < int(num_of_names):
    name = input("name : ")
    stor_names.append(name)
    counter = counter + 1

print("---------------------------------------")

i = 0

while i < stor_names.__len__():
    print("name "+ str(i+1) + ": " + stor_names[i])
    print("---------------------------------------")
    i = i + 1
