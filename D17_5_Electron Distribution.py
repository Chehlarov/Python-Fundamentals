number_of_electrons = int(input())

electrons = []
cell_layer = 1
while number_of_electrons > 0:
    possible_electrons = 2 * cell_layer ** 2
    electrons.append(min(possible_electrons, number_of_electrons))
    cell_layer += 1
    number_of_electrons -= possible_electrons

# result = [for layer in layers]

print(electrons)
