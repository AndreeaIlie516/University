;Bitwise operations
;ex. 12: Given the words A and B, compute the doubleword C as follows:
;           the bits 0-6 of C have the value 0
;           the bits 7-9 of C are the same as the bits 0-2 of A
;           the bits 10-15 of C are the same as the bits 8-13 of B
;           the bits 16-31 of C have the value 1
bits 32 
global start

extern exit
import exit msvcrt.dll 

segment data use32 class=data
    a dw 1001_1101_1011_1110b
    b dw 0011_0011_1001_1101b
    c dd 0
    
segment code use32 class=code
start:
    
    mov ecx, 0
    and cx, 1111_1111_1000_0000b ; the bits 0-6 of C have the value 0
    
    mov eax, 0
    mov ebx, 0
    mov ax, [a]
    and ax, 0000_0000_0000_0111b ; the bits 0-2 of A
    mov bl, 7
    rol ax, 7   
    or cx, ax  ;the bits 7-9 of C are the same as the bits 0-2 of A
    
    mov eax, 0
    mov ax, [b]
    and ax, 0011_1111_0000_0000b
    mov bl, 2
    rol ax, 2
    or cx, ax
    
    mov eax, 0
    mov eax, 1111_1111_1111_1111_0000_0000_0000_0000b
    or ecx, eax
    mov [c], ecx
    
    
    
    push dword 0 
    call [exit]