#include <iostream>

// Namespace: provides a solution for preventing name conflicts
//            In large projects. Each entity needs a unique name
//            A namespace allows for identically named entities 
//            as long as the namespaces are different

namespace first {
    int x = 1;
}

namespace second {
    int x = 2;
}

int main() 
{
    /*
    using namespace std;

    Allows us to access standard library names without the std:: prefix
    (e.g., cout instead of std::cout).

    However, this may cause naming conflicts with variables or functions
    that share names with those in the std namespace.

    Best practice: Use std:: explicitly.
    */

    using namespace second; // Change "second" to "first" to see different value of x

    std::cout << first::x; // Even you're "using namespace second"
                            // You could still value in "first" namespace using "first::"" prefix

    return 0;
}