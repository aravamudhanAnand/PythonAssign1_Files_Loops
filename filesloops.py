#Read The File Into A String
f = open("unisex_names_table.csv","r")
names = f.read()

#Convert The String To A List
names_list = names.split("\n")

#Convert The List Of Strings To A List Of Lists
nested_list =[]
for row in names_list:
	comma_list= row.split(",")
	nested_list.append(comma_list)


# Convert Numerical Values
numerical_list=[]
for i in nested_list:
    name = i[0]
    share = float(i[2])
    new_list= [name, share]
    numerical_list.append(new_list)
    
    
#Filter The List
thousand_or_greater = []
for line in numerical_list:
    name = line[0]
    population = line[1]
    if population >= 1000:
        thousand_or_greater.append(name)
print(thousand_or_greater[0:10])
    
    
