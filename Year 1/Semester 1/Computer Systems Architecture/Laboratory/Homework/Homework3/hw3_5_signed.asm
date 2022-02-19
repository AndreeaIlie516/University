;Multiplications, divisions - Signed representation
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
    
    res1 dw 0
    
segment code use32 class=code
start:
    
    mov eax, 0
    mov ebx, 0
    mov ecx, 0
    mov edx, 0
    
    mov al, [a]  ; AL = a = 24h
    cbw
    mov bx, [b]  ; BX = b = 3456h
    imul bx      ; DX:AX = AX * BX = a*b => AX = 5C18h, DX = 7h
    add ax, 2    ; AX = AX + 2h = 5C18 + 2 = 5C1Ah ; CF = 0
    adc dx, 0     ; DX = DX + CF = 7h + 0h = 7h
                  ; DX:AX = a*b + 2 = 7 5C1Ah
    push dx
    push ax
    pop ebx ;EBX = a*b+2 = 7 5C1Ah

    
    mov eax, 0
    mov ecx, 0
    mov edx, 0
    mov al, [a]  ; AL = a = 24h
    cbw
    add ax, 7    ; AX = AX + 7h = a+7h = 24h+7h = 2Bh
    mov dx, ax   ; DX = AX = a+7h = 24h+7h = 2Bh
    mov eax, 0
    mov al, [c]  ; AL = c = 12h
    cbw
    mov cx, ax   ; CX = AX = c = 12h
    sub dx, cx   ; DX = DX - CX = a +7h - c = 2Bh - 12h = 19h
    mov ecx, 0
    mov cx, dx   ; CX = DX = a +7h - c = 19h
    mov eax, 0
    push ebx 
    pop ax
    pop dx
    idiv cx      ; AX = DX:AX / CX = (a*b+2)/(a+7-c) = 7 5C1Ah / 19h = 4B5Dh
                 ; AX = DX:AX % CX = 7 5C1Ah % 19h = 5h
    cwde
    
    mov ebx, 0
    mov ebx, [d] ; EDX = EDX + d = 7890 ABCDh
    add eax, ebx ; EAX = EAX + EBX = (a*b+2)/(a+7-c) + d = 4B5Dh + 7890 ABCDh = 7890 F72Ah
    
    mov ebx, 0
    mov ecx, 0
    mov edx, 0
    mov ebx, dword[x+0] ; EBX = EBX + 55667788h
    mov ecx, dword[x+4] ; ECX = ECX + 11223344h
    add eax, ebx        ; EAX = EAX + EBX = 7890 F72A + 55667788h = CDF7 6EB2h ; CF = 0
    adc edx, ecx        ; EDX = EDX + ECX + CF = 0h + 11223344h + 0h = 11223344h
    
    
    push dword 0 
    call [exit] 