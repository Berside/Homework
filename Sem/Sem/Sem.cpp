#include <iostream>
#include "Header.h"
using namespace std;

int main()
{
	int a, b, c;
	cout << " Enter first arg" << endl; 
	cin >> a; 
	cout << " Enter second arg" << endl;
	cin >> b;
	cout << " Enter thirst arg" << endl;
	cin >> c;
	cout << " " << endl; 
	vector <double> f = solve(a, b, c);
	for (int i = 0; i < f.size() ; i++) {
		cout << "Roots:" << endl;
		cout << f[i] << endl;
	}
}
