#include <iostream>
// #include <vector>

// typedef: reserved keyword used to create an additional name
//          (alias) for another data type.
//          New identifier for an existing type
//          Helps w/ readability & reduces typos
//          Use when there is a clear benefit
//          Replaced w/ 'using' (work better w/ templates)

// typedef std::vector<std::pair<std::string, int>> pairlist_t;
// typedef std::string text_t;
// typedef int number_t;

using text_t = std::string;
using number_t = int; 

int main() 
{
    // pairlist_t pairlist

    text_t firstName = "Quang";
    number_t age = 21;

    std::cout << firstName << "\n";
    std::cout << age << "\n";

    return 0;
}