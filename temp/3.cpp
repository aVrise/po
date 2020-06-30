#include <bits/stdc++.h>
using namespace std;

int f(queue<int> &fa, queue<int> &fb, queue<int> &fc)
{
    if (!fa.empty() && !fb.empty() && !fc.empty())
    {
        int fz = 1000000001;
        fz = (!fa.empty() && fz > fa.front()) ? fa.front() : fz;
        fz = (!fb.empty() && fz > fb.front()) ? fb.front() : fz;
        fz = (!fb.empty() && fz > fc.front()) ? fb.front() : fz;
        if (fz == fa.front())
        {
            fa.pop();
        }
        else
        {
            if (fz == fb.front())
            {
                fb.pop();
            }
            else
            {
                fc.pop();
            }
        }
        return fz;
    }
    else
    {
        return -1;
    }
}

int main()
{
    // solution comes here
    int n,i;
    cin >> n;
    map<int, int> cm;
    queue<int> q1, q2, q3, q4, q6, q9;
    int a1[n][2], a2[n], a3[n];
    for (int j = 0; j < n; j++)
    {
        cin >> a1[j][0];
        a1[j][1] = j;
    }
    for (int j = 0; j < n; j++)
    {
        cin >> a2[j];
    }
    for (int j = 0; j < n; j++)
    {
        cin >> a3[j];
    }
    sort(a1, a1 + n);
    for (int j = 0; j < n; j++)
    {
        switch (a2[a1[j][1]] * a3[a1[j][1]])
        {
        case 1:
            q1.push(a1[j][0]);
            break;
        case 2:
            q2.push(a1[j][0]);
            break;
        case 3:
            q3.push(a1[j][0]);
            break;
        case 4:
            q4.push(a1[j][0]);
            break;
        case 6:
            q6.push(a1[j][0]);
            break;
        case 9:
            q9.push(a1[j][0]);
            break;
        }
    }
    cin >> n;
    for (int j = 0; j < n; j++)
    {
        cin >> i;
        switch (i)
        {
        case 1:
            cout << f(q1, q2, q3);
            break;
        case 2:
            cout << f(q2, q4, q6);
            break;
        case 3:
            cout << f(q3, q6, q9);
            break;
        }
    }

    return 0;
}