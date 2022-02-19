;Additions, subtractions: a - byte, b - word, c - double word, d - qword - Unsigned representation
;ex. 12: (a+b+d)-(a-c+d)+(b-c)
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
    add ax, [b]    ; AX = AX + b = 12h + 3456h = 3468h
    
    mov ebx, 0
    mov ecx, 0
    mov ebx, dword[d+0]  ; EBX = 5566 7788
    mov ecx, dword[d+4]  ; ECX = 1122 3344
    
    clc;
    add ebx, eax   ; EBX = EBX + EAX = 5566 7788h + 3468h = 5566 ABF0h
    adc ecx, 0     ; ECX = 1122 3344h11 + CF = 1122 3344h
    
    clc
    mov eax, 0
    mov al, [a]    ; AL = a = 12h
    mov ah, 0      ; unsigned conversion from al to ax
    mov dx, 0 
    sbb eax, [c]   ; EAX = a - c = 12h - 7890abcdh = 876F 5445; CF = 1
    
    mov edx, 0
    mov edx, dword[d+4]  ; EDX = 1122 3344h
    sbb edx, 0           ; EDX = EDX - 0 - CF = 1122 3344h - 1 = 1122 3343h
    add eax, dword[d+0]  ; EAX = EAX + 5566 7788h = 876F 5445h + 5566 7788h = DCD5 CBCD; CF = 0
    adc edx, 0     ; EDX = EDX + 0 + CF = 1122 3343h + 0 = 1122 3343h
    
    clc
    sub ebx, eax   ; EBX = EBX - EAX = 5566 ABF0h - DCD5 CBCDh = 7890 E023h; CF = 1
    sbb ecx, edx   ; ECX = ECX - EDX - CF = 1122 3344h - 1122 3343 - 1 = 0
    
    clc
    mov eax, 0
    add ax, [b]    ; AX = AX + b = 3456h
    mov edx, 0
    mov edx, [c]   ; EDX = c = 7890abcdh
    sub eax, edx   ; EAX = EAX - EDX = 3456h - 7890abcdh = 876f 8889h; CF = 1
    
    sbb ecx, 0     ; ECX = ECX - 0 - CF = FFFF FFFFh
    add ebx, eax   ; EBX = EBX + EAX = 7890 E023h + 876F 8889h = 0000 68AC; CF = 1
    adc ecx, 0     ; ECX = ECX + CF = FFFF FFFFh + 1 = 0h




    push dword 0 
    call [exit] 

