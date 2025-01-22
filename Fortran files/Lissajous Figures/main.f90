	program lissajous
    implicit none

    integer ::i
    real :: x,y,f1,f2,t,p
    real,parameter :: pi = 3.1415

    write(*,*)"Enter the value of frequency for x-wave:"
    read(*,*)f1

    write(*,*)"Enter the value of frequency for y-wave:"
    read(*,*)f2

    p = 0
    write(*,*)"The value of phase difference is",p

    open(unit = 20, file = 'lissfigs')

    do i = 0,100,1
        t = 2*i*pi/100
        x = cos(f2*t + p)
        y = cos(f1*t)
        write(20,*)x,y
    end do

    close(20)


end program lissajous

