# Hardcoded sequence
dna_sequence = "ATGC"

# Limpieza
dna_sequence = dna_sequence.strip()
dna_sequence = dna_sequence.upper()
dna_sequence = dna_sequence.replace(" ", "")

# Conteos
count_a = dna_sequence.count("A")
count_t = dna_sequence.count("T")
count_g = dna_sequence.count("G")
count_c = dna_sequence.count("C")

# Longitud
length = count_a + count_c + count_t + count_g


# Output

if(dna_sequence):
    print(f"sequence: {dna_sequence}")
    print(f"a_content: {count_a}   c_content: {count_c}   t_content: {count_t}   g_content: {count_g}")
    print(f"Length:", length)
    print(f"gc_content: {((count_c+count_g)/length)*100:.2f}%")
else:
    print(f"error: no sequence found, length:", length)
