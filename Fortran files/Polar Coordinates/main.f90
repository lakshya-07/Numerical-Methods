	program cartesian_to_polar
		implicit none
		real,parameter :: pi= 3.14159
		real :: x,y,r,ang,theta,deg

		write(*,*)"Give the value of x coordinate:"
		read(*,*)x
		write(*,*)"Give the value of y coordinate:"
		read(*,*)y

		r = sqrt(x**2+y**2)
		ang = abs(y/x)
		theta = atan(ang) !theta represent angle in radian
		deg =(180*theta)/pi !deg represent angle in degree

		if((x >= 0 ) .and. (y >= 0)) then
		write(*,*)"The value of Polar coordinate 'r' =",r
		write(*,*)"The value of Polar coordinate 'theta' =",deg

		else
		if((x < 0 ) .and. (y > 0) ) then
		write(*,*)"The value of Polar coordinate 'r' =",r
		write(*,*)"The value of Polar coordinate 'theta' =",(deg + 90)
		else
		if((x < 0 ) .and. (y < 0)) then
		write(*,*)"The value of Polar coordinate 'r' =",r
		write(*,*)"The value of Polar coordinate 'theta' =",(deg + 180)

		else
		if((x > 0 ) .and. (y < 0)) then
		write(*,*)"The value of Polar coordinate 'r' =",r
		write(*,*)"The value of Polar coordinate 'theta' =",(deg + 270)

		else
		write(*,*)"Your input is invalid"
		end if
		end if
		end if
		end if

		end program cartesian_to_polar
