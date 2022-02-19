;Bitwise operations
;ex. 27: Given the quadword A, obtain the integer number N represented on the bits 35-37 of A. Then obtain the the doubleword B by rotating the low doubleword of A N positions to the right. Obtain the byte C as follows:
;       the bits 0-3 of C are the same as the bits 8-11 of B
;       the bits 4-7 of C are the same as the bits 16-19 of B
bits 32 
global start

extern exit
import exit msvcrt.dll 

segment data use32 class=data
    a dq 1001_1101_1011_1110_1101_1001_1110_1011_1011_1000_0000_0000_1111_1101_1001_0111b
    n db 0
    b dd 0
    c db 0
    
segment code use32 class=code
start:
    
    mov eax, 0
    mov ebx, 0
    mov ecx, 0
    mov edx, 0
    
    mov eax, dword[a+0]
    mov edx, dword[a+4]
    mov ebx, 0000_0000_0011_1000b
    and edx, ebx
    ror edx, 3
    mov [n], dl   ; the integer number N represented on the bits 35-37 of A
    
    mov cl, 0
    mov cl, [n]
    ror eax, cl   ; totate N positions to the right
    mov [b], eax  ; dubleword B
    
    mov ebx, 0
    mov ecx, 0
    mov cx, 0000_0000_0000_0000_0000_1111_0000_0000b    
    mov ebx, [b]
    and ebx, ecx     ; the bits 8-11 of B
    mov ecx, 0
    mov cl, 8
    ror ebx, cl     ;  the bits 0-3 of C are the same as the bits 8-11 of B
    mov [c], ebx
    
    mov ebx, 0
    mov ecx, 0
    mov cx, 0000_0000_0000_1111_0000_0000_0000_0000b    
    mov ebx, [b]
    and ebx, ecx     ; the bits 16-19 of B
    mov ecx, 0
    mov cl, 12
    ror ebx, cl     ;  the bits 4-7 of C are the same as the bits 16-19 of B
    
    mov ecx, [c]
    or ecx, ebx
    mov [c], ecx

    
    push dword 0 
    call [exit]