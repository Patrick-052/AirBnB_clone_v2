# configuring nginx
package { 'nginx':
  ensure => present,
}

-> file { '/data':
  ensure  => 'directory'
}

-> file { '/data/web_static':
  ensure => 'directory'
}

-> file { '/data/web_static/releases':
  ensure => 'directory'
}

-> file { '/data/web_static/releases/test':
  ensure => 'directory'
}

-> file { '/data/web_static/shared':
  ensure => 'directory'
}

file { '/data/web_static/releases/test/index.html':
  content =>
  "<html>
    <head>
    </head>
    <body>
      Well my config file works fine!!
    </body>
  </html>",
}

-> file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test'
}

-> exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

file_line { 'append_after_pattern':
  ensure =>  present,
  path   => '/etc/nginx/sites-available/default',
  line   => 'location /hbnb_static {\n\talias /data/web_static/current/;\n\t}',
  match  => 'server_name _;',
  notify => Service['nginx'],
}

-> exec { 'nginx restart':
  path => '/etc/init.d/'
}
