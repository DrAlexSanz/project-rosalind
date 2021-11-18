

file = open('./rosalind_rna.txt', 'r')
input = file.read()

#input = "GATGGAACTTGACTACGTAAATT"


# simply replace

repl = input.replace("T", "U")



print(repl)