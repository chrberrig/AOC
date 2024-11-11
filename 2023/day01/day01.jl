f = open("input_day01.txt", "r")

# pt. 1:
onlynumbers = l -> filter(c->isdigit(c), collect(l))
firstandlast = arr -> parse(Int, string(arr[1], arr[end]))
cleanline = firstandlast∘onlynumbers
res = sum([cleanline(line) for line in readlines(f)])
print(res)

# pt. 2:
function translate_to_ints(l)
    trans_dict = Dict("zero"=>0, "one"=>1, "two"=>2, "three"=>3, "four"=>4, "five"=>5, "six"=>6, "seven"=>7, "eight"=>8, "nine"=>9)
    for (k, v) in trans_dict
        println(k, v)
        l = replace(l, k => v)
    end
    println(l)
    return l
end

cleanline2 = firstandlast∘onlynumbers∘translate_to_ints
for line in readlines(f)
    println("hi")
    println(line, translate_to_ints(line))
end
res = sum([cleanline2(line) for line in readlines(f)])
println(res)

close(f)
