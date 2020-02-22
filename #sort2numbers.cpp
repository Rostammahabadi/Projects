// This program asks the user to input 2 numbers then sorts them in ascending order
// then it will print the sum of all numbers as well as the average

#include <iostream>
#include <stdlib.h>

using namespace std;
int main(int, char**) {
    int n,m,z,sort1,sort2,sum1,sum2,sum3;
    n=0;
    double sum=0;
    while (n<3) {
        cout << " enter two integers (n n): ";
    cin >> m;
    cin >> z;
    if (m>z){
        sort1 = z;
        sort2 = m;
    }
    else{
        sort1 = m;
        sort2 = z;
    }
    cout << " Sorted is " << sort1 << " " << sort2 << endl;
    ++n;
    sum += m + z;
    }
    cout << " sum of all numbers entered: " << sum << endl;
    cout << " average of the numbers entered: " << sum/6 << endl;
    
}