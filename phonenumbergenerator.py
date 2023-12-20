#ethiopia phone number generator for wordlist

l = ['phone11.txt','phone12.txt','phone13.txt','phone20.txt']

for j in l:
    with open(j, 'w') as file:
        for i in range(1000000):
            # Format the number as a 6-digit string and write to the file
            if j == 'phone11.txt':
                file.write(f'0911{i:06d}\n')
            elif j == 'phone12.txt':
                file.write(f'0912{i:06d}\n')
            elif j == 'phone13.txt':
                file.write(f'0913{i:06d}\n')
            else:
                file.write(f'0920{i:06d}\n')