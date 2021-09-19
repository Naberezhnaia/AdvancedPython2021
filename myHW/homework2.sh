cd ~
> info.txt
touch info.txt
date >> info.txt
whoami >> info.txt
uname >> info.txt
find ~ -maxdepth 1 -type d | wc -l >> info.txt
find ~ -type f | wc -l >> info.txt

