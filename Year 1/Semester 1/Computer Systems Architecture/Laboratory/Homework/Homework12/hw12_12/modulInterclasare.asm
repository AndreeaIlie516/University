bits 32

extern _citireSirC

extern _printf

global _asmInterclasare

segment data public data use32
    lenRez                dd        0
    x     dd        0
    sir1        dd        0
    sir2        dd        0
    
segment code public code use32

_asmInterclasare:
    
    push ebp
    mov ebp, esp
    
    ;sub esp, 4 * 3  

    mov edx, [ebp+20]
   
    mov esi,[ebp+12]    ; esi = the first string passed as a parameter 
    mov edi,0           ; edi = 0, we want to add its elements onto even positions (0,2,..)
    mov ecx,[ebp+8]     ; ecx = len 
        
    loop1:         ; here we add the elements from the first string passed as a parameter (esp+16) into the result string, on even positions.
        lodsb
        mov [edx+edi],al          ; x[even_positions] = element from the first string
        add edi,2               ; skip the odd positions
    loop loop1
            
    mov esi,[ebp+16]   ; now esi = the second string passed as a parameter 
    mov edi,1           ; edi = 1, we want to add its elements onto odd positions (1,3,..)
    mov ecx,[ebp+8]     ; ecx = len
    
    loop2:        ; here we add the elements from the second string passed as a parameter (esp+16) into the result string, on odd positions.
        lodsb 
        mov [edx+edi],al         ; x[odd_positions] = element from the second string
        add edi,2              ; skip the even positions
    loop loop2
        
    dec edi 
    mov [edx+edi],dword 10  ; we add the end line character to the end of the string 
  
    
    mov [ebp+20], edx
    mov esp, ebp
    pop ebp
    
    ret                   ; we return, and now onto the stack at +4 we have our required string
    