#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    string ct1;
    multiset<char> cms1, cms2;
    set<char> cs;
    cin >> ct1;
    for (auto x : ct1)
    {
        cms1.insert(x);
        cs.insert(x);
    }
    cin >> ct1;
    for (auto x : ct1)
    {
        cms1.insert(x);
        cs.insert(x);
    }
    cin >> ct1;
    for (auto x : ct1)
    {
        cms2.insert(x);
    }
    for (auto x : cs)
    {
        if (cms1.count(x) != cms2.count(x))
        {
            cout << "NO" << endl;
            return 0;
        }
        else
            cms2.erase(x);
    }
    // for (auto x = cms2.begin() ; x != cms2.end() ; ++x){
    //     cout << &x << endl;
    // }
    if (cms2.empty())
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
    return 0;
}