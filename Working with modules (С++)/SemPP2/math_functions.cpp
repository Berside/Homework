#include "Header.h"
int plus_(int a, int b) {
    return a + b;
}

int minus_(int a, int b) {
    return a - b;
}

int ymnoshenie(int a, int b) {
    return a * b;
}

int delenie(int a, int b) {
    if (b != 0) {
        return a / b;
    }
    else {
        return 0;
    }
}