Array
-----

## Introduction to Array

**What is an array?**

> An Array is a collection of items. The items could be integers, strings, DVDs, games, books—anything really. The items are stored in neighboring (contiguous) memory locations. Because they're stored together, checking through the entire collection of items is straightforward.

**Creating an array**

*In Java*
```
// The actual code for creating an Array to hold DVD's.
DVD[] dvdCollection = new DVD[15];

// A simple definition for a DVD.
public class DVD {
    public String name;
    public int releaseYear;
    public String director;

    public DVD(String name, String releaseYear, String director) {
        this.name = name;
        this.releaseYear = releaseYear;
        this.director = director;
    }

    public String toString() {
        System.out.println(
            this.name + ", directed by " + this.director + ", released in " + this.releaseYear));
    }
}
```

**Accessing elements in the array**

> The two most primitive Array operations are writing elements into them, and reading elements from them. All other Array operations are built on top of these two primitive operations.

**Indexes** - each of the places is identified using a number in the range of 0 to N - 1

**Writing items in the array**

*In Java*
```
// Firstly, we need to actually create a DVD object for The Avengers.
DVD avengersDVD = new DVD("The Avengers", 2012, "Joss Whedon");

// Next, we'll put it into the 8th place of the Array. Remember, because we
// started numbering from 0, the index we want is 7.
dvdCollection[7] = avengersDVD;

DVD incrediblesDVD = new DVD("The Incredibles", 2004, "Brad Bird");
DVD findingDoryDVD = new DVD("Finding Dory", 2016, "Andrew Stanton");
DVD lionKingDVD = new DVD("The Lion King", 2019, "Jon Favreau");

// Put "The Incredibles" into the 4th place: index 3.
dvdCollection[3] = incrediblesDVD;

// Put "Finding Dory" into the 10th place: index 9.
dvdCollection[9] = findingDoryDVD;

// Put "The Lion King" into the 3rd place: index 2.
dvdCollection[2] = lionKingDVD;

DVD starWarsDVD = new DVD("Star Wars", 1977, "George Lucas");
dvdCollection[3] = starWarsDVD;
```

> Because we just put Star Wars into the Array at index 3, The Incredibles is no longer in the Array. It has been overwritten! If we still have the incrediblesDVD variable in scope, then the DVD still exists in the computer's memory. If not though, it's totally gone!

**Reading items from array**

*In Java*
```
// Print out what's in indexes 7, 10, and 3.
System.out.println(dvdCollection[7]);
System.out.println(dvdCollection[10]);
System.out.println(dvdCollection[3]);

// Will print:

// The Avengers, directed by Joss Whedon, released in 2012
// null
// Star Wars, directed by George Lucas, released in 1977
```

> Notice that because we haven't yet put anything at index 10, the value it contains is null. In other languages, such as C, the Array slot could contain completely random data.

**Writing items into an array with a loop**

*In Java*
```
int[] squareNumbers = new int[10];

// Go through each of the Array indexes, from 0 to 9.
for (int i = 0; i < 10; i++) {
    // We need to be careful with the 0-indexing. The next square number
    // is given by (i + 1) * (i + 1).
    // Calculate it and insert it into the Array at index i.
    int square = (i + 1) * (i + 1);
    squareNumbers[i] = square;
}
```

**Reading items from an array with a loop**

*In Java*
```
// Go through each of the Array indexes, from 0 to 9.
for (int i = 0; i < 10; i++) {
    // Access and print what's at the i'th index.
    System.out.println(squareNumbers[i]);
}

// Will print:
// 1
// 4
// 9
// 16
// 25
// 36
// 49
// 64
// 81
// 100
```

> One last thing worth knowing now is that there's a more elegant way of printing out the values of an Array—a variant of the for loop, commonly referred to as a "for each" loop.

**Array capacity vs length**

> If somebody asks you how long the DVD Array is, what what would your answer be?

There are two different answers you might have given.

1. The number of DVDs the box could hold, if it was full, or

2. The number of DVDs currently in the box.

Both answers are correct, and both have very different meanings! It's important to understand the difference between them, and use them correctly. We call the first one the **capacity** of the Array, and the second one the **length** of the Array.

**Array capacity**

Let's say we've created a new Array like this.

`DVD[] array = new DVD[6]`

When we created the Array, we specified that it can hold up to 6 DVD's. This is the Array's **capacity**.
The Array's capacity must be decided when the Array is created. The capacity cannot be changed later. 

The capacity of an Array in Java can be checked by looking at the value of its `length` attribute. This is done using the code `arr.length`, where arr is the name of the Array. Different programming languages have different ways of checking the length of an Array.

