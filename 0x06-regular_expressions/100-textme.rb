#!/usr/bin/env ruby

# Accepts one argument from the command line
input_string = ARGV[0]

# Regular expressions to extract sender, receiver, and flags
sender_regex = /\[from:([\w+]+)\]/
receiver_regex = /\[to:([\w+]+)\]/
flags_regex = /\[flags:(\-?\d+:\d+:\-?\d+:\d+:\-?\d+)\]/

# Method to extract sender, receiver, and flags from the log line
def extract_info(input_string, sender_regex, receiver_regex, flags_regex)
  sender = input_string.match(sender_regex)[1]
  receiver = input_string.match(receiver_regex)[1]
  flags = input_string.match(flags_regex)[1]
  puts "#{sender},#{receiver},#{flags}"
end

# Calls the method with the input string and regex patterns
extract_info(input_string, sender_regex, receiver_regex, flags_regex)
