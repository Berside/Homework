#pragma once
#include <cmath>
#include <vector>
using namespace std;
   vector<double> solve(double a, double b, double c) {
   double d = b*b - 4*a*c;
   vector<double> roots;

   if (d > 0) {
       roots.push_back((-b + sqrt(d)) / (2*a));
       roots.push_back((-b - sqrt(d)) / (2*a));
   }
   else if (d== 0) {
       roots.push_back(-b / (2*a));
   }
   return roots;
}