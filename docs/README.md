# HeavyLifter Manual

## Introduction

I've designed my HeavyLifter in order to do the heavy lifting for us. 

Enjoy!

## Technical info

The robot has to be fed an *instruction set file* containing the starting state as a pictogram followed by the instructions to be carried out in order (see example below).

* The starting state diagram should be compiled using the following rules:
    * boxes are to be represented by following the pattern: `|%|`, where `%` should be replaced by a capital letter of the English alphabet
    * there shall be no more boxes then letters available, and each box should be uniquely identified by its label
    * boxes should be separated horizontally by a single space
    * there can be no more than 10 stacks, each of which should be identified by a number centered below them
    * the text "bottom" should be placed below the stacks, indicating in which direction the ground is located
* movement instructions should be expressed following the pattern: `move #1 from #2 to #3`, where `#1` indicates the number of boxes to move between stacks `#2` and `#3`.
* model v1 can only move one box at a time, but I've already ordered v2, which doesn't have this limitation

## Example

In this example, the robotic arm will move boxes arranged in 4 stacks following the set of instructions given below the starting state:

    |K|            
    |A| |Q|     |F|
    |P| |U| |B| |T|
     1   2   3   4
         bottom

    move 1 from 3 to 4
    move 2 from 1 to 3
    move 1 from 1 to 2
    move 2 from 4 to 1

After all instructions have been carried out, the boxes lie in the following state:

* when using the HeavyLifter v1

            |P|     
        |F| |Q| |A|    
        |B| |U| |K| |T|
         1   2   3   4
            bottom

* when using the HeavyLifter v2

            |P|     
        |B| |Q| |K|    
        |F| |U| |A| |T|
         1   2   3   4
            bottom
