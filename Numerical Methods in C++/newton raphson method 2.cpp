//newton raphson method
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

double funct(double x)
{

    return (3*x+sin(x)-exp(x));
}

double dfunct(double x)
{

    return (3+cos(x)-exp(x));
}

void nrm(double a,double e)
{

    if(funct(a)== 0){
        cout << "Your initial guess is the root the function." << endl;
    }
    if(dfunct(a)== 0){
        cout << endl;
        cout << "Your initial guess is making the derivative 0." << endl;
    }


    double d = funct(a)/dfunct(a);
    int i;
    cout << "n" <<setw(15)<< "a" <<setw(15)<< "f(x)" <<setw(15)<< "f'(x)"<< endl;
    cout << "----------------------------------------------------------------------"<< endl;

    while(abs(d) >= e)
    {
        d = funct(a)/dfunct(a);
        a = a - d;
            cout << ++i <<setw(15)<< a <<setw(15)<< funct(a) <<setw(15)<< dfunct(a) << endl;
    }
    cout << endl;
    cout << "The calculated value of root is "<< a << endl;

}



int main()
{ int i;
double a,e;

cout << "Enter the value of initial guess: ";
cin >> a;

cout << "Enter the value of tolerance: ";
cin >> e;

nrm(a,e);



    return 0;
}