```
int capacity = array.length;
System.out.println("The Array has a capacity of " + capacity);
```

Running this code will give the following output:

>The Array has a capacity of 6

**Array length**

The other definition of **length** is the number of DVDs, or other items, currently in the Array. This is something you'll need to keep track of yourself, and you won't get any errors if you overwrite an existing DVD, or if you leave a gap in the Array.

*In Java*
```
// Create a new array with a capacity of 10.
int[] array = new int[6];

// Current length is 0, because it has 0 elements.
int length = 0;

// Add 6 items into it.
for (int i = 0; i < 3; i++) {
    array[i] = i * i;
    // Each time we add an element, the length goes up by one.
    length++;
}

System.out.println("The Array has a capacity of " + array.length);
System.out.println("The Array has a length of " + length);
```

Running this code will give the following output:

>The Array has a capacity of 6
>The Array has a length of 3

**Handling array parameters**

Most Array questions on LeetCode have an Array passed in as a parameter, with no "length" or "capacity" parameter. What do we mean by this? Well, let's look at an example. Here is the description for the first problem you'll be asked to solve.

>Given a binary array, find the maximum number of consecutive 1s in this array.

And here is the code template you're given.
```
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        // Hint: Initialise and declare a variable here to 
        // keep track of how many 1's you've seen in a row.
        for (int i = 0; i < nums.length; i++) {
            // Do something with element nums[i].
        }
    }
}
```

The only parameter is nums; an Array. You couldn't possibly solve this question without knowing how long nums is. Well, luckily it's straightforward. When an Array is given as a parameter, without any additional information, you can safely assume that **length == capacity**. That is, the Array is the exact right size to hold all of it's data. We can, therefore, use .length.

Inserting Items into an Array
-----------------------------

> An array is a data structure, which means that it stores data in a specific format and supports certain operations on the data it stores.

**Array Insertions**

Inserting a new element into an Array can take many forms:

1. Inserting a new element at the end of the Array

2. Inserting a new element at the beginning of the Array

3. Inserting a new element at any given index inside the Array

**Inserting at the end of an Array**

All we need to do for inserting an element at the end is to assign the new element to one index past the current last element.

*In Java*
```
// Declare an integer array of 6 elements
int intArray = new int[6];
int length = 0;

// Add 3 elements to the Array
for (int i = 0; i < 3; i++) {
    intArray[length] = i;
    length++;
}

// Define a function, printArray, to help visualize what is happening
for (int i = 0; i < intArray.length; i++) {
    System.out.println("Index " + i + " contains " + intArray[i]);
}
```

If we run the `printArray` function, we'll get the following output

```
Index 0 contains 0.
Index 1 contains 1.
Index 2 contains 2.
Index 3 contains 0.
Index 4 contains 0.
Index 5 contains 0.
```

Index 3, 4, and 5 all contain 0 because Java filles unused `int` Array slots with 0.

```
// Insert a new element at the end of the Array. Again,
// it's important to ensure that there is enough space
// in the array for inserting a new element.
intArray[length] = 10;
length++;
```

Notice how we also incremented the length? This is very important, next time when we add another element, we'll accidentally overwrite the one we just added!

Running `printArray` again, we'll get the following output:

```
Index 0 contains 0.
Index 1 contains 1.
Index 2 contains 2.
Index 3 contains 10.
Index 4 contains 0.
Index 5 contains 0.
```

**Inserting at the start of an Array**

To insert an element at the start of an Array, we'll need to shift all other elements in the Array to the right by one index to create space for the new element.

The time taken for insertion at the beginning of an Array will be proportional to the length of the Array. In terms of time complexity analysis, this is a linear time complexity: O(N), where N is the length of the Array.

*In Java*
```
// First, we will have to create space for a new element.
// We do that by shifting each element one index to the right.
// This will firstly move the element at index 3, then 2, then 1, then finally 0.
// We need to go backwards to avoid overwriting any elements.
for (int i = 3; i >= 0; i--) {
    intArray[i + 1] = intArray[i];
}

// Now that we have created space for the new element,
// we can insert it at the beginning.
intArray[0] = 20;
```

Running `printArray` will give an output of

```
Index 0 contains 20.
Index 1 contains 0.
Index 2 contains 1.
Index 3 contains 2.
Index 4 contains 10.
Index 5 contains 0.
```

**Inserting anywhere in the Array**

Similarly, for inserting at any given index, we first need to shift all the elements from that index onwards one position to the right.

Insertion at the beginning is basically a special case of inserting an element at a given index—in that case, the given index was 0.

