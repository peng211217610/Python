#!/bin/bash

#进入到common目录，引入配置
cd "$HOME"/phm/backup_common || exit;. ./begin_config.sh

#ftp脚本
function my_ftp(){
cd ../backup_receive || exit
ftp -niv <<- EOF
open ${IP_ADDRESS}
user ${USERNAME} ${PASSWORD}
ascii
cd phm/
prompt off
mget *
bye
EOF
}

