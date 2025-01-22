	program quadratic_equation
    implicit none

    real :: axsq, bx, con, discrmnt, r1, r2,realprt, imgprt

    write(*,*)"Give the value of a:"
    read(*,*)axsq

     write(*,*)"Give the value of b:"
    read(*,*)bx

     write(*,*)"Give the value of c:"
    read(*,*)con

        discrmnt = bx*bx - 4*axsq*con

if(discrmnt > 0) then

        r1 = (-bx + sqrt(discrmnt))/2*axsq
        r2 = (-bx - sqrt(discrmnt))/2*axsq

        write(*,"(1x,a34,f7.3)")"The first root of the equation is",r1
        write(*,"(1x,a35,f7.3)")"The second root of the equation is",r2

else
    if(discrmnt .eq. 0) then

        r1 = -bx/(2*axsq)
        r2 = -bx/(2*axsq)

        write(*,"(1x,a34,f7.3)")"The first root of the equation is",r1
        write(*,"(1x,a35,f7.3)")"The second root of the equation is",r2
    else
        if(discrmnt < 0) then

             realprt = -bx/(2*axsq)
             imgprt = sqrt(-discrmnt)/(2*axsq)

        write(*,"(1x,a34,f7.3,a2,f6.3,a1)")"The first root of the equation is",realprt,"+",imgprt,"i"
        write(*,"(1x,a35,f7.3,a2,f6.3,a1)")"The second root of the equation is",realprt,"-",imgprt,"i"

        else
            write(*,*)"Your input is invalid"

            end if
            end if
            end if

end program quadratic_equation
