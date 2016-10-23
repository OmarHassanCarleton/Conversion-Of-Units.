#Omar Hassan
#101036344
#Assignment 1.2
#Gaddis, T. (2015). "Starting Out With Python"
#CULearn.(2016-09-28).Retrieved from https://culearn.carleton.ca/moodle/pluginfile.php/1854379/mod_resource/content/2/COMP1405-F16-XXX-XX-%28Assignment%201.2%20of%205%29.pdf

#one mickey is equivalent to 0.000127 metres
#one rope is equivalent to 6.096 metres        
Mickey=0.000127
Rope=6.096

#Ask user to enter any number
Number = float ( input( "Enter any number"))

#Converts Mickey to Rope units
Equation1= Number*Mickey/Rope 

#Converts Rope to Mickey units 
Equation2= Number*Rope/Mickey 

#Program prints the coversion units in mickey and rope
print("Mickey",Equation1,"Rope",Equation2)

