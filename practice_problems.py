"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""
product_ids = [1, 2, 3, 4, 5, 6, 7, 1]
print(product_ids)

def has_duplicates(product_ids):
    return len(product_ids) != len(set(product_ids)) #creates a unique set and compares list lengths to identify counts and possible duplicates
print(has_duplicates) #returns there are duplicates 

# I chose a straightforward list and set implementation for this problem as there were not specific orders that needed to be maintained, 
# but the set allowed me to compare the original list to the unique values I was searching for duplicates within. I feel like this was the most straightforward approach to identifying duplicates, 
# and found it made the most sense after reviewing the weekly resources as well. I had to research new syntax as I wanted it to work to identify any duplicates, not just a specific id I would ask it to look for. 

"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue: #implementing tasks as strings not nodes as used in previous class work
    def __init__(self):
        self.tasks = [] 

    def add_task(self, task):
        self.tasks.append(task) #adds a task

    def remove_oldest_task(self):
        if not self.tasks:
            return None 
        return self.tasks.pop(0) #pops the task from the queue
    
# I used a queue in this example as you want to approach tasks in the order they come in. If someone is the first in, they need to be the first out. 
# I also did not use the node approach to the queue, and rather researched more about using strings as the 'tasks' at hand. 
# Using this approach, it should be easy to add tasks and remove / pop old or finished tasks hypothetically. 

"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""
stream = [1, 1, 2, 3, 4, 4, 5, 6, 7]

class UniqueTracker:
    def __init__(self):
        self.tracker = set() #creates the instance

    def add(self, value):
        self.tracker.add(value) #adds a value

    def get_unique_count(self):
        return len(self.tracker) #returns the unique count
     
# I used a set for this example as it discounts duplicates, and will allow me to create a set of integers 
# where I can do a unique count of the values. Sets are built to be efficient at checking values, so I felt this was the best option.
# I did initially think of a linked list, but it seemed they were not as efficient for checking values when reviewing each use in the weekly resources. 

