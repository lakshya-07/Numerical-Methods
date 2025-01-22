//newton raphson method
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

double funct(double x){

      return (pow(x,6)-x-1);
}


void secant(double x1 ,double x2 ,double e){ // x1 = x_n-1 and x2 = xn
    double h,a;
    int i = 0;

   if(funct(x1)== 0){
            cout <<"The required value of root is " << x1 << endl; //in case chosen guess is the root
            }

    if(funct(x2)== 0){
            cout <<"The required value of root is " << x2 << endl;
    }

    else if((funct(x2)-funct(x1))== 0){
            cout << "Your initial guesses are making denominator 0."<< endl;}
  else{
    //cout << setprecision(8);
    cout << "n" <<setw(10)<< "x1"<< setw(20)<< "funct(x1)" <<setw(20)<< "x2"<< setw(20)<< "funct(x2)" <<setw(20)<< "x_n+1" <<setw(20)<< "funct(x_n+1)"<< endl;
  cout << "--------------------------------------------------------------------------------------------------------------------"<< endl;
   h = funct(x2)*((x2-x1)/(funct(x2)-funct(x1))); //secant step size

    while(abs(h) >= e){
         h = funct(x2)*((x2-x1)/(funct(x2)-funct(x1)));
         a = x2 - h;
         cout << ++i <<setw(10)<< x1<< setw(20) << funct(x1) <<setw(20)<<  x2<< setw(20)<< funct(x2) <<setw(20)<< a <<setw(20)<< funct(a) << endl;
         x1 = x2;  // for next iteration changing x1 to x2
         x2 = a; //  also x2 is put equal to calculated new root a
    }
    cout << endl;
    cout <<"The final value of root is " << a << endl;
  }



}

int main(){

    double x1,x2,e;
    cout << "Enter the value of first guess: ";
    cin >> x1;

    cout << "Enter the value of second guess: ";
    cin >> x2;

    cout << "Enter the value of tolerance limit: ";
    cin >> e;

    cout << endl;

    secant(x1,x2,e);


return 0;}

