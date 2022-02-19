; Functions calls
; A negative number a (a: dword) is given. Display the value of that number in base 10 and in the base 16 in the following format: "a = <base_10> (base 10), a = <base_16> (base 16)"
bits 32

global start        

extern exit,scanf,printf               
import exit msvcrt.dll    
import scanf msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data
    ; ...
    a dw 0

    read_a db "a=",0
    format db "%d",0            ; Attention! If we want to read hex numbers, %d becomes %x. In this format we can only read numbers in decimal
    print_format_base10 db "a=%d (base 10)         ", 0 ; definining the format
    print_format_base16 db "a=%x (base 16)", 0          ; definining the format
    
segment code use32 class=code
    start:

        ;"a="
        push dword read_a   ; ! on the stack is placed the address of the string, not its value       
        call [printf]       ; call function printf for printing
        add esp, 4          ; free parameters on the stack; 4 = size of dword; 1 = number of parameters
        
        ;read the value of a
        push dword a        ; ! address of a, not value
        push dword format
        call [scanf]        ; call function scanf for reading
        add esp, 4*2        ; free parameters on the stack
                            ; 4 = size of a dword; 2 = no of perameters
        
            
        push dword [a]              
        push dword print_format_base10  ; ! on the stack is placed the address of the string, not its value   
        call [printf]                   ; call function printf for printing          
        add esp,4*2                     ; free parameters on the stack; 4 = size of dword; 2 = number of parameters    
        
        
        push dword [a]        
        push dword print_format_base16  ; ! on the stack is placed the address of the string, not its value
        call [printf]                   ; call function printf for printing          
        add esp,4*2                     ; free parameters on the stack; 4 = size of dword; 2 = number of parameters
        
        push dword 0      
        call [exit]       