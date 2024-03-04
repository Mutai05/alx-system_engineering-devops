# Automate the task of creating a custom HTTP header response, but with Puppet
exec { 'configure_custom_http_header':
  command  => "apt-get -y update && apt-get -y install nginx && sed -i '/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;' /etc/nginx/sites-available/default && service nginx restart",
  provider => shell,
  path     => '/usr/bin:/bin',  # Add the path to the shell command if necessary
  require  => Package['nginx'],  # Ensure that Nginx is installed before running the command
}
