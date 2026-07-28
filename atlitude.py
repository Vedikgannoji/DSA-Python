gain = [-5,1,5,0,-7]
def highestAltitude(gain):
    attitude=0
    highest=0
    for g in gain:
        attitude+=g
        highest=max(highest,attitude)
    return highest
        
print(highestAltitude(gain))
            
