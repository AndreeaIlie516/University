;Additions, subtractions: a - byte, b - word, c - double word, d - qword - Unsigned representation
;ex. 27: (a+c)-(d+b)
bits 32 
global start

extern exit
import exit msvcrt.dll 

segment data use32 class=data
    a db 12h
    b dw 3456h
    c dd 7890abcdh
    d dq 1122334455667788h 
    carry db 0h

segment code use32 class=code
start:
    
    mov eax, 0
    mov ebx, 0
    mov ecx, 0
    mov edx, 0
    mov al, [a]    ; AL = a = 12h
    mov ah, 0      ; unsigned conversion from al to ax
    mov dx, 0
    add eax, [c]   ; EAX = EAX + c = a + c = 12h + 7890 ABCDh = 7890 ABDFh; CF = 0

    mov ebx, dword[d+0]  ; EBX = 5566 7788h
    mov ecx, dword[d+4]  ; ECX = 1122 3344h
   
    clc
    mov dx, [b]
    add ebx, edx   ; EBX = EBX + b = 5566 7788h + 3456h = 5566 ABDEh; CF = 0
    adc ecx, 0      ; ECX = ECX + CF = ECX + 0 = 1122 3344h


    mov edx = 0
    sub eax, ebx   ; EAX = EAX - EBX = 7890 ABDFh - 5566 ABDEh = 232A 0001h; CF = 0
    sbb edx, ecx   ; EDX = EDX - EDX = 0h - 1122 3344h = EEDD CCBCh
    
    push dword 0  
    call [exit] 
