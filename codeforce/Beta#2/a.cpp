#include <bits/stdc++.h>
using namespace std;

typedef pair<string, int> PAIR;

bool cmp_val(const PAIR &left, const PAIR &right)
{
    return left.second > right.second;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    set<string> cs;
    vector<PAIR> cv, cv1;
    map<string, int> cm;
    int cn, cb, cf = 0;
    string ca;
    cin >> cn;
    for (int ci = 0; ci < cn; ci++)
    {
        cin >> ca >> cb;
        cv1.push_back(make_pair(ca, cb));
        // cout << ca << cb << endl;

        for (auto cit = cv.begin(); cit != cv.end(); ++cit)
        {
            cf = 0;
            if (cit->first == ca)
            {
                cit->second += cb;
                cf = 1;
                break;
            }
        }

        if (cv.empty() || cf == 0)
        {
            cv.push_back(make_pair(ca, cb));
        }
        sort(cv.begin(), cv.end(), cmp_val);
        // for (auto x : cv)
        // {
        //     cout << x.first << ' ' << x.second << ' ';
        // }
        // cout << endl
        //      << endl;
    }
    int cmax = cv[0].second;
    for (auto cit = cv.begin(); cit->second == cmax; ++cit)
    {
        cs.insert(cit->first);
    }
    for (PAIR ci : cv1)
    {
        if (cs.count(ci.first))
        {
            if (cm.count(ci.first))
            {
                cm[ci.first] += ci.second;
            }
            else
            {
                cm[ci.first] = ci.second;
            }
            if (cm[ci.first] >= cmax)
            {
                cout << ci.first << endl;
                break;
            }
        }
    }
    return 0;
}