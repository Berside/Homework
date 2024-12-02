#include <iostream>
#include "Header.h"
using namespace std;
int main()
{
    int a, b ,c;
    cout << "Enter first number:";
    cin >> a;
    cout << endl;
    cout << "Enter Second number:";
    cin >> b;
    cout << endl;

    cout << "Its time to Choose:" << endl << "1 - plus" << endl << "2 - minus" << endl << "3 - ymnoshenie" << endl << "4 - delenie" << endl;
    cin >> c; 
    if (c == 1) {
        int f = plus_(a, b);
        cout << f;
    }
    else if (c == 2) {
        int f = minus_(a, b);
        cout << f;
    }
    else if (c == 3) {
        int f = ymnoshenie(a, b);
        cout << f;
    }
    else if (c == 4) {
        int f = delenie(a, b);
        cout << f;
    }
    else {
        cout << "Fuck you";
    }
}
