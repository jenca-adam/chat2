rm -rf .ssh
echo " na dialogu, ktory sa otvori postlacaj same entery"
konsole -e ssh-keygen -t rsa

ssh-copy-id $1@turing.gjh.sk >/dev/null 2>/dev/null
cd
clear
mkdir .sc 2>/dev/null
echo "clear
ssh jenca.a@turing.gjh.sk
clear" >.sc/schoologin
echo export\ PATH=\$PATH:$(pwd)/.sc >>.bashrc
chmod a+x .sc/schoologin
clear
echo "prihlas sa do skoly prikazom \"schoologin\""
bash -rcfile .bashrc

