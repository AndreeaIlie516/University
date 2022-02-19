;Multi-modul programming (asm+asm)
;27. Read a sentence from the keyboard containing different characters (lowercase letters, big letters, numbers, special ones, etc). Obtain a new string with only the small case letters and another string with only the big case letters. Print both strings on the screen.
bits 32 

global start        

extern exit,printf,scanf              
import exit msvcrt.dll    
import printf msvcrt.dll
import scanf msvcrt.dll

extern module 
        
segment data use32 class=data
    string resb 20
    ;msg db "n=", 0
    ;msg2 db "The string is: ", 0
    ;format_number db "%d"
    ;n resb 1
    format db "%s", 0
    string1 db "245advABfsc"
    x resd 10      
    y resd 10
   
    
    
segment code use32 class=code
    start:

        push dword string
        push dword format
		call [scanf]       
		add esp, 4 * 2 
        
  
        ;push dword n
        push dword string
        push dword x
        push dword y
        call module     
        add esp,4*4         ; we clear the stack 
       
        
        push dword x
        call [printf]
        add esp,4
        
        push dword y
        call [printf]
        add esp,4
        
        
        push    dword 0
        call    [exit]       
     