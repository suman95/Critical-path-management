# Critical-path-management
A complete C++ code for Critical path Management i.e. for finding critical path, slack times etc.

# Usage
Compile with any C++ compiler (Recomendded C++ version 11)

## Inputs
Consider the following project plan <br />
[![scree_shot.png](https://s19.postimg.org/a1o4pjaqb/scree_shot.png)](https://postimg.org/image/l19c1515b/) <br />
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

Enter successors for task Start : 1

Enter successors for task A : 2 3

Enter successors for task B : 4

Enter successors for task C : 4

Enter successors for task D : 5

Enter successors for task E : 6
```
# Results
A table containing all values for tasks along with the critical path.<br />
*Note : The Program includes dummy Start and Finish Activities with duration 0 for ease.* 
[![scree2.png](https://s19.postimg.org/vzkljbpqr/scree2.png)](https://postimg.org/image/3zghz1ma7/)