*In Java*
```
// Say we want to insert the element at index 2.
// First, we will have to create space for the new element.
for (int i = 4; i >= 2; i--)
{
    // Shift each element one position to the right.
    intArray[i + 1] = intArray[i];
}

// Now that we have created space for the new element,
// we can insert it at the required index.
intArray[2] = 30;
```

Running `printArray` will give an output of

```
Index 0 contains 20.
Index 1 contains 0.
Index 2 contains 30.
Index 3 contains 1.
Index 4 contains 2.
Index 5 contains 10.
```

The main thing to be careful of is remembering that `array.length` gives you the total capacity of the Array

If you want to know the last used slot, you'll need to keep track of this yourself using a `length` variable.

Deleting Items from an Array
----------------------------

Deletion in an Array works in a very similar manner to insertion, and has the same three different cases:

1. Deleting the last element of the Array.

2. Deleting the first element of the Array.

3. Deletion at any given index.

**Deleting from the end of an array**

> Deletionat the end of an Array is similar to people standing in a line, also known as a *queue*.

The person who most recently joined the queue can leave at any time without disturbing the rest of the queue.

Deleting at the end of an Array is the least time consuming of the three cases.

*In Java*
```
// Declare an integer array of 10 elements.
int[] intArray = new int[10];

// The array currently contains 0 elements
int length = 0;

// Add elements at the first 6 indexes of the Array.
for(int i = 0; i < 6; i++) {
    intArray[length] = i;
    length++;
}

// Deletion from the end is as simple as reducing the length
// of the array by 1.
length--;

for (int i = 0; i < intArray.length; i++) {
    System.out.println("Index " + i + " contains " + intArray[i]);
}
```

We'll get the following result,
```
Index 0 contains 0.
Index 1 contains 1.
Index 2 contains 2.
Index 3 contains 0.
Index 4 contains 0.
Index 5 contains 0.
Index 6 contains 0.
Index 7 contains 0.
Index 8 contains 0.
Index 9 contains 0.
```

What's gone wrong? Well, remember how there's two different definitions of length? When we use `intArray.length`, we're looking every valid index of the Array. When in fact, we only want to look at the ones that we've put values into. The fix is easy, we just iterate up to our own `length` variable instead.

*Java*
```
for (int i = 0; i < length; i++) {
    System.out.println("Index " + i + " contains " + intArray[i]);
}
```

Run this, and you'll get the following before the deletion:

```
Index 0 contains 0.
Index 1 contains 1.
Index 2 contains 2.
Index 3 contains 3.
Index 4 contains 4.
Index 5 contains 5.
```

And the following after:

```
Index 0 contains 0.
Index 1 contains 1.
Index 2 contains 2.
Index 3 contains 3.
Index 4 contains 4.
```

**Deleting from the start of an Array**

If we want to delete the first element of the Array, that will create a vacant spot at the 0th index. To fill that spot, we will shift the element at index 1 one step to the left. Going by the ripple effect, every element all the way to the last one will be shifted one place to the left. This shift of elements takes O(N)O(N) time, where NN is the number of elements in the Array.

*Java*
```
// Starting at index 1, we shift each element one position
// to the left.
for (int i = 1; i < length; i++) {
    // Shift each element one position to the left
    int_array[i - 1] = int_array[i];
}

// Note that it's important to reduce the length of the array by 1.
// Otherwise, we'll lose consistency of the size. This length
// variable is the only thing controlling where new elements might
// get added.
length--;
```

Starting from index `0`, we'll move every element one position to its left, effectively "deleting" the element at index `0`. We also need to reduce `length` by `1` so that the next new element is inserted in the correct position.

And here's the output we'll get, with our updated `printArray` function.

```
Index 0 contains 1.
Index 1 contains 2.
Index 2 contains 3.
Index 3 contains 4.
```

**Deleting from anywhere in the Array**

For deletion at any given index, the empty space created by the deleted item will need to be filled. Each of the elements to the right of the index we're deleting at will get shifted to the left by one.

This shift of elements takes O(K)O(K) time where KK is the number of elements to the right of the given index. Since potentially K = NK=N, we say that the time complexity of this operation is also O(N).

*Java*
```
// Say we want to delete the element at index 1
for (int i = 2; i < length; i++) {
    // Shift each element one position to the left
    int_array[i - 1] = int_array[i];
}

// Again, the length needs to be consistent with the current
// state of the array.
length--;
```

Here is the output from the `printArray` function.
```
Index 0 contains 1.
Index 1 contains 3.
Index 2 contains 4.
```
