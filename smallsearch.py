# small search file program

def check_num_query( query_list):
    """
    this function check the no of matching keywords from the query to the list of results and form a list,
    where score is the total count of matching keywords as per order of list of results.

     """
    for i in list_of_results:

        score = 0

        for j in query_list:

            list_of_results_check = i.split(" ")

            score += list_of_results_check.count(j)

        global result_refrence
        Scores.append(score)

    return Scores



if __name__ == '__main__':


    # list of results
    list_of_results = ["this is good", "python is the best programming language", "python  language and python snake is two different things", "samrat is one of the best programmer"]


    #query by user
    query = input("enter your query ")

    query_list = query.split(" ")

    Scores = []

    # calling function
    check_num_query(query_list)

    # now my result_refrence had all the  values
    # print(result_refrence)
    # making list of decending order of Scores

    sortedS = [sentscore for sentscore in sorted(zip(Scores, list_of_results), reverse= True)]      #most important step
    # print(sortedS)

    # relevent results
    rel_sortedS = []
    for score , item in sortedS:

        if score == 0:
            pass
        else:
            rel_sortedS.append(item)

    print(f"Total {len(rel_sortedS)} results are found")

    # printing relevent results in specific order
    for i in rel_sortedS:
        print(i)





