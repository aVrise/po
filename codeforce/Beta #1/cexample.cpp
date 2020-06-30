#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <string>
#include <cmath>
#include <queue>
#include <stack>

using namespace std;

#define pi 3.141592653589793
#define eps 10e-3

typedef struct point
{
    double x, y;
};

point p[3];

double area(double x0, double y0, double x1, double y1, double x2, double y2)
{
    return 0.5 * fabs(x0 * y1 + x2 * y0 + x1 * y2 - x2 * y1 - x0 * y2 - x1 * y0);
}

double dis(point a, point b)
{
    return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

bool is_ok(int n, double jiao)
{
    double cnt = n * jiao / pi;
    double pnt = floor(cnt + eps);
    if (cnt - pnt < eps)
        return true;
    return false;
}

int main()
{
    for (int i = 0; i < 3; i++)
        scanf("%lf%lf", &p[i].x, &p[i].y);
    double a = dis(p[0], p[1]);
    double b = dis(p[0], p[2]);
    double c = dis(p[1], p[2]);
    double A = acos((b * b + c * c - a * a) / 2 / b / c);
    double B = acos((a * a + c * c - b * b) / 2 / a / c);
    double C = acos((b * b + a * a - c * c) / 2 / b / a);
    double r = a * b * c / area(p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y) / 4;

    int n;
    for (n = 3; n <= 100; n++)
        if (is_ok(n, A) && is_ok(n, B) && is_ok(n, C))
            break;

    double tag = 2 * pi / n;
    double Area = n * r * r * sin(tag) / 2;

    printf("%.8lf\n", Area);
    return 0;
}