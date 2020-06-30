#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int ca, cx, cy, cz = 0;
    cin >> ca >> cx >> cy;
    if (cy % ca == 0 || cx >= ca || cx <= -ca)
    {
        cz = 0;
    }
    else if (cy - ca > 0)
    {
        int n = cy;
        cy = (cy - ca) % (2 * ca);
        n = 3 * (n - cy - ca) / 2 / ca;
        if (cy < ca && cx < (double)ca / 2 && cx > -(double)ca / 2)
        {
            cz = 1 + n + 1;
        }
        else if (cy > ca)
        {
            if (cx < 0 && cx > -ca)
            {
                cz = 2 + n + 1;
            }
            else if (cx > 0 && cx < ca)
            {
                cz = 3 + n + 1;
            }
        }
    }
    else
    {
        if (cx < (double)ca / 2 && cx > -(double)ca / 2)
        {
            cz = 1;
        }
    }

    if (cz < 1)
        cz = -1;
    cout << cz << endl;
    return 0;
}