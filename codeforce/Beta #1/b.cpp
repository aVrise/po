#include <bits/stdc++.h>
using namespace std;

int f(const string& fa, const int& fd)
{
    auto fi = fa.crbegin();
    int fb = 0, fc = 1;
    if (fd == 10)
    {
        while (fi != fa.crend())
        {
            fb += (*fi - '0') * fc;
            fc *= fd;
            fi++;
        }
    }
    else
    {
        while (fi != fa.crend())
        {
            fb += (*fi - 'A' + 1) * fc;
            fc *= fd;
            fi++;
        }
    }
    return fb;
}

void g(int ga)
{
    stack<char> gs;
    int gb;
    while (ga != 0)
    {
        gb = (ga - 1) % 26;
        ga = (ga - 1) / 26;
        gs.push((char) ('A' + gb));
    }
    while(!gs.empty())
    {
        cout << gs.top();
        gs.pop();
    }
}

int main()
{
    // solution comes here
    int n;
    cin >> n;
    while(n--)
    {
        string ca;
        int cf = 0;
        vector<string> cv;
        cin >> ca;
        auto ci = ca.begin();
        stringstream cs;
        while (ci != ca.end())
        {   
            cs.str("");
            if (*ci >= 'A')
            {
                while (*ci >= 'A')
                {
                    cs << *ci;
                    ci++;
                }
            }
            else
                {
                while (*ci < 'A' && ci != ca.end())
                {
                    cs << *ci;
                    ci++;
                }
            }
            cv.push_back(cs.str());
        }
        if (cv.size() == 4)
        {
            g(f(cv[3], 10));
            cout << cv[1] << endl;
        }
        else
        {
            cout << "R" << cv[1] << "C" << f(cv[0], 26) << endl;
        }
    }
    return 0;
}