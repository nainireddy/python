def mergesort(nlist):
    if len(nlist) > 1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]


        mergesort(lefthalf)
        mergesort(righthalf)

        i=j=k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k] = lefthalf[i]
                i = i+1
            else:
                nlist[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            nlist[k] = lefthalf[i]
            i =i+1
            k = k+1

        while j < len(righthalf):
            nlist[k] = righthalf[j]
            j = j+1
            k = k+1

        return nlist



nlist = [33, 54, 45, 23, 11, 15, 87, 76, 64]

print mergesort(nlist)
