;Multiplications, divisions - Signed representation
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
    
segment code use32 class=code
start:
    
    mov eax, 0
    mov ebx, 0
    mov ecx, 0
    mov edx, 0
    
    mov bx, 100h ; BX = BX + 100h = 100h
    add bl, byte[a]  ; BX=BX+a=100h+7Fh = 17Fh
    
    mov al, [b]  ; AL = AL + b = 24h
    cbw          ; Converts the byte AL to the word AX in the signed interpretation
    cwd          ; Converts the word AX to the dword DX:AX in the signed interpretation
    mul word[c]  ; DX: AX = AX * c = 24h * 3456h => AX = 5C18; DX = 7h
    
    add ax, bx   ; AX = AX + BX = 5C18h + 17Fh = 5D97
    ; adc dx, 0    ; DX = DX + CF = 7h + 0h = 7h
    
    push dx
    push ax
    pop eax      ; EAX = 0007 5D97h
    mov ebx, eax ; EBX = 0007 5D2970
    
    mov eax, 0
    mov al, [a]  ; AL = a = 7Fh
    cbw          ; Converts the byte AL to the word AX in the signed interpretation

    sub ax, 100h  ; AX = AX - 100h = a - 100 = 7Fh - 100h = FF7Fh
    cwde          ; Converts the word AX to the dword EAX in the signed interpretation
    mov cx, ax  ; CX = AX = FF7Fh
    
    mov eax, ebx  ; EAX = EBX = 0007 5D97h
    cdq           ; ; Converts the dword EAX to the qword EDX:EAX in the signed interpretation
    
    idiv ecx       ; EAX = EDX:EAX  / ECX = 0007 5D97h / FF7Fh = 7
                   ; EDX = EDX:EAX % ECX = 0007 5D97h % FF7Fh = 611Eh
              
    
    mov ebx, 0
    mov ebx, [e]   ; EBX = EBX + e = 7890 ABCDh
    add eax, ebx   ; EAX = EAX + EBX = 7h + 7890 ABCDh = 7890 ABD4h
    mov [res1], eax ;   res1 = 7890 ABd4h
    
    mov eax, 0
    mov ebx, 0
    mov ecx, 0
    mov edx, 0

    mov al, [a]         ; AL = a = 7Fh
    cbw                 ; Converts the byte AL to the word AX in the signed interpretation            
    cwde                ; Converts the word AX to the dword EAX in the signed interpretation
    
    mov ecx, eax
    mov eax, 0
    mov eax, dword[x+0]  ; EAX = 23456789h
    mov edx, dword[x+4]  ; EDX = 1h
    
    idiv ecx   ; EAX = EDX:EAX / ECX = 1 23456789h / 7Fh = 24B 2111h
               ; EAX = EDX:EAX % ECX = 1 23456789h % 7Fh = 1Ah
               ; EAX = x/a = 24B 2111h
    
    mov edx, 0
    add eax, [res1]  ; EAX = EAX + res1 = x/a + (100+a+b*c)/(a-100)+e = 24B 2111h + 7890 ABD4h = 7ADB CCE5
    ; adc edx, 0       ; EDX = EDX + CF = 0h
    
    
    
    
    push dword 0 
    call [exit]