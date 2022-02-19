;Multiplications, divisions - Unsigned  representation
;ex. 27: (100+a+b*c)/(a-100)+e+x/a; a,b-byte; c-word; e-doubleword; x-qword
bits 32 
global start

extern exit
import exit msvcrt.dll 

segment data use32 class=data
    a db 7Fh
    b db 24h
    c dw 3456h
    e dd 7890ABCDh
    x dq 123456789h 

    res1 dd 0
    res2 dd 0
    
segment code use32 class=code
start:
    
    mov eax, 0
    mov ebx, 0
    mov ecx, 0
    mov edx, 0
    
    mov bx, 100h    ; BX = 100h
    add bl, [a]     ; BX = BX+ a = 100h + 7F = 17Fh
    mov al, [b]     ; AL = b = 24h
    mov ah, 0
    mov cx, [c]     ; CX = c = 3456h
    mul cx          ; DX: AX = AX * CX = 24h * 3456h = 7 5C18h
    
    push dx
    push ax
    pop ebx
    mov [res1], ebx ; res1 = (100+a+b*c) = 7 5C18h
    
    mov eax, 0
    mov ebx, 0
    mov ecx, 0
    mov edx, 0
    
    mov al, [a]    ; AL = a = 7Fh
    mov ah, 0
    sub eax, 100h  ; EAX = EAX - 100h = FFFF FF7fh
    mov [res2], ax  ; res2 = a-100 = FF7fh
    
    mov eax, 0
    mov ecx, 0
    mov edx, 0
    mov eax, [res1]
    mov ecx, [res2]
    div ecx         ; EAX = EDX:EAX / ECX = (100+a+b*c)/(a-100) = 7 5C18h / FF7Fh = 7
    
    mov ebx, 0
    mov ebx, [e]
    add eax, ebx   ; EAX = EAX + EBX = (100+a+b*c)/(a-100) + e = 7 + 7890ABCDh = 7890 ABD4h
    mov ebx, eax
    
    mov eax, 0
    mov edx, 0
    mov ecx, 0
    mov eax, dword[x+0]
    mov edx, dword[x+4]
    
    mov cl, [a]        ;CL = a = 7Fh
    
    
    idiv ecx   ; EAX = EDX:EAX / ECX = 1 23456789h / 7Fh = 24B 2111h
               ; EAX = EDX:EAX % ECX = 1 23456789h % 7Fh = 1Ah
               ; EAX = x/a = 24B 2111h
    
    mov edx, 0
    add eax, ebx  ; EAX = EAX + ebx = x/a + (100+a+b*c)/(a-100)+e = 24B 2111h + 7890 ABD4h = 7ADB CCE5

    
    push dword 0 
    call [exit]