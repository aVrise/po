#include <bits/stdc++.h>
using namespace std;

typedef pair<int, string> PAIR;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    vector<pair> cv;
    set<pair> cs;
    map<int, int> cm;
    int ci, cj = 1, cb;
    string ca;
    cin >> ci;
    for (int i = 0; ci < i; ci++)
    {
        cin >> ca >> cb;
        cm[ca] += 1;
        cs.insert(make_pair(cb,ca));
    }
    return 0;
}