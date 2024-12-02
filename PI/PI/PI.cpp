#include <iostream>
#include <string>
#include <map>
using namespace std;

class Student {
public:
	string name;
	double average_score;

	void print() {
		cout << "Name: " << name << endl << "Score: " << average_score << endl;
	}

	Student() : name(""), average_score(0.0) {}

	Student(string student_name, double student_score) {
		name = student_name;
		average_score = student_score;
	}

};
int main() {
	map<int, Student> list = {
		{25723, Student("Poverinov", 43.2)},
		{12352, Student("Naumov", 44.7)},
		{26143, Student("Popovic", 36.1)},
		{22411, Student("Babkin", 29)},
		{26321, Student("Pavlov", 25)},
		{10031, Student("Kamyshkin", 39.9)},
		{31231, Student("Lordler", 46.7)},
		{51231, Student("Snow", 54)},
		{02131, Student("Sandman", 41.2)},
		{12331, Student("Mamkin", 32.2)},
		{12345, Student("Lesorybov", 51.2)}
	};

	int number;
	int arr[11] = { 25723,12352,26143,22411,26321,10031,31231, 51231,02131,12331,12345 };
	cout << "Gradebook numbers:" << endl;
	for (int i = 0; i < 11; i++) {
		cout << arr[i] << " ";
	}
	cout << endl;

	string y = "Y";
	while ((y == "Y") or (y == "y")) {
		cout << "Enter gradebook number" << endl;
		cin >> number;
		if (list.find(number) != list.end()) {
			list[number].print();
		}
		else {
			cout << "No student with that number." << endl;
		}
		cout << "Next? ( Y or N)" << endl;
		cin >> y;
	}
}