#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''Oracle'''

# 引入包



#Linux的操作
'''开启远程Oracle数据库'''
cmd_operate_oracle ='''#!/usr/bin/bash
su - oracle -c "lsnrctl start;sqlplus / as sysdba" << EOF
startup
EOF
'''
'''关闭远程Oracle数据库'''
cmd_shutdown_oracle = '''#!/usr/bin/bash
su - oracle -c "sqlplus / as sysdba" << EOF
shutdown immediate;
exit;
EOF
su - oracle -c "lsnrctl stop"
'''




















if __name__ == "__main__":
    pass
