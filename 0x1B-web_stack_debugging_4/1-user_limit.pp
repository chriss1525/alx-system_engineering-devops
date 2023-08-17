# Puppet file to change the OS configuration so that it is possible to login with the holberton user
# and open a file without any error message

exec {'replace-1':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 1024/" /etc/security/limits.conf',
  before   => Exec['replace-2'],
}

exec {'replace-2':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 1024/" /etc/security/limits.conf',
}
