bits 32

global interclasare   

segment data use32 class=data
    x resd 20      ; we need an auxiliary string to help us interleave the two passed as parameters

segment code use32 class=code
interclasare:
    
    mov esi,[esp+16]    ; esi = the first string passed as a parameter 
    mov edi,0           ; edi = 0, we want to add its elements onto even positions (0,2,..)
    mov ecx,[esp+8]     ; ecx = len 
        
    loop1:         ; here we add the elements from the first string passed as a parameter (esp+16) into the result string, on even positions.
        lodsb
        mov [x+edi],al          ; x[even_positions] = element from the first string
        add edi,2               ; skip the odd positions
    loop loop1
            
    mov esi,[esp+12]   ; now esi = the second string passed as a parameter 
    mov edi,1           ; edi = 1, we want to add its elements onto odd positions (1,3,..)
    mov ecx,[esp+8]     ; ecx = len
    
    loop2:        ; here we add the elements from the second string passed as a parameter (esp+16) into the result string, on odd positions.
        lodsb 
        mov [x+edi],al         ; x[odd_positions] = element from the second string
        add edi,2              ; skip the even positions
    loop loop2
        
    dec edi 
    mov [x+edi],dword 10  ; we add the end line character to the end of the string 
    mov [esp+4],dword x   ; we add it onto the stack, in the place of the parameter before the call
    
    ret                   ; we return, and now onto the stack at +4 we have our required string
    