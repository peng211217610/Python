#!/bin/bash
#命令汇总
cd "$HOME"/phm/backup_common || exit;. ./function_common.sh;
echo "$line0"
#if条件对比
#
#echo –n "Enter your name:"
#read name
#if [ "${name}" == "" ]
#then
#    echo "You did not enter any information"
#else
#    echo "Your name: ${name}"
#fi
#echo "$line0"
#多条件情况
#if 条件1;then
#    if 条件2;then
#        命令1
#    else
#        命令2
#else
#    if条件3;then
#        命令3
#    else
#        命令4
#fi
echo "$line0"
#case的用法
    echo –n "enter a number from 1 to 5"
read NUM
case $NUM in
        1) echo "you select 1" ;;
        2) echo "you select 2" ;;
        3) echo "you select 3" ;;
        4) echo "you select 4" ;;
        5) echo "you select 5" ;;
        *) echo "basename $NUM is not between 1 and 5"
    esac
echo "$line0"
#注意区间的使用
echo –n "please input your mark:"
read mark
case $mark in
    100|9[0-9]|8[5-9]) echo "you are the best!";;#
    8[0-4]|7[0-9]) echo "you get a good mark!";;#        80-84、70-79
    7[0-4]|6[0-9]) echo "come on!";;#                    70-74、60-69
    [0-5][0-9]) echo "You must study hard!";;#            00-59
esac
echo "$line0"
#打印出一个格式供选择
#echo "——————–menu—————–"
echo ——————–menu—————–
echo "1 Show Time"
echo "2 CPU load"
echo "3 Memory free"
echo "0 Exit"
echo "——————————————–"
echo -n "Enter you chose [0-3]:"
read NUM
if [ "$NUM" -lt 0 ] || [ "$NUM" -gt 3 ]
then
    echo "This is not between 0-3."
else
    if [ "$NUM" == "1" ]
    then
        date +"%Y-%m-%d %H:%M:%S"
    else
        if [ "$NUM" == "2" ]
    then
        echo "傻了吧唧的"
        else
        if [ "$NUM" == "3" ]
        then
        echo "你个二货"
        else
            exit
        fi
    fi
    fi
fi