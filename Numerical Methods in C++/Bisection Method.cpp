//bisection method
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

double funct(double x){ //any function can be implemented here

      //return (pow(x,3) + x*x + x +7);  //problem 1
       return (x*exp(x)-1);              //problem 2
}

double bisection(double a, double b, double e){
    double c;
    int i;
    int n = log(abs(b-a)/e)/log(2);

    cout << "No. of iterations will be = "<< n << endl;
    cout << endl;

    if (funct(a)*funct(b) >= 0){
cout << "You have not assumed right a and b" << endl;
return 0;}
cout << "n" <<setw(15)<< "a" << setw(15) << "funct(a)" <<setw(15)<< "b" <<  setw(15) << "funct(b)" <<setw(15)<< "c" <<setw(15)<< "funct(c)"<< endl;
cout << "--------------------------------------------------------------------------------------------------------------"<< endl;

while (abs(b-a) >= e){  // e is the tolerance
  // loop for printing iterations

    c = (a+b)/2;

    cout << ++i <<setw(15)<< a << setw(15) << funct(a) << setw(15)<< b << setw(15) << funct(b)<<setw(15)<< c <<setw(15)<< funct(c)<< endl;

    if(funct(c) == 0){ // c is the root
        break;
    } else if (funct(a)*funct(c) < 0){ //if negative putting b=c & new interval is [a,c]
    b = c;}
    else{
        a = c;}  // now new interval is [c,b]


}
cout << endl;
cout << "The calculated value of root is "<< c << endl;


}

int main(){
int i;
double a, b ,c,e;
cout << "Enter the value of a: ";
cin >> a;

cout << "Enter the value of b: ";
cin >> b;

cout << "Enter the value of tolerance limit: ";
cin >> e;

bisection(a,b,e); //calling above function of bisection

return 0;
  }
