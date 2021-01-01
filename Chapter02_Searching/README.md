## Answered Questions
* 02.01 Binary Search (p. 74) [Goolge Colab Link](https://colab.research.google.com/drive/14HjZrOsVxRSOGL-5E07nKj962wYvrt2D?authuser=2#scrollTo=mIERoTTo-XCO)
* 02.03 Collision Resolution (p. 28) [Goolge Colab Link](https://colab.research.google.com/drive/1b9fzvSJSRaZ3-9BUg78NPPVZMkSq5g26?authuser=2#scrollTo=iPe4w_TTGKZk)

## 02.01 Binary Search
* An array contains the elements show below. Using the binary search algorithm, trace the steps followed to find 88. At each loop iteration, including the last, show the contents of **first**, **last**, and **mid**.
* And use the same procedure to find 20. **(It can't be found.)**

```
8 13 17 26 44 56 88 97
```

## 02.03 Collision Resolution
- Using the **modulo-division** method and **linear probing**, store the keys shown below in an array with 19 elements. How many collisions occurred? What is the density of the list after all keys have been inserted?
- Using a **linked list** method for collisions.
- Using the **digit-extraction** method (first, third, and fifth digits) and **quadratic probing**
- Using **mid-square** method, with the center two digits, for hashing. Use **pseudorandom number** generator for rehashing if a collision occurs. Use a=3 and c=-1 as the factors.
- Using **key-offset** method for collisions.
- Using the **fold shift** method for collisions and folding two digits at a time and then **modulo division** of the folded sum.
- Using the **fold boundary** method.
- Using the **rotation method** for hashing. First rotate the rightmost digits two to the left and then use **digit extraction** (first, third, and fifth digits). Use the **linear probe** method to resolve collisions.
- Using a **key-offset** method for collisions.