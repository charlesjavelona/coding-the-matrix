def create_voting_dict(strlist):
    """
    Input: strlist, has a structure [party affilate(R or D)| home state, voting records(1, 0, -1)] ['Bunning R KY 1 -1 1 1 1 0 1 1 1 1 1 1', Name party affiliate, home state, voting records, ... and so on] 
    Output: Return a dictionary that maps the last name of a senator to it's voting record. Here's an example: {Bunning: [1, -1, 1, 1, 0, 1]}
    """
    dic = {}
    for element in strlist:
        e = element.split()
        dic[e[0]] = [int(l) for l in e[3:]] 
    return dic            
        
