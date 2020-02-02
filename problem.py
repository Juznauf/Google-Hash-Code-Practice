# problem description 
# order at most one pizza of each type


# Estimated the max number of pizza slices that you want to order based on the number of registered participants 

# the goal is to order as many pizza slices as possible, but not more than the max number 

# the input is a text file with two lines
# first line is the number of max slices followed by the number of types
# second line is a ordered list of the number of slices for each type of pizza.

# output should contain two lines
# first line is a single integer K, the number of different types of pizza to order
# second line should contain K numbers, the types of pizza to order , and numbered from 0 to N-1 in the order they are listed in the input

# must return the number of pizzas followed by their indexes


def submit(out_file, result):

    """
    function to write to file
    out_file as type txt and result is a list of pizza slices with their corresponding indexes (index,slices)
    """
    types = len(result)
    pizzas_index = [x[0] for x in result]
    with open(out_file, 'w') as out_file:
        out_file.write(str(types) + '\n')
        out_file.write(' '.join([str(x) for x in pizzas_index[::-1]])) # reverse back the index list
 


def pizza_to_order(in_file, out_file):
    
    """
    function to execute calculations, takes in a in_file(data) and 
    out_file(output) as args
    """
    PIZZA_ORDERED_DICT = {}
    result_ls = []
    
    with open(in_file) as in_file:
        in_file_ls = []
        for line in in_file:
            in_file_ls.append(line)
        MAX_SLICES = int(in_file_ls[0].strip('\n').split()[0])
        PIZZA_ORDERED_LS = [int(x) for x in in_file_ls[1].strip('\n').split()] 

        print('=' * len(f"The maximum number of slices allowed is {MAX_SLICES}."))
        print(f"The maximum number of slices allowed is {MAX_SLICES}.") # print out max slices for evaluation
        BENCHMARK = MAX_SLICES
        PIZZA_ORDERED_LS = list(enumerate(PIZZA_ORDERED_LS))

        for slices in PIZZA_ORDERED_LS[::-1]:
            MAX_SLICES -= slices[1]
            result_ls.append(slices)

            if MAX_SLICES == 0: #if perfect 
                break #break loop and execute the submit function 
            elif MAX_SLICES <0: #if minus down goes below 
                MAX_SLICES += slices[1] # sum back the previous slice
                result_ls.pop() # pop the last item from the result list
                continue # continue to the next iteration
        print(f"The score for this data set is {BENCHMARK - MAX_SLICES}.")
        # print(BENCHMARK - MAX_SLICES)
        submit(out_file, result_ls) #call the submit function 


        # indexing from the right 
        # # for i in range(1, len(PIZZA_ORDERED_LS) + 1): # form the dictionary
        # #     PIZZA_ORDERED_DICT[PIZZA_ORDERED_LS[-i]] = -i  # reverse the list iteration
        # #     MAX_SLICES -= PIZZA_ORDERED_LS[-i]
        # #     result_ls.append((PIZZA_ORDERED_LS[-1],-i))
        # #     # will not work as this assumes the first x is taken as a final answer 
        # #     if MAX_SLICES == 0:  # if perfect
        # #         break # break loop and return the dict key with value
        # #     elif MAX_SLICES < 0: # if minus down goes below
        # #         MAX_SLICES += PIZZA_ORDERED_LS[-i] # sum back the previous list 
        # #         result_ls.pop()  # pop the last item from the list
        # #         continue 
        
        # submit(out_file, result_ls)


            

if __name__ == "__main__":

    # calculate the scores for this model. The score is calculated as the number of slices returned from the list of pizzas
    input_data = ['a_example.in','b_small.in','c_medium.in','d_quite_big.in', 'e_also_big.in']

    print('calculating from data set a to data set e')
    print('-' * len('calculating from data set a to data set e'))


    for data in input_data:
        print('\n\n')
        in_file = data
        out_file = data.split('.')[0] + '.txt'
        print(f'Evaluating data set {data}')
        pizza_to_order(in_file, out_file)  