# import string

# def print_rangoli(size):
#     lowercase = list(string.ascii_lowercase)
#     required_char = [lowercase[i] for i in range(size)]
#     half_ans = []
    
    
#     for j in required_char:
#         ele = ""
        
#         for x in range(size-1, lowercase.index(j), -1):
#             ele += lowercase[x]
        
#         half_ans.append("-".join(ele + j + ele[::-1]))


#     bottom_half = [h.center(len(half_ans[0]), "-") for h in half_ans]
#     top_half = [h.center(len(half_ans[0]), "-") for h in half_ans[-1:0:-1]]
#     result = top_half + bottom_half
        
#     print(*result, sep='\n')


# print_rangoli(3)
