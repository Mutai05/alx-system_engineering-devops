# Puppet manifest to configure custom HTTP response header

# Install Nginx package
package { 'nginx':
  ensure => present,
}

# Get the hostname of the server
$hostname = $::hostname

# Create a custom Nginx configuration file
file { '/etc/nginx/conf.d/custom_header.conf':
  ensure  => file,
  content => "add_header X-Served-By $hostname;",
  notify  => Service['nginx'],
}

# Restart Nginx when the configuration changes
service { 'nginx':
  ensure => running,
  enable => true,
  require => File['/etc/nginx/conf.d/custom_header.conf'],
}

# Display success message
notify { "Nginx configured with custom HTTP response header X-Served-By on $hostname": }
