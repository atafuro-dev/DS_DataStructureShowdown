#3. Remove Duplicates (Keep Order)
#Return the values in the order they first appeared, without duplicates.
#Input: ["apple", "banana", "apple", "kiwi", "banana"]
#Output: ["apple", "banana", "kiwi"]


#solution 1
myList = ["apple", "banana", "apple", "kiwi", "banana"]
unique_list = list(dict.fromkeys(myList)) #new researched method 
#creates a new dictionary from the list provided with a specific order - no duplicates
print(unique_list)
#returns: ['apple', 'banana', 'kiwi'] - kept order but removed duplicates

#solution 2
myList2 = ["apple", "apple", "strawberry", "kiwi", "banana"]
unique_list2 = list(dict.fromkeys(myList2)) #new researched method 
print(unique_list2)
#returns: ['apple', 'strawberry', 'kiwi', 'banana']

#solution 3
myList3 = [1, 2, 4, 7, 7, 8, 7]
unique_list3 = list(dict.fromkeys(myList3)) #new researched method 
print(unique_list3)
#returns: [1, 2, 4, 7, 8]

#another variation (new researched way of approaching the problem with extra time)
myList = ["apple", "banana", "apple", "kiwi", "banana"]
seen = set() #temporary set 
unique_list = [x for x in myList if not (x in seen or seen.add(x))]
print(unique_list)
#returns: ['apple', 'banana', 'kiwi']

# MEMO: 
# For these timed problems, I picked one I thought I could handle under the time constraint. I understand in the real world that is not always the case, but for the first time I approached one I thought I could handle.
# I chose to approach the values as a list as they had an order that needed to be maintained no matter what changes or updates were made to it. At first, I thought of a linked list but they do not always maintain a specific indexed order - this scenario
# needed to maintain that. I approached it with a simple solution to ensure I could show the foundational skills that could be built on in more complex ways if I had more time in the future. The time limit did alter my flexibility to take a riskier or more complex
# approach to the problem, as then I would not have been able to come to a solution in 30 min. Under the pressure of needing to be done in 30 min, I did not go as in-depth as I would have hoped to, but still tried to show
# a basic understanding that could be explored if I had more time. 
# Fortunately, I did have a few minutes to try to push myself to research and understand a new method of returning a list in its original order wihout duplicates. I am still trying to fully wrap my head around the syntax, but I feel it could be useful with more complex cases.





# list - has a specific order






