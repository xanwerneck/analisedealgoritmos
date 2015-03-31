BASE = 40

class Array
  def to_arithmetic_number(base)
    b = base**self.size
    self.inject(0){|result, nxt| result + nxt*(b/=base) }
  end

  def arithmetic_each(size, base, &block)
    number = self[0...size].to_arithmetic_number(base)
    yield number, 0
    base_mult = base**(size-1)
    self[size..-1].each_with_index do |nxt, i|
      number = (number - (number/base_mult)*base_mult)*base + nxt
      yield number, i+1
    end
  end
end

def matching(p, t)
  m = p.size
  n = t.size
  tnumber = t.to_arithmetic_number(BASE)
  valids = []
  p.arithmetic_each(n, BASE) do |pnumber, start_i|
    if pnumber == tnumber
      valids << start_i
    end
  end
  return valids
end


TEST_CASES = [
  [[1,2,3,4,5], [1,2], [0]],
  [[1,2,3,4,5,1,2], [1,2], [0,5]],
  [[1,2,3,4,5,1,2], [1,2,3], [0]],
  [[1,2,3,4,5,1,2], [1,2,3,9], []],
  [[1,2,3,4,5,1,2,1], [1], [0,5,7]],
  [[14,29,30,41,15,14,29,30], [14,29,30], [0,5]]
]

failing_case = TEST_CASES.find{|(p, t, expected)| matching(p,t) != expected}
if failing_case.nil?
  puts "Todos os testes passaram"
else
  p = failing_case[0]
  t = failing_case[1]
  expected = failing_case[2]

  puts "O caso (#{p.inspect},#{t.inspect}) falhou. retornou #{matching(p,t).inspect} mas deveria ser #{expected.inspect}"
end
