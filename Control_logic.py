from __future__ import division
import time
import Adafruit_PCA9685

def Move_to_target(start,end):
    dist = abs(end - start)
    steps = (dist//1.2) + 1
    print(steps)
    
    while steps:
        
        # Engage Lower Limb
        L3.engage_gecko(M_gecko)
        L4.engage_gecko(M_gecko)
        L5.engage_gecko(M_gecko)
        
        # Move Forward
        L1.extend_limb(M_starfish)
        L2.extend_limb(M_starfish)
        
        # Engage Forward Limbs
        L1.engage_gecko(M_gecko)
        L2.engage_gecko(M_gecko)
        
        # Disengage Back Limbs
        L3.disengage_gecko(M_gecko)
        L4.disengage_gecko(M_gecko)
        L5.disengage_gecko(M_gecko)
        
        # Shift Forward -> Compress back Limbs
        L3.contract_limb(M_starfish)
        L4.contract_limb(M_starfish)
        L5.contract_limb(M_starfish)
        
        # Compress Forward Limbs Just for stall
        L1.contract_limb(M_starfish)
        L2.contract_limb(M_starfish)
        
        #Disengage Gecko Patch
        L1.disengage_gecko(M_gecko)
        L2.disengage_gecko(M_gecko)
        
        if steps%100 == 0:
            print('Steps left',steps-1)
        steps -=1
    
    print('Motion complete')
    return 1

Move_to_target(0,6)