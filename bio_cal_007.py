def Hanoi_towers(n,startPeg,destinationPeg):
    if(n==1):
        print("diski baslangic peginden",startPeg, "hedef pege tasi",destinationPeg)
        return
    transitPeg = 6-startPeg-destinationPeg
    Hanoi_towers(n-1,startPeg,transitPeg)
    print("disk baslangic peginden",startPeg,  "hedef pege tasindi",destinationPeg)
    Hanoi_towers(n-1,transitPeg,destinationPeg)
    return
Hanoi_towers(3,2,4)
