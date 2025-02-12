#include <stdio.h>
#include <string>
using namespace std;

int main(){
    int i, c = 0, l, u, mid;
    int n = 5;
    int a[5] = {
        4,
        7,
        8,
        11,
        21
    };
    int m = 11;
    l = 0, u = n - 1;
    while (l <= u) {
        mid = (l + u) / 2;
        if (m == a[mid]) {
            c = 1;
            break;
        } else if (m < a[mid]) {
            u = mid - 1;
        } else
            l = mid + 1;
    }
    if (c == 0)
        printf("XX.");
    else
        printf("YY.");
    return 0;

}
