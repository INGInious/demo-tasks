#Dummy example of ipython script to evaluate student answer for equation: 2x²-Value=0
import math

#Get the random input parameter and select a predifined value based on it
RandomIndex=int(float(get_input("@random")[0]*100))%6
Values = [8, 18, 32, 50, 72, 98]
Value=Values[RandomIndex]

#Get the student answer and the correct answer
Student = int(get_input("test"))
Solution = int(math.sqrt(Value/2))

#As an example, the two answers can be accessed from command line via temporary environment variables
#This is useful if you want to share the same variable for python commands and bash commands
%env MySolution=$Solution
%env StudentSolution=$Student

#Compare student solution and correct solution.
#This could be implemeneted in python but here it uses bash for the Ipython example
! if [ "$StudentSolution" = "$MySolution" ]; then feedback-result success; else feedback-result failed; fi
