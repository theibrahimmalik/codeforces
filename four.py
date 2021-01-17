class AttackCleanup:
    
    def restore_data(self, message):
        
        finalMessage = []
        isNumber = False
        actualNumber = 0
        
        for character in message:
            while isNumber:
                for i in range(actualNumber-1):
                    if character == 'g':
                        finalMessage.append('t')
                    elif character == 't':
                        finalMessage.append('g')
                    elif character == 'x':
                        finalMessage.append('c')
                    elif character == 'z':
                        finalMessage.append('a')
                        
                isNumber = False
                    
            if character == 'g':
                finalMessage.append('t')
            elif character == 't':
                finalMessage.append('g')
            elif character == 'x':
                finalMessage.append('c')
            elif character == 'z':
                finalMessage.append('a')
            elif character.isdigit():
                actualNumber = int(character)
                isNumber = True
                
                
        str1 = ''.join(finalMessage)
        print(str1)
        


m1 = AttackCleanup()
m1.restore_data('gtxgtxzg3z8g4txz3g3z')


"""
number = False
actualNumber = 0
for loop message
    while number:
        for i in actualNumber:
            if characterEncoded:
                list.append(appendChatacterDecodedinList)
        number = False
    if characterCoded:
        appendCharacterDecodeinList
    elif number:
        number = true:
        

#move to sc/uc repository after monday and then delete this comment 

"""
