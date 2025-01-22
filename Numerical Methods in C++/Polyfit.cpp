#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main(){
int i,j,k,l,N,n;

cout << "Enter the number of data points: ";
cin >> N;


double x[N],y[N],a[N][N+1],m,X[N],s;;

for(i = 0; i < N; i++){
    cout << "Enter the value of x["<<i<<"]: ";
    cin >> x[i];
}
cout<<endl;
for(i = 0; i < N; i++){
    cout << "Enter the value of y["<<i<<"]: ";
    cin >> y[i];
}
cout<<endl;

cout << "Enter the degree of polynomial to be fitted: ";
cin >> n;

for(i = 0; i < n+1; i++){
    for(j = 0; j < n+1; j++){
        a[i][j] = 0;
        a[i][n+1] = 0;

        for(k = 0; k < N; k++){
            a[i][j] = a[i][j] + pow(x[k],i+j);
            a[i][n+1] = a[i][n+1] + y[k]*pow(x[k],i);
        }

    }
}



cout << endl;
cout << "The generated augmented matrix is: "<<endl;
for(k = 0; k < n+1; k++){
        cout << setprecision(3);
    for(l = 0; l < n+2; l++){
        cout << a[k][l] <<"      ";
    }
    cout<<endl;
}

n = n+1;
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


X[-1] = a[n-1][n]/a[n-1][n-1];

for(i = n-1; i >= 0; i--)
	{
		s=0;
		for(j = i+1; j <= n; j++){

		s += a[i][j]*X[j];
		X[i]=(a[i][n]-s)/a[i][i];
		}

	}

cout<< endl<<"Solutions of the matrix system are: "<< endl;
	 for(i = 0;i < n;i++)
	 {
	  	cout<<"x["<< i<<"] = "<< X[i]<< endl;
	 }




return 0;}




