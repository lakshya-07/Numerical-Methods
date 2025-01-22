cd 'C:\Users\Lakshya Singh\Desktop\codeblocks\Fortran files\Euler Method'
plot 'Exact Graph' w l lw 3, 'For n = 2' w l lw 3,'For n = 8' w l lw 3,'For n = 16' w l lw 3,'For n = 32' w l lw 3  
set title "Euler's Method Graph for dy/dx = 2x"                                                                     
set xlabel 'Values of x' 
set ylabel 'Values of y'
replot
