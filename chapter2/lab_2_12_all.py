def create_voting_dict(strlist):
    """
    Input: strlist, has a structure [party affilate(R or D)| home state, voting records(1, 0, -1)] ['Bunning R KY 1 -1 1 1 1 0 1 1 1 1 1 1', Name party affiliate, home state, voting records, ... and so on] 
    Output: Return a dictionary that maps the last name of a senator to it's voting record. Here's an example: {Bunning: [1, -1, 1, 1, 0, 1]}
    """
    voting_dict = dict() 
    for element in strlist:
        e = element.split(' ')
        voting_dict[e[0]] = [int(l) for l in e[3:]] 
    return voting_dict 


def extract_democrats(strlist):
    """
    Input: strlist. A list with a structure [{name, party affiliate(R or D) | home state, voting records}
    Output: A list of all the names in the democrat party
    """
    l = set()
    for element in strlist:
        e = element.split(' ')
        if(e[1] == 'D'): l.add(e[0])
    return list(l)    
        

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Inputs: 
        sen_a is senator A
        sen_b is senator B
        voting_dict is the result from the voting list converted to a dictionary
    Output: The dot product between the values of sen_a and sen_b     
    """
    sen_a_result = voting_dict[sen_a]
    sen_b_result = voting_dict[sen_b]
    return sum([ a*b for a, b in zip(voting_dict[sen_a], voting_dict[sen_b])])


def most_similar(sen, voting_dict):
    """
    Inputs: 
        sen is a string name of a senator. Ex. 'Biden'
        voting_dict is the dictionary list containing all of the senators and their voting records
    
    Outputs: 
        Return a senator name that is most similar to the voting records. Excluding the current senator input
    

    Define most similar?
        Most similar is when two senators dot product result is greater than 1. 
    """
    num = 0
    name = ''
    for v in voting_dict:
        if(v == sen): continue
        result = policy_compare(sen, v, voting_dict) 
        if(num < result): 
            num = result
            name = v
    return name


def least_similar(sen, voting_dict):
    """
    Inputs: 
        sen is a string name of a senator. Ex. 'Biden'
        voting_dict is the dictionary list containing all of the senators and their voting records
    
    Outputs: 
        Return a senator name that is least similar to the voting records. Excluding the current senator input
    

    Define least similar?
        Least similar is when two senators dot product result is less than 0. 
    """
    num = 100
    name = ''
    for v in voting_dict:
        if(v == sen): continue
        result = policy_compare(sen, v, voting_dict) 
        if(result < num): 
            num = result
            name = v
    return [name, num]

def find_average_similarities(sen, sen_set, voting_dict):
    """
    Inputs:
        sen, senator name
        sen_set, list containing names of senators
        voting_dict, dictionary with key value paris of senators and their voting records

    Output:
        The average results of the dot product between the sen variable and sen_set 
    """
    result = 0 
    for s in sen_set:
        if(s == sen): 
            sen_set.remove(s) 
            continue
        result += policy_compare(sen, s, voting_dict)
    return result/len(sen_set)


def find_average_record(sen_set, voting_dict):
    """
    Input:
        sen_set, is a list of senator names
        voting_dict is a key value pair of senators and their voting records
    Output:
        The average record given a senator set
    """
    result = 0
    for s in sen_set:
        result += sum(voting_dict[s])
    return result/len(sen_set)        


def procedure_bitter_rivals(voting_dict):
    """
    Input: voting_dict is a key value pair of senators and their voting records
    Output: Two names that disagree the most
    """
    result = 100
    curr_sen = ''
    least_sen = ''
    num = 0
    for k in voting_dict:
        curr_sen, num = least_similar(k, voting_dict)
        if(num < result):
            result = num
            least_sen = k
    return [curr_sen, least_sen, result]        
                


