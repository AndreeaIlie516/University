;Additions, subtractions: a - byte, b - word, c - double word, d - qword - Unsigned representation
;ex. 28: d-(a+b)+(c+c)
bits 32 
global start

extern exit
import exit msvcrt.dll 

segment data use32 class=data
    a db 12h
    b dw 3456h
    c dd 7890abcdh
    d dq 1122334455667788h 
    carry dd 0

segment code use32 class=code
start:
    
    mov eax, 0
    mov al, [a]    ; AL = a = 12h
    mov ah, 0      ; unsigned conversion from al to ax
    mov dx, 0
    add ax, [b]    ; AX = AX + b = 12h + 3456h = 3468h; CF = 0
    
    mov ebx, 0
    mov ecx, 0
    mov ebx, dword[d+0]  ; EBX = 5566 7788h
    mov ecx, dword[d+4]  ; ECX = 1122 3344h
    
    adc ecx, 0     ; ECX = ECX + CF = 1122 3344h + 0 = 1122 3344h
    clc
    sub ebx, eax   ; EBX = EBX - EAX = 5566 7788h - 0000 3468h = 5566 4320; CF = 0
    sbb ecx, 0     ; ECX = ECX - CF = 1122 3344h - 0 = 1122 3344h
    
    mov eax, 0




    push dword 0 
    call [exit] 
