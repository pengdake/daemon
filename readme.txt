测试环境：
centos 7

执行方法：
启动所有eayunstack相关的守护进程
python control.py start
关闭所有eayunstack相关的守护进程
python control.py stop
重启所有eayunstack相关的守护进程
python control.py restart

memory_monitor要求
1.需要安装python-daemon和yaml的包
2.执行此服务需要超级用户权限
3.执行前，需将以内存使用量来排序的设置写入top的配置文件（先输入top，再输入M,最后输入W）


