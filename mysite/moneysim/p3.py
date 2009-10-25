#===============================================================================
# Part C for Assignment 1, Financial Technology
# Yi Wang    
#    yw2298@columbia.edu 
# Yuan Wang
#    yw2326@columbia.edu
#
#===============================================================================

from time import localtime, strftime
import os,sys
import random
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
# import pylab

#===============================================================================
# Fed interest rate related function definitions
#===============================================================================
Fed_rate = 0.05 # Fed interest rate    
SCALAR = 10;
random.seed(100) # set the random seed
Nb=5 # number of banks
Nc=5 # number of comsumers
    
def bid_ask():
    """
    in the range of 1-2%
    """
    return random.random()*0.01+0.01

def rate_factor_bank():
    """
    factor to adjust bank's loan bias due to Fed interest rate
    """
    return 1 + Fed_rate * SCALAR

def rate_factor_consumer():
    """
    factor to adjust consumer based on interest rate
    """
    return 1 + (Fed_rate + bid_ask())*SCALAR

# note.txt records bank failure info etc.
#sys.stdout = open('note.txt','w')
print '# simulation start at', strftime("%a, %d %b %Y %H:%M:%S +0000", localtime())


def sim(rr,seed):
    Fed_rate = rr/100
    random.seed(seed) # set the random seed
    #===============================================================================
    # Initial value of concerned variables, for Chart Later
    #===============================================================================
    
    Fed_R = [0]# total money from bank reserves
    #M=[550.]
    M=[]
    B=[100.]
    #rr=[0.1]
    #cr=0.1
    
    rr= []
    cr= []
    #give cr and rr a random init
    cr_init = random.uniform(0.1,0.2)
    rr_init = random.uniform(0.05,0.06)
    rr.append(rr_init)
    cr.append(cr_init)
    
    M_init = (cr[0]+1) * B[0] /(cr[0]+rr[0])
    M.append(M_init)
    
    #get D which is Total_B_C + R
    D_init = M[0]/(cr[0]+1)
    
    Total_Consumer_C_init = M[0]-D_init
    
    #===============================================================================
    # Consumer init
    #===============================================================================
    Consumer_D = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    Consumer_L = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    #Consumer_C = [10,10,10,10,10]
    Consumer_C =[0,0,0,0,0]
    
    for i in range(Nc):
        Consumer_C[i] = Total_Consumer_C_init / 5
    
    GDP_max = 0.1
    GDP_min = -0.03
    
    # Bank init
    #===============================================================================
    #Bank_C = [100,100,100,100,100]
    Bank_C = [0,0,0,0,0]
    for i in range(Nb):
        Bank_C[i]= D_init / 5
    
    Bank_L = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    Bank_R = [0,0,0,0,0]
    for i in range(Nb):
        Bank_R[i] = Bank_C[i]*rr[0]
        Bank_C[i] = Bank_C[i] - Bank_R[i]
        
    Fed_R[0] = sum(Bank_R)
    Fed_L =[0,0,0,0,0]
    
    #===============================================================================
    # Sample init
    #===============================================================================
    Bank_C_Sample = []
    Bank_R_Sample = []
    Consumer_C_Sample = []
    Fed_L_Sample = []
    
    #===============================================================================
    # Simulation Start
    # Number of simulation cycles
    #===============================================================================
    Ntime = 100 
    for step in range(Ntime):
        Bank_C_prev = Bank_C[:]
        Consumer_C_prev = Consumer_C[:]
        # Make more activities among banks and consumer
        # inner cycle
        for j in range(int(5*random.random())):
            #===============================================================================
            # Consumer & Bank # Nc
            #===============================================================================
            for i in range(Nc):
                deposit_state = random.randrange(0,2)
                loan_state = random.randrange(0,2)
                if (Consumer_C[i]>0) and (deposit_state == 1):
                    Consumer_D[i][i] =  random.random() * Consumer_C[i] * rate_factor_consumer()
                    Consumer_C[i] = Consumer_C[i] - Consumer_D[i][i]
                if (Consumer_C[i]>0) and (loan_state == 1):
                    # if change 0.25 to 0.5, some banks maybe fail
                    #0.25 no fail condition
                    Consumer_L[i][i] =  0.1*random.random() * Bank_C[i]* rate_factor_bank()
                    Consumer_C[i] = Consumer_C[i] + Consumer_L[i][i]
        #        print step,i,str(Consumer_C[i]),str(Consumer_L[i][i]),str(Consumer_D[i][i]),'BEFORE'
        #        if Consumer_C[i]<0:
        #            pass
        #            print step,i,str(Consumer_C[i]),str(Consumer_L[i][i]),str(Consumer_D[i][i])
                
            #===============================================================================
            # Bank & Bank
            # b loan from b+1
            #===============================================================================
            for b in range(Nb):
                bank_loan_state = random.randrange(0,2)
                if (b != 4) and (Bank_C[b+1]>0) and (bank_loan_state == 1):
                    Bank_L[b][b+1] = random.random() * Bank_C[b+1] * rate_factor_bank()
        #            print step,b,'bank loan',Bank_L[b][b+1]
                elif(Bank_C[0]>0) and (bank_loan_state == 1) and (b == 4):
                    Bank_L[4][0] = random.random() * Bank_C[0] * rate_factor_bank()
                
            #    if (b==0) and (Bank_C[1]>0) and (bank_loan_state == 1):
            #        Bank_L[0][1] = 0.1 * Bank_C[1] + Bank_L[0][1]
            
            #===============================================================================
            # Bank_C update
            #===============================================================================
            for b in range(Nb):
                if(b==0):
                    Bank_C[0] = Bank_C[0] + Bank_L[0][1]+ Consumer_D[0][0] - Consumer_L[0][0]-Bank_L[4][0]
                elif(b==4):
                    Bank_C[4] = Bank_C[4] + Bank_L[4][0]+ Consumer_D[4][4] - Consumer_L[4][4]-Bank_L[3][4]
                else :
                    Bank_C[b] = Bank_C[b] + Bank_L[b][b+1]+ Consumer_D[b][b] - Consumer_L[b][b]-Bank_L[b-1][b]
                    
                
        #===============================================================================
        # Fed loan to Bank to bail out
        #===============================================================================
        # calculate Fed_L to Bank
        # if Bank_C<20; Fed loan 10 to Bank
        
        Fed_L =[0,0,0,0,0]
        for b in range(Nb):
            if(0 < Bank_C[b]<=20):
                """ when bank's money goes low """
                Fed_L[b]=Fed_L[b]+9
                Bank_C[b] = Bank_C[b]+ 9
            while(Bank_C[b]<0):
                """ bank failure """
                # always bail out
                # print step,'\tBank',b,'fail',round(Bank_C[b],2),
                # Fed bail out bank        
                Bank_C[b] = Bank_C[b]+ 29
                Fed_L[b] = Fed_L[b]+ 29
                # print '\tafter bail out', round(Bank_C[b],2)
    
        #===============================================================================
        # Adjust net assets of consumers and banks
        # according to GDP rate
        #===============================================================================
        for i in range(Nb):
            diff = (Bank_C[i]-Bank_C_prev[i])/Bank_C_prev[i]
            if diff > GDP_max:
                Bank_C[i] = Bank_C_prev[i]*(1+GDP_max)
            if diff < GDP_min:
                Bank_C[i] = Bank_C_prev[i]*(1+GDP_min)
                
        for i in range(Nc):
            diff = (Consumer_C[i]-Consumer_C_prev[i])/Consumer_C_prev[i]
            if diff > GDP_max:
                Consumer_C[i] = Consumer_C_prev[i]*(1+GDP_max)
            if diff < GDP_min:
                Consumer_C[i] = Consumer_C_prev[i]*(1+GDP_min)
    
        #===============================================================================
        # find new M B
        #===============================================================================
        Total_Bank_Currency = sum(Bank_C)
        Total_Consumer_Currency = sum(Consumer_C)
    #    sum all banks reserves
        Fed_R.append(sum(Bank_R))
        # M= Total_Consumer_C + Total_Bank_C + Fed_R
        M.append(Total_Bank_Currency + Total_Consumer_Currency)
        B.append(Total_Consumer_Currency+Fed_R[-1])
        cr.append(Total_Consumer_Currency/Total_Bank_Currency)
        #===============================================================================
        # Fed adjust rr based on new M/B
        #===============================================================================
        
    # var step is old step
    
        if M[step]/B[step]< M[-1]/B[-1]:
            #everytime increase will between 0 and i_max
    #        i_max=(1-rr[step])/10
            increase = random.uniform(0,0.1)
            rr.append(rr[step]*(1+increase))
        elif M[step]/B[step] > M[-1]/B[-1]:
            #everytime decrease will between 0 and c
    #        d_min=rr[step]/2
            decrease = random.uniform(0,0.1)
            rr.append(rr[step]*(1-decrease))
            
        else:
            rr.append(rr[step])
         #   rr[-1] = rr[step]
        
        #===============================================================================
        # Feb regulate banks through reserve
        # change Bank_R
        #===============================================================================
        for b in range(Nb):
    #        brr = Bank_R[b]/(Bank_R[b]+Bank_C[b])
            tempR = rr[step+1]*(Bank_R[b]+Bank_C[b])
            Bank_C[b] = Bank_C[b] + Bank_R[b] - tempR
            Bank_R[b] = tempR
                
        #===============================================================================
        # Bank and Comsumer Assert Change GDP
        #===============================================================================
        
        
        #===============================================================================
        # Bank & Consumer Sample  
        #===============================================================================
        Bank_C_Sample.append(Bank_C[0])
        Bank_R_Sample.append(Bank_R[0])
        Consumer_C_Sample.append(Consumer_C[0])
        Fed_L_Sample.append(Fed_L[0])
            
    #===============================================================================
    # Simulation End
    # end of one cycle        
    #===============================================================================
    
    # MB = M/B
    MB = [x/y for x,y in zip(M, B)]
    
    #===============================================================================
    # Output table to file out.txt
    #===============================================================================
    sys.stdout = open('/home/e/Desktop/Python/mysite/templates/moneysim/p3_table.txt','w')
    WIDTH = 14
    
    #Header
     
     
    print 'step'.ljust(4),\
      'M'.rjust(WIDTH),\
      'B'.rjust(WIDTH),\
      'Fed_R'.rjust(WIDTH),\
      'M/B'.rjust(WIDTH),\
      'rr'.rjust(WIDTH)
    
    for i in range(Ntime):
        print str(i+1).ljust(4),\
        str(round(M[i],2)).rjust(WIDTH),\
        str(round(B[i],2)).rjust(WIDTH),\
        str(round(Fed_R[i],2)).rjust(WIDTH),\
        str(round(MB[i],2)).rjust(WIDTH),\
        (str(round(rr[i]*100,2))+'%').rjust(WIDTH)
    
    #===============================================================================
    # Chart
    #===============================================================================
    
    fig = plt.figure(3)
    ax = fig.add_subplot(421)
    ax.plot(M, 'r-',B,'b-')
    ax.legend(('M', 'B'), shadow = True,loc='upper center')
    
    ax = fig.add_subplot(423)
    ax.plot(Fed_R,'g-')
    ax.legend(('Fed_R',), shadow = True,loc='upper center')
    
    ax = fig.add_subplot(425)
    ax.plot(MB, '-')
    ax.legend(('v=M/B',), shadow = True,loc='upper center')
    
    ax = fig.add_subplot(427)
    ax.plot(rr, '-')
    ax.legend((r'rr',), shadow = True,loc='upper center')
    
    #--Sample on the right--------------------------------------------------------------------------- 
    ax = fig.add_subplot(422)
    ax.plot(Bank_C_Sample, 'r-')
    ax.legend(('Bank_C_Sample',), shadow = True,loc='upper center')
    
    ax = fig.add_subplot(424)
    ax.plot(Bank_R_Sample,'g-',Fed_L_Sample,'r-')
    ax.legend(('Bank_R_Sample','Fed_L_Sample'), shadow = True,loc='upper center')
    
    ax = fig.add_subplot(426)
    ax.plot(Consumer_C_Sample,'y-')
    ax.legend(('Consumer_C_Sample',), shadow = True,loc='upper center')
    
    ax = fig.add_subplot(428)
    ax.plot(cr, 'k-')
    ax.legend(('cr',), shadow = True,loc='upper center')
    
    #--------------------------------------------------------------- plt.show();
    #os.remove('/home/e/Desktop/Python/mysite/templates/moneysim/p3.png')
    plt.savefig('/home/e/Desktop/Python/mysite/templates/moneysim/p3.png')
    return 0
