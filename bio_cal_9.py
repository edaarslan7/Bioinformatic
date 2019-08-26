def Hanoi_towers(n,startPeg,destinationPeg):
    if(n==1):
        print("diski baslangic peginden hedef pege tasi")
        return
    transitPeg = 6-startPeg-destinationPeg
    Hanoi_towers(n-1,startPeg,transitPeg)
    print("disk baslangic peginden hedef pege tasindi")
    Hanoi_towers(n-1,transitPeg,destinationPeg)
    return
