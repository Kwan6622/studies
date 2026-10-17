#include <iostream>

int main()
{
    char op;
    double num1;
    double num2;
    double result;

    std::cout << "******************** CALCULATOR ********************\n";

    std::cout << "Enter an operator (+ - * /): ";
    std::cin >> op;

    if (op != '+' && op != '-' && op != '*' && op != '/')
    {
        std::cout << "Invalid operator!\n";
        return 1;
    }

    std::cout << "Enter #1: ";
    if (!(std::cin >> num1)) {
        std::cout << "Invalid number!\n";
        return 1;
    }

    std::cout << "Enter #2: ";
    if (!(std::cin >> num2)) {
        std::cout << "Invalid number!\n";
        return 1;
    }

    switch(op){
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            if (num2 == 0){
                std::cout << "Cannot divide by zero!\n"; 
                return 1;
            }
            result = num1 / num2;
            break;
    }

    std::cout << "Result: " << result << "\n";

    std::cout << "****************************************************";

    return 0;
}