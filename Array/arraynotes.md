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
