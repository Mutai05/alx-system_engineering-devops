# 0-create_a_file.pp

# Ensure the file '/tmp/school' exists with the specified permissions, owner, and group
file { '/tmp/school':
  ensure  => 'file',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
