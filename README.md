# Pyramid_Structure_Sum_Paths

## This Python code will receive a pyramid structure or numbers as input and return the sums of all the valids paths.


Input example:
```
      12
      
    45  96
    
  42  32  14
  
52  64  63  19

```
A valid path will take one number from each row, moving only one at the right or at the left.
For example:
```
      **12**
      
    **45**  96
    
  42  **32**  14
  
52  **64**  63  19
```
With sum: 12 + 45 + 32 +64

Or:
```
      **12**
      
    45  **96**
    
  42  **32**  14
  
52  **64**  63  19
```
With sum: 12 + 96 + 32 + 64

Note that the number of levels can vary from input to input.





## The second part of this code will return all the sums with the number of times it appears,
## sorted according to count.


For example:

 Sum  |  Count
 
 165  |   3
 
 206  |   1
