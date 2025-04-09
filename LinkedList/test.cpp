#include <iostream>
using namespace std;

void someFunc(int* ptr, int*& ptr2){
    cout << "value" << ptr << " .  heloo\n";
    cout << "reference" << ptr2 << "  dd";
}


int main(){
    int* ptr;
    int x = 10;
    ptr = &x;
    someFunc(ptr, ptr);

// }