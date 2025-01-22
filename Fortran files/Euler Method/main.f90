	real function funct(x)
    real :: x
    funct = 2*x
    return
    end function funct

    program euler
    implicit none

    integer ::n,i,j
    real :: h,xf,xi,y,funct,y_anylt

    write(*,*)"Enter the initial value of x:"
    read(*,*)xi

    write(*,*)"Enter the initial value of y:"
    read(*,*)y

    write(*,*)"Enter the final value of x:"
    read(*,*)xf

    write(*,*)"Enter the value of 'n' for step size:"
    read(*,*)n

    h = ((xf-xi)/n)

    open(unit = 5, file = 'Exact Graph')

    do i = xi,xf
        write(5,*)i,i**2
    end do

    close(5)

    open(unit = 15, file = 'For n = 32')

    do i = 1,n
        y = y + funct(xi)*h
        xi = xi + h
        write(15,*)xi,y
    end do


    close(15)


    end program euler


