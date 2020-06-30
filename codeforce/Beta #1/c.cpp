#include <bits/stdc++.h>
using namespace std;

const long double PI = 3.141592653589793238L;

double gcd(double a, double b)
{
    if (b < 0.1)
        return a;
    if (a > b || abs(a - b) < 1e-9)
    {
        int j = 1;
        for (int i = 1; i * b - a <= 1e-9; i++)
        {
            j = i;
        }
        a = a - j * b;
    }
    //cout << 123 << endl;
    // cout << a << "ppp" << b << endl;
    return gcd(b, a);
}

double angle(double a1, double b1, double a2, double b2, double a3, double b3)
{
    double x1 = a2 - a1, y1 = b2 - b1, x2 = a3 - a1, y2 = b3 - b1;
    double theta = acos(((x1 * x2) + (y1 * y2)) / sqrt((x1 * x1 + y1 * y1) * (x2 * x2 + y2 * y2))) * 180 / PI;
    return theta;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    double x, y, x1, x2, x3, y1, y2, y3, a1, b1, c1, a2, b2, c2;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
    a1 = x1 - x2;
    b1 = y1 - y2;
    c1 = -(x2 * x2 + y2 * y2 - x1 * x1 - y1 * y1) / 2;
    a2 = x2 - x3;
    b2 = y2 - y3;
    c2 = -(x3 * x3 + y3 * y3 - x2 * x2 - y2 * y2) / 2;
    x = -(b1 * c2 - b2 * c1) / (b2 * a1 - b1 * a2);
    y = -(a1 * c2 - a2 * c1) / (a2 * b1 - a1 * b2);
    double r = sqrt((x - x1) * (x - x1) + (y - y1) * (y - y1));
    // double r2 = sqrt((x - x2) * (x - x2) + (y - y2) * (y - y2));
    // double r3 = sqrt((x - x3) * (x - x3) + (y - y3) * (y - y3));
    // cout << r2 << r3 << r << endl;

    double angle1, angle2, angle3;
    angle1 = angle(x, y, x1, y1, x2, y2);
    angle2 = angle(x, y, x2, y2, x3, y3);
    angle3 = angle(x, y, x3, y3, x1, y1);
    // cout << angle1 << endl
    //      << angle2 << endl
    //      << angle3 << endl;
    double anglemax;
    anglemax = min(gcd(angle1, angle2), gcd(angle2, angle3));
    // cout << anglemax << endl;
    if (abs(360 / anglemax - round(360 / anglemax)) > 0.01)
    {
        int j = 1;
        for (int i = 2; abs(360 * i / anglemax - round(360 * i / anglemax)) > 0.01; i++)
            j = i;
        anglemax /= j + 1;
    }
    // cout << anglemax << endl;
    double answer = 180 / anglemax * r * r * sin(anglemax * PI / 180);
    // cout << 180 / anglemax * r * r * sin(anglemax * PI / 180) << endl;
    printf("%.6f\n", answer);
    return 0;
}