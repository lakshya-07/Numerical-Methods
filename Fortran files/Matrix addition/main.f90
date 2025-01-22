program addsubtract_matrix
	implicit none
	real, dimension(3,3) :: a,b,c,d
	integer :: i,j

	write(*,*)"For matrix A:"
	do i = 1,3
	    do j = 1,3
	       write(*,"(a22,i1,i1,a2)")"Enter the value of A(",i,j,"):"
	       read(*,*)a(i,j)
	    end do
	end do
	write(*,*)
	write(*,*)"For matrix B:"
	do i = 1,3
	    do j = 1,3
	       write(*,"(a22,i1,i1,a2)")"Enter the value of B(",i,j,"):"
	       read(*,*)b(i,j)
     	end do
	end do
	write(*,*)
	write(*,*)"The sum of matrix A and matrix B is given by matrix C:"
	do i = 1,3
	    do j = 1,3
	       c(i,j) = a(i,j) + b(i,j)
	       write(*,"(a22,i1,i1,a2,f10.2)")"The value of C(",i,j,"):",c(i,j)
	    end do
	end do
	write(*,*)
	write(*,*)"The differnce of matrix A and matrix B is given by matrix D:"
	do i = 1,3
     	do j = 1,3
        	d(i,j) = a(i,j) - b(i,j)
        	write(*,"(a22,i1,i1,a2,f10.2)")"The value of D(",i,j,"):",d(i,j)
       	end do
	end do

	end program addsubtract_matrix
