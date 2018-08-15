
#部署django
###添加用户
1. 添加用户并且设置密码

		$ useradd yinmingke
		$ passwd yinmingke

2.给新添加的用户赋予可以sudo的权限

		$ echo "yinmingke ALL=(All)ALL" >> /etc/sudoers

3.切换到yinmingke用户环境

###添加yum源

1. 网址是<https://iuscommunity.org/pages/Repos.html>
2. 下载两个仓库的rpm文件

		$ wget http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
		$ wget http://dl.iuscommunity.org/pub/ius/stable/CentOS/7/x86_64/ius-release-1.0-14.ius.centos7.noarch.rpm


3. 安装

		$ sudo rpm -ivh epel-release-7-5.noarch.rpm
		$ sudo rpm -ivh ius-release-1.0-13.ius.centos7.noarch.rpm

4. 查看结果

 		$ sudo yum repolist

5. 批量安装下开发工具，这样，下面就不用单独安装gcc了

		$ sudo yum -y update
		$ sudo yum install -y zlib-dev openssl-devel sqlite-devel bzip2-devel

5. cent7 不需要单独去配置国内源
6. 安装zsh 及autojump

		$ sudo yum install zsh
		$ curl -L http://install.ohmyz.sh | sh
		$ chsh -s /bin/zsh
		$ sudo yum install autojump
		$ sudo yum install autojump-zsh

7. 编辑 .zshrc,加入sudo插件,然后重启动

8.编辑~/.zshrc , 更改皮肤为

###安装vsftpd
1. 安装vsftpd

		$ sudo yum -y install vsftpd

2. 编辑配置文件

		$ sudo vi /etc/vsftpd/vsftpd.conf

		anonymous_enable=NO

		chroot_local_users=YES
		末尾添加：
		allow_writeable_chroot=YES

3. 启动vsftpd

		sudo service vsftpd start

4. 让vsftpd开机启动

		sudo systemctl enable vsftpd.service

5. 检查vsftpd是否启动

		pgrep vsftpd

		如果出现进程号就表示已经成功启动





###安装mariadb
1. 删除自带的mariadb

		$ sudo yum remove mariadb-libs -y

2. 安装mariadb

		$ sudo yum install mariadb100u-server mariadb100u -y

3. 启动 mariadb

		$ sudo service mariadb start

4. 让mariadb服务开机就启动

		$ sudo systemctl enable mariadb.service

5. 执行数据的安全设置

		$ mysql_secure_installation

6. 开启mysql root 远程访问的的代码

		mysql>  GRANT ALL PRIVILEGES ON *.* TO root@"%" IDENTIFIED BY "密码";
		mysql>  flush privileges;

###安装python3.4

1. 下载python3.4 源码包 (会比较慢，翻墙更佳)

		$ wget https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tgz

2. 解压

		$ tar xvf Python-3.4.3.tgz

3. 进入解压后目录


4. 准备将python3安装在/usr/local/python3	下，所以先新建这个目录

		$ sudo mkdir /usr/local/python3

5. 先指定安装目录，再make，最后make install

		$ ./configure --prefix /usr/local/python3
		$ make
		$ sudo make install
		$ sudo cp /usr/local/python3/bin/pip3 /usr/bin

	更改pip源，国外的源实在太慢了

		新建一个文件 ~/.config/pip/pip.conf,添加如下内容
		[global]
		index-url = http://pypi.douban.com/simple
		[install]
		trusted-host = pypi.douban.com

		然后要搞明白一点，如果是sudo pip install ，实际上是去root用户目录下找这个pip.conf的。
		所以，这个文件其实应该放在两个地方，一个是当前用户~下，一个是root~下。

		$ sudo pip3 install --upgrade pip
7. 删除原先python的快捷方式

		$ sudo rm -rf /usr/bin/python

8. 对python3 建立快捷方式

		$ sudo ln -s /usr/local/python3/bin/python3 /usr/bin/python

9. 这时，运行python 就应该是 python3.4了
10. 修复yum

		$ sudo vi /usr/bin/yum
		$ sudo vi /usr/libexec/urlgrabber-ext-down

	将第一行变成
			#!/usr/bin/python2.7

###安装django


		$ sudo pip3 install django

###安装uwsgi

		$ sudo yum install python-devel
		$ sudo pip3 install uwsgi
		$ sudo ln -s /usr/local/python3/bin/uwsgi /usr/bin/uwsgi



###部署
1. 生成本地密钥对

		$ ssh-keygen -t rsa

2. 将 ~/.ssh/id_rsa.pub 的内容 部署到 bitbucket 上

		$ cat ~/.ssh/id_rsa.pub
		选择，复制到剪贴板
		访问 http://bitbucket.org,登录，进入项目 mysite

1. 从bitbucket上克隆代码

		如果挂载第二块磁盘，一般挂载到用户主目录下的disk子目录，这么做的目的是为了方便ftp上传和下载,如果没有第二块磁盘，直接创建一个disk目录
		$ mkdir ~/disk
		$ cd disk
		创建www目录
		$ mkdir www
		$ cd www
		下面的操作都在www里面进行
		$ git clone git@bitbucket.org:yin_mingke/mysite.git
		$ mkdir resources
		经过上面一步后， www 下面应该有两个子目录，一个是克隆下来的mysite，一个是resources
		$ chmod -R 755 www
		$ cd mysite
		$ sudo yum install libjpeg-turbo libjpeg-turbo-devel //如果系统中没有安装jpeg库，可能在安装pillow时出错
		$ sudo pip3 install -r package.txt //安装所有的第三方django包
		$ pip3 list //验证

2. 安装配置nginx

		$ sudo yum -y install nginx
		$ sudo systemctl enable nginx.service
		$ sudo cp /home/yinmingke/disk/www/mysite/nginx.conf /etc/nginx/nginx.conf
		$ mkdir ~/disk/log
		$ mkdir ~/disk/log/nginx //为错误日志存放地点建立目录

3. 编辑/etc/rc.local ，让uwsgi在开机时启动

		sudo vi /etc/rc.d/rc.local
		将下面一行添加到rc.local的尾部
		su yinmingke -c "uwsgi --ini /home/yinmingke/disk/www/mysite/mysite_uwsgi.ini"

		$ sudo chmod +x /etc/rc.d/rc.local
		$ sudo reboot

这样之后,应该就能愉快的运行了