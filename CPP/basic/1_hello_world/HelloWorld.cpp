#include <iostream>

using namespace std;

int main()
{

    // This is a comment

    /*
    Multi-line comment
    */

    std::cout << "Hello World!" << std::endl; //Requires iostream | Also flushes output buffer after each line -> Slower  
    std::cout << "This is my first C++ program!" << endl ;
    std::cout << "It's great to learn C++!" << '\n'; //Faster performance -> Should you most cases
    return 0; //Must be at the end of the program to indicate that the program has ended successfully
}