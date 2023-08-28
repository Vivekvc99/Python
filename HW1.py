#Vivek Chauhan

#Question 1

def maximum_for(li):
    maximum = li[0]
    for i in li:
        if i > maximum:
            maximum = i
    return maximum
#Test Case 1:
list = [1,2,3,4,5]

def main(list) :
    print(maximum_for(list))
    
