def vowels_counter(str):
     
    vowels: set = {'a', 'e', 'i', 'o', 'u'}



    vowels_count: int = 0
    for i in str:
        if i in vowels:
         vowels_count += 1
         print(i)
    print(vowels_count)

vowels_counter("Bilal")
