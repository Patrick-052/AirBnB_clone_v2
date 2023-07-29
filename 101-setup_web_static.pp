# configuring nginx
package { 'nginx':
  ensure => installed,
}

exec { 'creating directories':
  command => 'mkdir -p /data/web_static/releases/test /data/web_static/shared',
}

file { 'writing to a file':
  path    => '/data/web_static/releases/test/index.html',
  content =>
  "<html>
    <head>
    </head>
    <body>
      Well my config file works fine!!
    </body>
  </html>",
}

exec { 'creating a symbolic link':
  command => 'rm -f /data/web_static/current && ln -s /data/web_static/releases/test/ /data/web_static/current',
}

file { '/data/':
  ensure => directory,
  path   => '/data/',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file_line { 'append_after_pattern':
  ensure =>  present,
  path   => '/etc/nginx/sites-available/default',
  line   => 'location /hbnb_static {\n\talias /data/web_static/current/;\n\t}',
  match  => 'server_name _;',
  notify => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
}
