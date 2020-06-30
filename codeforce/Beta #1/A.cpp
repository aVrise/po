#include <bits/stdc++.h>
using namespace std;
int f(int x, int y)
{
    if (x % y == 0)
        return x / y;
    else
        return x / y + 1;
}

int main()
{
    // solution comes here
    int ca, cb, cc;
    cin >> ca >> cb >> cc;
    ca = f(ca, cc);
    cb = f(cb, cc);
    cout << (long long)ca * cb;
}