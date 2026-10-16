#include <iostream>

// The const keyword specifies that a variable's value is constant
// Tells the compiler to prevent anyone from modifying it 
// (read-only)

int main() 
{
    const double PI = 3.14159; // Naming covention: write the variable in ALL CAPS
    double radius = 10;
    double circumference = 2 * PI * radius;

    std::cout << circumference << " cm"; 

    return 0;
}