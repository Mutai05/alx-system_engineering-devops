# 2-execute_a_command.pp

# Ensure the process 'killmenow' is terminated using pkill
exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/bin:/usr/bin',
  refreshonly => true,
}
