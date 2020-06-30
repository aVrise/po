#include <bits/stdc++.h>
using namespace std;

int f(int a)
{
    return a < 0 ? 0 : a;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int cn, cR, cr;
    const double pi = 3.1415926;
    const double eps = 1e-3;
    cin >> cn >> cR >> cr;
    double ca = (1.0 * cn * pi + f(cn - 2) * (1.732 - 0.5 * pi)) * cr * cr + f(pi * cR * cR - pi * (cR - cr) * (cR - cr) - (pi * (cR - cr) / cr) * (pi - acos(cr / cR)) * cr * cr);
    if (cn == 1)
    {
        ca = 1.0 * cn * pi * cr * cr;
    }
    if (ca - pi * cR * cR > eps)
    {
        cout << "NO" << endl;
    }
    else
    {
        cout << "YES" << endl;
    }
    return 0;
}