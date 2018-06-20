def grade(score):
    if score >= 90:
        return 'A'
    elif (80<= score < 90):
        return 'B'
    elif (70<= score < 79) :
        return 'C'
    elif (60<= score < 69):
        return 'D'
    elif score < 60:
        return 'F'
print('your grade is: %s' %grade(45))
print('your grade is: %s' %grade(98))

    
    
        

        
    
