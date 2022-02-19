;Multiplications, divisions - Unsigned representation
;ex. 12: (a*b+2)/(a+7-c)+d+x; a,c-byte; b-word; d-doubleword; x-qword
bits 32 
global start

extern exit
import exit msvcrt.dll 

segment data use32 class=data
    a db 24h
    b dw 3456h
    c db 12h
    d dd 7890ABCDh
    x dq 1122334455667788h 

    
segment code use32 class=code
start:
    
    mov eax, 0
    mov ebx, 0
    mov ecx, 0
    mov edx, 0
    
    mov al, [a]   ; AL = a = 24h
    mov bx, [b]   ; BX = b = 3456h
    mul word bx   ; DX: AX = AX * BX = a*b = 24*3456 => AX = 5C18; DX = 7
    add ax, 2    ; AX = AX + 2h = 5C18 + 2 = 5C1Ah ; CF = 0
    adc dx, 0     ; DX = DX + CF = 7h + 0h = 7h
                  ; DX:AX = a*b + 2 = 7 5C1Ah
                  
    mov ebx, 0
    mov bl, [a]   ; BL = a = 24h
    add bl, 7     ; BL = BL + 7 = a + 7h = 24h + 7h = 2Bh
    adc Bh, 0     ; BH = BH + CF = 0h + 0h = 0h
    mov cl, [c]   ; CL = c = 12h
    sub bx, cx    ; BX = BX - CX = a + 7 - c = 2Bh - 12h = 19h
    
    div bx        ; AX = DX:AX / BX = 0007 5C1Ah / 19h = 4B5Dh
                  ; DX = DX:AX % BX = 0007 5C1Hh % 19h = 5h
                  
    mov edx, 0
    mov ebx, [d]  ; EBX = EBX + d = 7890ABCDh
    add eax, ebx  ; EAX = EAX + EBX = 4B5Dh + 7890ABCDh = 7890 F72Ah
    adc edx, 0    ; EDX = EDX + CF = 0h
    
    mov ebx, 0
    mov ecx, 0
    mov ebx, dword[x+0] ; EBX = EBX + 55667788h
    mov ecx, dword[x+4] ; ECX = ECX + 11223344h
    add eax, ebx        ; EAX = EAX + EBX = 7890 F72A + 55667788h = CDF7 6EB2h ; CF = 0
    adc edx, ecx        ; EDX = EDX + ECX + CF = 0h + 11223344h + 0h = 11223344h
    
    push dword 0 
    call [exit] 