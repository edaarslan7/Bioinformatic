import random

def format_frequencies(frequencies):
    return ', '.join(['%s: %.2f' % (base, frequencies[base])
                      for base in frequencies])


def get_base_frequencies_v2(dna):
        return {base: dna.count(base)/float(len(dna))
                for base in 'ATGC'}

def mutate_v1(dna):
    dna_list = list(dna)
    mutation_site = random.randint(0, len(dna_list) - 1)
    dna_list[mutation_site] = random.choice(list('ATCG'))
    return ''.join(dna_list)


dna = 'ACGGAGATTTCGGTATGCAT'
print('Starting DNA:', dna)
print(format_frequencies(get_base_frequencies_v2(dna)))

nmutations = 10000
for i in range(nmutations):
    dna = mutate_v1(dna)

print('DNA after %d mutations:' % nmutations, dna)
print(format_frequencies(get_base_frequencies_v2(dna)))
