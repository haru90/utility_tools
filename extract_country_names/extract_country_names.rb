require 'csv'

unless ARGV.size == 2
  puts 'Usage: ruby extract_country_names.rb [in Google countries.csv path] [out path]'
end

country_names = []

CSV.foreach(ARGV[0], headers: true) do |r|
  country_names.push(r['name'])
end

country_names.sort!

File.open(ARGV[1], 'w') do |f|
  country_names.each do |country_name|
    f.puts(country_name)
  end
end
