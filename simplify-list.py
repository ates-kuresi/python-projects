if __name__ == '__main__':
    mylist=[1,2,3,5,5,5,5,4,3,5] # write your list inside of this.
    scores=[]
    for n in mylist:
        if n in scores:
            pass
        else:
            scores.append(n)
    print(scores)
