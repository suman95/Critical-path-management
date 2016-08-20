# Critical-path-management
A complete C++ code for Critical path Management i.e. for finding critical path, slack times etc.

# Usage
Compile with any C++ compiler (Recomendded C++ version 11)

# Inputs
Consider the following project plan <br />
[![scree_shot.png](https://s14.postimg.org/67phepoxt/scree_shot.png)](https://postimg.org/image/rhd3pk58d/) <br />
Input for above project plan will be as
```
Enter the number of tasks : 5

Enter task #1 : A
Enter duration for 1 : 20

Enter task #2 : B
Enter duration for 2 : 30

Enter task #3 : C
Enter duration for 3 : 40

Enter task #4 : D
Enter duration for 4 : 30

Enter task #5 : E
Enter duration for 5 : 10

Enter successors for task 1 : 2 3
Enter predecessors for task 1 : 0

Enter successors for task 2 : 4
Enter predecessors for task 2 : 1

Enter successors for task 3 : 4
Enter predecessors for task 3 : 1

Enter successors for task 4 : 5
Enter predecessors for task 4 : 2 3

Enter successors for task 5 : 6
Enter predecessors for task 5 : 4
```
# Results
A table containing all values for tasks along with the critical path.
