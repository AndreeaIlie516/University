;Multi-modul programming (asm+asm)
;12.Two strings of characters of equal length are given. Calculate and ;display the results of the interleaving of the letters, for the two possible ;interlaces (the letters of the first string in an even position, ;respectively the letters from the first string in an odd positions). Where ;no character exist in the source string, the ‘ ’ character will replace it ;in the destination string.
bits 32 

global start        

extern exit,printf              
import exit msvcrt.dll    
import printf msvcrt.dll
extern interclasare   
        
segment data use32 class=data
    s1 db "acegi"     
    len equ $-s1 
    s2 db "bdfhj"     
    
    x times len+len dd ''        
    
    
segment code use32 class=code
    start:

        push dword s1
        push dword s2
        push dword len 
        push dword x
        call interclasare      
        add esp,4*4         
        
        
        push dword x
        call [printf]
        add esp,4
        
        
        push    dword 0
        call    [exit]       
     
