cd 'C:\Users\Lakshya Singh\Desktop\codeblocks\Fortran files\Projectile'
plot 'Angle = 30deg' w l lw 3, 'Angle = 45deg' w l lw 3, 'Angle = 60deg' w l lw 3, 'Angle = 75deg' w l lw 3, 'Angle = 90deg' w l lw 3  
set title 'Trajectories of Projectile at different angles'
set xlabel 'Distance travelled along x-axis' 
set ylabel 'Distance travelled along y-axis' 
replot
