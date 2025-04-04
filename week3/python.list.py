def print_list(elements):
    for elements in elements:
        print(elements)
def largest(elements):
    for i in elements :
        largest=0
        largest=max(largest,i)
    print("largest=",largest)    
limit = int(input("enter the length of list:"))
elements = []
for i in range(limit):
    temp = int(input(f"emter number {i+1}: "))
    elements.append(temp)
print_list(elements)
largest(elements)
    
