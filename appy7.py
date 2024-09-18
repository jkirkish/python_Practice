if __name__ == '__main__':
    # declare the list my_list as an empty list
    my_list = []
    #read the number of commands to put
    N = int(input())
    #process each command
    for _ in range(N):
        #use the input to separate the command and its arguments
        command = input().split()
        
        if command[0] == "insert":#inserts integer e at index i
            my_list.insert(int(command[1]), int(command[2]))
        elif command[0] == "print": #prints the first occurrence of e
            print(my_list)
        elif command[0] == "remove":#removes the first occurrence of e
            my_list.remove(int(command[1]))
        elif command[0] == "append": #appends e at the end of the list
            my_list.append(int(command[1]))
        elif command[0] == "sort": #sorts the list in ascending order
            my_list.sort()
        elif command[0] == "pop": #removes the last element from the list
            my_list.pop()
        elif command[0] == "reverse":#reverses the list
            my_list.reverse()