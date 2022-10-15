def correct(*tests):
    result = {}
    total = 0
    max = 0
    min = 10
    # here we have a list with a person name as index[0] and then the correct answers to compare
    comparer = ['person', 'A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']

    for group in tests:
        count = 0
        for each in group:
                if len(each) > 1:
                    result[each] = 0
                    count += 1
                else:
                    if each == comparer[count]:
                        result[group[0]] += 1
                        count += 1
                        
    print('Student               Grade')

    for name, grade in result.items():
        total += grade
        if max < grade:
            max = grade
        if min > grade:
            min = grade

        print(f'{name}                 {grade}')

    average = total / len(result)

    print('---------------------------')
    print(f'General average: {average}')
    print(f'Max grade: {max}')
    print(f'Min grade: {min}')
    print(f'Student total: {len(result)}')

# here is called the function by passing 2 lists, both with the student's name on index 0 and then its answer on the "imaginay" questions
correct(('Renzo','A','B','C','D','E','E','A','C','B','A'), ('Martha','A','B','C','D','E','E','D','C','B','B' ))