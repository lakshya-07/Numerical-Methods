	program stats
	implicit none
	integer ::i,j,tnum
	real :: item,nsum,sqrsum,mean,var1,var2,std1,std2

	write(*,"(1x,a34)")"Enter total number of data items:"
	read(*,*)tnum
	write(*,*)

	nsum = 0
	sqrsum = 0
	do i = 1,tnum,1
        write(*,"(1x,a16,i4,a2)")"Enter data item",i,":"
	    read(*,*)item
	    nsum = nsum + (item)
	    sqrsum = sqrsum + (item**2)
	end do

	mean = nsum/tnum

	var1 = (sqrsum - (nsum**2)/tnum)/(tnum-1)

	var2 = (sqrsum/tnum - (mean**2))

	std1 = sqrt(var1)
	std2 = sqrt(var2)
	write(*,*)
	write(*,*)"The Mean of the given data is = ",mean
	write(*,*)
	write(*,*)"The Sample Variance of the given data is = ",var1
	write(*,*)"The Sample Standard Deviation of the given data is = ",std1
	write(*,*)
	write(*,*)"The Poplution Variance of the given data is = ",var2
	write(*,*)"The Population Standard Deviation of the given data is = ",std2

	end program stats
