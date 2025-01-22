	subroutine prime(num,div)
    integer :: num,div

    do div = 2,num
        if (mod(num,div) == 0) then
        if (num == div) then
            write(*,*)num
        else
                exit
        end if
        end if
    end do
    return
end subroutine prime

program primenum
    integer :: n,i,div
    write(*,*)"Enter the range of prime numbers from 0 to :"
    read(*,*)n

    write(*,"(1x,a45,i5)")"Here is list of prime numbers upto",n
    write(*,*)"-------------------------------------------------"

    if (n > 2) then
        write(*,"(10x,a2)")"2"
    end if

    do i = 3,n,1
        call prime(i,div)
    end do
end program primenum

