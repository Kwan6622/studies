#include <iostream>

int main()
{
    // integer - Whole number
    int age = 21;
    int days = 7;
    int year = 2026;
    std::cout << year;

    // double - equals to float in Python | number including decimal
    double gpa = 2.8;
    double fee = 9.99;
    double score = 8.3;
    double temperature = 32.7;
    std::cout << temperature;

    // char - single character | It'll return a warning if it stores more than 1 character
    // Use '' to represent single character
    char Grade = 'F';
    char initial = 'D';
    char currency = '$';
    std::cout << currency;

    //boolean - true or false | 1 or 0
    bool student = true;
    bool absent = false;
    bool power = true;
    std::cout << student;

    // string - a sequence of text 
    // use "" to represent a string
    std::string name = "Quang";
    std::string country = "Vietnam";
    std::string food = "Sushi";

    std::cout << "Hello, I'm " << name << "!\n";
    std::cout << "I'm from " << country << ".\n";
    std::cout << "My favorite food is " << food << ".\n";

    return 0;
}