#!/usr/bin/bash


#建立信任关系
read -p 'Please input target server ipAddress :' tg_ip
read -p 'Please input target server username :' tg_user

#获取当前用户名

user=`whoami`

#获取当前用户家目录
user_home_path=`cat /etc/passwd | grep ${user} | tail -1 | cut -d ':' -f 6`


cd ${user_home_path}/.ssh

#根据DSA算法生成私钥和公钥
echo '下面的步骤一路回车'
ssh-keygen -t dsa

#拷贝公钥给目标服务器
ssh-copy-id -i id_dsa.pub –p 22 ${tg_user}@${tg_ip}




















