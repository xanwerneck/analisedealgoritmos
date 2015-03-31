def bigger_sum(a)
  n = a.size
  sum = 0
  max_sum = -9999999
  begin_i = 0
  interval = [0,0]
  a.each_with_index do |num, i|
    sum += num
    if sum > max_sum
      max_sum = sum
      interval = [begin_i, i]
    end
    if sum < 0
      sum = 0
      begin_i = i + 1
    end
  end
  return interval
end

TEST_CASES = [
  [[1, 2, 3], [0,2]],
  [[-1, 2, 3], [1,2]],
  [[1, -2, 3], [2,2]],
  [[1, -2, 100, -91, 40, 50], [2,2]],
  [[1000, -2, -100, -91, -40, -50], [0,0]],
  [[-1000, -2, -100, -91, -40, -50], [1,1]]
]

failed = TEST_CASES.find{|(array, expected)| bigger_sum(array) != expected}
if failed.nil?
  puts "Os testes passaram"
else
  array = failed[0]
  expected = failed[1]
  puts "O caso #{array.inspect} falhou, retornou #{bigger_sum(array).inspect} mas deveria ser #{expected.inspect}"
end
