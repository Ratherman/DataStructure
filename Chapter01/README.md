## Answered Questions
* 01.26 (p. 27)
* 01.29 (p. 28)

## 01.26 College Bookstore
Your college bookstore has hired you as a summer intern to design a new textbook inventory system. It is to include the following major processes:

- Ordering Textbooks
- Receiving Textbooks
- Determining Retail Price
- Pricing Used Textbooks
- Determining Quantity on Hand
- Recording Textbook Sales
- Recording Textbook Returns

## 01.29 Frequency Histogram
Write a program that builds a frequency array for data values in the range 1 to 20 and then prints their histogram. The data are to read from a file. The design for the program is shown in the following figure. 

Each of the subalgorithms is described below.

- The **getData** algorithm reads the file and store the data in an array.
- The **printData** algorithm prints the data in the array.
- The **makeFrequency** algorithm examines the data in the array, one element at a time, and adds 1 to the corresponding element in a frequency array based on the data value.
- The **makeHistogram** algorithm prints out a vertical histogram using asterisks for each occurrence of an element. For example, if there were five value 1s and eight value 2s in the data, it would print

    ```
    1: *****
    2: ********
    ```