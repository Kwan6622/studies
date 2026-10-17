#include <iostream>

// Type conversion: convert a value of one data type to another
//                  Implicit = automatic
//                  Explicit = precede value w/ new data type (int)

int main()
{
    // int x = 3.14; 
    // -> This returns "3"
    // The program will automatically truncate to fit the data type
    
    // double x = (int) 3.14; 
    // int x = (double) 2;
    // -> These are also a way to convert
    
    // char x = 100;
    // This returns "d"

    // std::cout << (char) 101; 
    // This returns "e"
    // They will return the corresponding CHARACTER in the ASCII table

    int correct = 8;
    int question = 10;
    
    double score = static_cast<double>(correct) / question * 100;
    // You have to convert one of the two var here to DOUBLE
    // Because C++ is doing integer divison -> Returns integer (0 instead of 0.8)
    // -> 0 * 100 = 0

    // (double) correct | works, C syntax 
    // static_cast<double>(correct) | best practice for modern C++

    std::cout << score << "%";

    return 0;
}