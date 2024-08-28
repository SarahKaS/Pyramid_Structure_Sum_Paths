# Pyramid_Structure_Sum_Paths
This Python code will receive a pyramid structure or numbers as input and return the sums of all the valids paths.


Input example:<sub>
      12<sub>
    45  96<sub>
  42  32  14<sub>
52  64  63  19<sub>

A valid path will take one number from each row, moving only one at the right or at the left.
For example:<sub>
      **12**<sub>
    **45**  96<sub>
  42  **32**  14<sub>
52  **64**  63  19<sub>
With sum: 12 + 45 + 32 +64<sub>

Or:<sub>
      **12**<sub>
    45  **96**<sub>
  42  **32**  14<sub>
52  **64**  63  19<sub>
With sum: 12 + 96 + 32 + 64<sub>

Note that the number of levels can vary from input to input.



The second part of this code will return all the sums with the number of times it appears,
sorted according to count.
<sub>
For example:<sub>
 Sum  |  Count<sub>
 165  |   3<sub>
 206  |   1<sub>
