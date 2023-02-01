echo -e ' \e[103m +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+ \e[0m\n' \
        '\e[103m |T|G|S|T|u|r|b|o| |i|n|s|t|a|l|l| \e[0m\n' \
        '\e[103m +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+ \e[0m\n'

echo 'Starting install...'
sleep 1

apt update 
apt -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold"  upgrade -y
apt install python3 git -y
pip3 install pipenv
git clone https://github.com/liriondev/TGSTurbo
cd TGSTurbo
pipenv install
