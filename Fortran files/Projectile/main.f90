program projectile
implicit none

real ,parameter :: pi = 22/7, g = 9.81
real :: u ,theta, ti, tf, tstep, t,x,y,rad
integer :: i

write(*,*)"Enter the value of velocity:"
read(*,*)u

write(*,*)"Enter the value of angle:"
read(*,*)theta

rad = theta*(pi/180)
ti = 0
tf = 2*u*sin(rad)/g
tstep = (tf - ti)/20

open(unit = 10, file = 'Angle = 75deg')
! In output file, the value of the velocity is 5 m/s

do i = 1,20
     t = ti + i*tstep
     x = u*cos(rad)*t
     y = u*sin(rad)*t - 0.5*g*t*t
     write(10,*)x,y
end do

close(10)

end program projectile
