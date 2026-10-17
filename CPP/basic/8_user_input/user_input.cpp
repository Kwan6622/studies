#include <iostream>
#include <string>

// cout << : Stream insertion operator (output)
// cin >>  : Stream extraction operator (input)

int main()
{
    std::string name;
    int age;

    std::cout << "How old are you?: ";
    std::cin >> age;

    /*
        std::cin >> age reads the integer but leaves the
        newline character ('\n') in the input buffer.

        If std::getline() is called immediately afterward,
        it consumes that leftover newline and returns
        an empty string.

        std::ws discards leading whitespace, including
        spaces, tabs, and newline characters.
    */

    std::cout << "What's your full name?: ";
    std::getline(std::cin >> std::ws, name);

    /*
        The >> operator normally reads input until
        it encounters whitespace.

        std::getline() reads an entire line, including
        spaces, until it encounters a newline character.
    */

    std::cout << "Hello, " << name << "!\n";
    std::cout << "You are " << age << " years old!\n";

    return 0;
}