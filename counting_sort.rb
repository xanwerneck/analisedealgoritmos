def counting_sort(a, min: 0, max:nil)
  counts = Array.new(max-min, 0)
  a.each{|num| counts[num-min] += 1}
  counts[1..-1].each_with_index do |count, i|
    counts[i+1] += counts[i]
  end
  sorted = []
  a.reverse_each do |num|
    sorted[counts[num-min]-1] = num
    counts[num-min] -= 1
  end
  sorted
end

if ARGV[0] == "test"
  TEST_CASES = [
    [[3, 1, 2], [1, 2, 3]],
    [[9, 8, 2,  3, 1, 2], [1, 2, 2, 3, 8, 9]],
    [[9, 8, 7, 6, 5, 5, 5, 4, 3], [3, 4, 5, 5, 5, 6, 7, 8, 9]]
  ]

  failed = TEST_CASES.find{|(array, expected)| counting_sort(array.map{|x|x+900}, min: 900, max: 1000) != expected.map{|x|x+900}}
  if failed.nil?
    puts "Os testes passaram"
  else
    array = failed[0]
    expected = failed[1]
    puts "O caso #{array.inspect} falhou, retornou #{counting_sort(array.map{|x| x+900}, min: 900, max: 1000).inspect} mas deveria ser #{expected.inspect}"
  end
end
