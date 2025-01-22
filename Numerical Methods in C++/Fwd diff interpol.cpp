//Newton forward difference interpolation
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

double pval(double p,int n){
    double t = p;
    for(int i = 1; i < n ; i++){
         t = t*(p-i);}
    return t;
}

int factorial(int n){
    int fact = 1;
    if ( n == 0){
             return 1;
    } else{
        for(int i = 1; i < n + 1; i++){
                fact = fact*i;}
    }
    return fact;
}

int main()
{ int i,j,n,k;

cout << "Enter the total number of data points: ";
cin >> n;

double x[n], y[n][n],val,s,p;

 for(i = 0; i < n ; i++){
  cout << "Enter the value of x[" << i << "] = ";
  cin >> x[i];
 }
 cout << endl;

 for(i = 0; i < n ; i++){
  cout << "Enter the value of y[" << i <<"] = ";
  cin >> y[i][0];
 }

 cout<<endl;
 cout << "Enter the value of point you want to find: ";
cin >> val;

for(i = 1; i < n; i++){
  for(j = 0; j < n-i; j++){
   y[j][i] = y[j+1][i-1] - y[j][i-1];
  }
 }

cout<<endl;

cout << "The required Forward Difference table is:"<< endl;
cout << endl;


cout << "X[]" << setw(10) << "Y[]";

for(i = 1; i < n; i++){
        cout << setw(10) << "DEL["<<i<<"]";
 }
 cout<<endl;
 cout<<"-----------------------------------------------------------"<<endl;

 for(i = 0; i < n; i++){
  cout << x[i];
  for(j = 0; j < n-i ; j++){
   cout << setw(10) << y[i][j];
  }
  cout << endl;
 }

p = (val - x[0])/(x[1] - x[0]);

s = y[0][0];
for(k = 1; k < n; k++){
    s = s + (pval(p,k)*y[0][k])/factorial(k);
}
cout << endl;
cout << "The calculated value of y at x = "<< val << " is " << s << endl;

    return 0;
}






