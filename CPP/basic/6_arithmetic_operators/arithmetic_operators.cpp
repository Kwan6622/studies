#include <iostream>

// arithmetic operators: return result of a specific
//                      arithmetic operators (+ - * /)

int main() 
{
    int students = 30; 

    // students = students + 1 | long version | add 1 
    // students += 3; | short version | add 3 
    // students++; | add 1 - often seen in loops 

    // students = students - 5; | substract by 5
    // students -= 3; | substract by 3
    // students --; | substract by 1

    // students = students * 4; | multiply by 4
    // students *= 8; | multiply by 8

    // students = students / 2; | divide by 2 
    // students /= 3; | divide by 3

    int remainder = students % 2; // Modulo operator: Find the remainder of a division

    std::cout << students << "\n"; 
    std::cout << remainder;

    // Operation order: Parentheses
    //                  Multiplication / Division
    //                  Addition / Substraction
    //                  Left to Right 

    return 0;
}