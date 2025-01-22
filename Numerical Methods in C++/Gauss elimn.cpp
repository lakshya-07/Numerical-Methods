#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main(){
int i,j,k,l,n;

cout << "Enter the number of unknowns: ";
cin >> n;

double a[n][n+1],m,x[n],s;

cout << "Enter the values of augmented matrix: "<< endl;
for(i = 0;i < n;i++)
	 {
		  for(j = 0;j <= n;j++){
			   cout<<"a["<< i<<"]"<< j<<"]= ";
			   cin>>a[i][j];
		  }
	 }

for(i = 0; i < n; i++){
        if(a[i][i] == 0){
            cout << "Diagonal entry is zero. No unique solution exists." << endl;
            exit;
        }
        for(j = i+1; j <= n-1;j++){
                m = a[j][i]/a[i][i];


        for(k = 0; k <= n; k++){
            a[j][k] = a[j][k] - m*a[i][k];
        }
        }
}


cout << endl;
cout << "Upper triangular coefficient matrix is given by: " << endl;
for(k = 0; k < n; k++){
        cout << setprecision(3);
    for(l = 0; l < n+1; l++){
        cout << a[k][l] <<"      ";
        if(l == n){
            cout<<endl;
        }
    }
}


x[-1] = a[n-1][n]/a[n-1][n-1];

for(i = n-1; i >= 0; i--)
	{
		s=0;
		for(j = i+1; j <= n; j++){

		s += a[i][j]*x[j];
		x[i]=(a[i][n]-s)/a[i][i];
		}

	}

cout<< endl<<"Solutions of the matrix system are: "<< endl;
	 for(i = 0;i < n;i++)
	 {
	  	cout<<"x["<< i<<"] = "<< x[i]<< endl;
	 }






return 0;

}
