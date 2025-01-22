	program multiply_matrix
	implicit none
	real, dimension(3,3) :: a,b,c,d
	integer :: i,j,k,r1,r2,r3

	write(*,*)"Enter the number of rows in first matrix:"
	read(*,*)r1

	write(*,*)"Enter the number of columns in first matrix:"
	read(*,*)r2

	write(*,"(1x,a44,i8)")"The number of rows in second matrix will be:",r2
	write(*,*)
	write(*,*)"Enter the number of columns in second matrix:"
	read(*,*)r3

	write(*,*)
	write(*,*)"For matrix A:"

	do i = 1,r1
	    do j = 1,r2
	       write(*,"(a22,i1,i1,a2)")"Enter the value of A(",i,j,"):"
	       read(*,*)a(i,j)
	    end do
	end do

	write(*,*)
	write(*,*)"For matrix B:"

	do i = 1,r2
    	do j = 1,r3
           write(*,"(a22,i1,i1,a2)")"Enter the value of B(",i,j,"):"
	       read(*,*)b(i,j)
	   end do
	end do

	do i = 1,r1
    	do j = 1,r3
	       c(i,j) = 0
	           do k = 1,r2
	              c(i,j) = c(i,j) + a(i,k)*b(k,j)
          end do
	    end do
	end do

	write(*,*)
	write(*,*)"The product of matrix A and matrix B is given by matrix C:"

	do i = 1,r1
	    do j = 1,r3
	       write(*,"(a22,i1,i1,a2,f10.2)")"The value of C(",i,j,"):",c(i,j)
	    end do
	end do

	end program multiply_matrix
