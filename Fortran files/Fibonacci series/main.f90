	program fibonacci
    implicit none

    integer :: n
    real :: a,b,i,c

    write(*,*)"Enter the total number of terms required: "
    read(*,*)n

    a = 0
    b = 1
    write(*,"(f50.1)")a
    write(*,"(f50.1)")b

    do i = 1,n
        a = c
        c = b
        b = a + b
        write(*,"(f50.1)")b

    end do

end program Fibonacci
