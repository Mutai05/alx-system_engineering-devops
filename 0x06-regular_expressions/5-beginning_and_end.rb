#!/usr/bin/env ruby

# Accepts one argument from the command line
input_string = ARGV[0]

# Regular expression to match pattern starting with 'h', ending with 'n', and having any single character in between
regex = /^h.n$/

# Method to match and output the result
def match_pattern(input_string, regex)
  if input_string.match?(regex)
    puts input_string
  else
    puts "$"
  end
end

# Calls the method with the input string and regex
match_pattern(input_string, regex)
