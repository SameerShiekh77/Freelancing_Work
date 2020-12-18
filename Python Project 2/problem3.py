def countVotes(votes):
    #Yourcodegoesfromheretocounttheinputvotesandoutputvotingresult
    list1 = votes.split(',')
    count = 0
    reject = 0
    for x in list1:
        if (x.strip(' ') == 'y') or (x.strip(' ') == 'Y'):
            count = count + 1
        elif (x.strip(' ') == 'n') or (x.strip(' ') == 'N'):
            reject = reject + 1
    print(f"Reject: 20 votes in total, {count} accept and {reject} reject")


votes = "N ,Y, Y,N,n, N , N , N ,n ,y, n,N,Y, y,Y,N, N , n ,y, N"
# the function call below should display the message 
# Reject: 20 votes in total, 7 accept and 13 reject
countVotes(votes)

votes =  "y,n,Y,y,y ,n, N,  Y,N  , N,y, n,  Y,Y,y,  N  ,y, n,  n  , Y  "  #thefunctioncallbelowshoulddisplaythemessage
# Accept: 20 votes in total, 11 accept and 9 reject

countVotes(votes)

