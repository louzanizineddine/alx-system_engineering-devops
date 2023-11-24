#install Flask from pip3

package { 'Flask':
ensure   => installed,
provider => 'pip3',
version  => '2.1.0',
}

