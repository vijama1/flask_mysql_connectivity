# flask_mysql_connectivity
Steps to install mysql-server:

    $ sudo apt update
    $ sudo apt install mysql-server
    $ sudo mysql_secure_installation (it will ask for password and various fields just enter the password which you want and press y elsewhere)
    Adjusting user authentication privileges (By default in mysql 5.7 root is granted with socket_auth plugin so password login will display a error, to make login possible with password for root do this:) $ sudo mysql mysql> SELECT user,authentication_string,plugin,host FROM mysql.user; mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_password'; mysql> FLUSH PRIVILEGES; mysql> exit now you can login normally by your_password

Steps to install mysql.connector: $ sudo apt-get install python3-mysql.connector
To install flask:
  sudo pip3 install flask
