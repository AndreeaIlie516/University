;Additions, subtractions: a - byte, b - word, c - double word, d - qword - Signed representation
;ex. 27: (d+d-c)-(c+c-a)+(c+a)
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
    
    mov eax, dword[d+0] ; EAX = EAX + 55667788h = 55667788h
    mov edx, dword[d+4] ; EDX = EDX + 11223344h = 11223344h
    mov ebx, dword[d+0] ; EBX = EBX + 55667788h = 55667788h
    mov ecx, dword[d+4] ; ECX = ECX + 11223344h = 11223344h
    add eax, ebx        ; EAX = EAX + EBX = 55667788h + 55667788h = AACCEF10h; CF = 0
    adc edx, ecx        ; EDX = EDX + ECX + CF = 11223344h + 11223344h + 0 = 22446688h
                        ; EDX: EAX = d + d
    sub eax, [c]        ; EAX = EAX - c = AACCEF10h = 7890ABCDh = 323C4343h
    sbb edx, 0          ; EDX = EDX - CF = 22446688h - 0 = 22446688h
                        ; EDX:EAX = (d + d - c)
     
    clc     
    mov ebx, 0
    mov ecx, 0
    
    mov cl, [a]
    mov ebx, [c]        ; EBX = EBX + c = 7890ABCDh
    add ebx, [c]        ; EBX = EBX + c = c + c = 7890ABCDh + 7890ABCDh = F121579Ah ; CF = 0

    sub ebx, ecx        ; EBX = EBX - ECX = c + c - a = F121579Ah - 12h = F1215788h
    
    sub eax, ebx        ; EAX = EAX - ECX = 323C4343h - F1215788h = 411A EBBBh; CF = 1
    sbb edx, 0          ; EDX = EDX - CF = 22446688h - 1h = 22446687h
    
    
   
    
    push dword 0 
    call [exit] 