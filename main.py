
print("Get the multiples in common of two numbers")
print("")

up = True

while up:
    print("=====================================")
    n1 = input("Number 1: ")
    n2 = input("Number 2: ")
    n_range = input("Number of multiples: ")

    n1_list = []
    n2_list = []
    m_list = []

    try:
        for x in range(int(n_range)):
            n1_list.append(int(n1)*(x+1))

        for y in range(int(n_range)):
            n2_list.append(int(n2)*(y+1))

        for z in range(int(n_range)):
            if n1_list[z] in n2_list:
                m_list.append(n1_list[z])

        print(n1+"'s "+n_range+" Multiples: ")
        print(n1_list)
        print()
        print(n2+"'s "+n_range+" Multiples: ")
        print(n2_list)
        print()
        print("Matches: ")
        print(m_list)
        
    except:
        print("An error occured. Try again.")
        
