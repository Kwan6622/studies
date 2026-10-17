#include <iostream>
#include <cmath>

int main()
{
    double x = 7;
    double y = 10;
    double z;

    z = std::max(x, y); 
    std::cout << z << "\n";

    z = std::min(x, y);
    std::cout << z << "\n";

    // Comes with 'cmath' library
    z = pow(2, 4); // A to the power of B
    std::cout << z << "\n";

    z = sqrt(9); // square root 
    std::cout << z << "\n";

    z = abs(-100); // absolute value
    std::cout << z << "\n";

    z = round(3.14); // automatically round a value
    std::cout << z << "\n";

    z = ceil(6.1); // round up a value
    std::cout << z << "\n";

    z = floor(10.99); // round down a value
    std::cout << z;

    return 0;
}