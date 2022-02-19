;Additions, subtractions: a - byte, b - word, c - double word, d - qword - Signed representation
;ex. 28: c+d-a-b+(c-a)
bits 32 
global start

extern exit
import exit msvcrt.dll 

segment data use32 class=data
    a db 12h
    b dw 3456h
    c dd 7890abcdh
    d dq 1122334455667788h 

segment code use32 class=code
start:
    
    mov eax, 0
    mov ebx, 0
    mov ecx, 0
    mov edx, 0
    
    mov ebx, [c]   ; EAX = c = 7890 ABCDh
    mov eax, dword[d+0]
    mov ecx, dword[d+4]
    
    add eax, ebx    ; EAX = EAX + ECX = 7890 ABCD + 5566 7788h = CDF7 2355
    cdq
    adc edx, ecx    ; EDX = EDX + CF + ECX = 0000 0000h + 0h + 1122 3344h = 1122 3344h
    




    push dword 0 
    call [exit] 
