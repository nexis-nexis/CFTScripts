# I got tired of navigating to the Downloads folder and locating VPN files when I am working on platforms like
# hack-the-box, try-hack-me and proving-grounds. So I wrote this short bash script that automate the whole process. 

# Hope you enjoy it! 


#!/bin/bash
echo "Specify the VPN you which to start (HTB,THM or PG ): "
read openvpn  
if [ $openvpn == 'HTB' ]; then
    echo "VPN for HACK THE BOX Platform Starting......"
    sudo openvpn /home/kali/nexisnexis.ovpn
elif [ $openvpn == 'THM' ]; then
        echo "VPN for TRY HACK ME Platform Starting......"
        sudo openvpn /home/kali/tryhackme.ovpn
elif [ $openvpn == 'PG' ]; then
        echo "VPN for Proving Grounds Platform Starting......"
        sudo openvpn /home/kali/OS-549835-OSCP.ovpn
fi
