	real function funct(x)
	real :: x
	funct = x**3
	return
	end function funct

	program integrate
	implicit none
	integer ::n,i,j
	real :: h,s,a,b,funct,I_exact,perror

	I_exact = 20.25

	write(*,*)"Enter the value of lower limit(a):"
	read(*,*)a

	write(*,*)"Enter the value of upper limit(b):"
	read(*,*)b
	write(*,*)

	write(*,*)"The exact value of the integral is =",I_exact
	write(*,*)

	do j = 1,7
	   write(*,"(1x,a55,i2,a1)")"Enter the value of n for step size for interation no. ",j,":"
	   read(*,*)n  !values of n taken are 1,2,4,8,16,32,64
   	   h = (b-a)/n
	   s = 0
	   do i = 1,n
	      s = s + funct(a + (2*i - 1)*(h/2))
	   end do
	   write(*,*)"The calculated value of integral=",s*h
	   perror = (abs(I_exact - (s*h))/I_exact)*100
	   write(*,*)"The error in the calculated value =",perror,"%"
	   write(*,*)
	end do

	end program integrate
