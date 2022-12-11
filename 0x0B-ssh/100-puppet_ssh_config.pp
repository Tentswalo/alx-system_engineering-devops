# Change SSH config file
exec { 'echo':
path => 'usr/bin:/bin',
command => 