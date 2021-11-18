

file = open('./rosalind_dna.txt', 'r')
input = file.read()

tot = len(input)

# Option 1, replace non A by "", repeat with the rest.
# Option 2, count A, count ... If I have the total I don't need to count all of them, only n-1 letters.

a_s = input.count("A")
c_s = input.count("C")
g_s = input.count("G")
t_s = tot - a_s - c_s - g_s

results = [a_s, c_s, g_s, t_s]

results_str = [str(elem) for elem in results]

results_str = " ".join(results_str)


print(results_str)