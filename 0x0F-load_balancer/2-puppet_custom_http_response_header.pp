# Use Puppet to automate the task of creating a custom HTTP header response
exec {'update':
  command => '/usr/bin/apt-get update',
}
-> package {'nginx':
  ensure => 'present',
}
-> exec { 'insert_header_line':
  command => "sed -i '47i\        add_header X-Served-By \$hostname;' /etc/nginx/sites-enabled/default",
  path    => ['/bin', '/usr/bin'],
}
-> exec {'run':
  command => '/usr/sbin/service nginx restart',
}
