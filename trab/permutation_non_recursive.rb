def each_permutation(letters, &block)
  used = {}
  used_in_columns = (0...letters.size).map{Hash.new}
  current = []
  i = 0
  total_permutations = (2..letters.size).inject(:*)

  while i != total_permutations
    while current.size != letters.size
      letters.each do |l|
        column = used_in_columns[current.size]
        if !used[l] && !column[l]
          current << l 
          used[l] = true
          column[l] = true
          break
        end
      end
    end

    yield current, i
    i += 1

    while current.size == letters.size || letters.all?{|l| used_in_columns[current.size][l] || used[l]}
      if current.size < letters.size
        used_in_columns[current.size] = {}
      end
      removed = current.pop
      used[removed] = false
    end
  end
end

each_permutation(%w{a b c}){|perm, i| puts "#{i}: #{perm.inspect}"}
