echo 'Begin to install python3!'
if [ -d '/usr/local/python3' ];then
	rm -rf /usr/local/python3
fi
mkdir /usr/local/python3
if [ -e /usr/local/${1} ];then
	mv /usr/local/${1} /usr/local/python3
else
	echo "/usr/local/  do not have ${1} the correct python3 package!"
	exit;
fi
cd /usr/local/python3
tar -xvf ${1}
untar_dir=`echo ${1} | cut -d '.' -f 1,2,3`
cd ${untar_dir}
./configure --prefix=/usr/local/python3
make
make install
cd /usr/bin
ln -s /usr/local/python3/bin/python3 /usr/bin/python3