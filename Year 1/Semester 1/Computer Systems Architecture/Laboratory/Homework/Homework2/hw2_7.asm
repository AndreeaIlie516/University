; Multiplications, divisions: a,b,c - byte, d - word, ex. 12: a*[b+c+d/b]+d
bits 32 
global start

extern exit
import exit msvcrt.dll 

segment data use32 class=data
    a db 12
    b db 6
    c db 7
    d dw 129


segment code use32 class=code
start:
; ...
    mov ax, 0
    mov bx, 0
    mov dx, 0
    
    mov dl, [b] ; DX = b = 6
    add dl, [c] ; DX = (b + c) = 6 + 7 = 13
    
    mov ax, [d] ; AX = d = 129
    mov bl, [b] ; BL = b = 6
    div bl      ; AL = AX / BL = d / b = 129 / 6 = 21 , ah = ax % b = d % b = 129 % 6 = 3
     
    mov bx, 0
    mov bl, al  ; use BL to store only AL in BX, not AX (AL and AH)
    add dx, bx  ; DX = DX + BX = (b + c) + d / b = 13 + 21 = 34 
    
    mov ax, 0
    mov ax, dx  ; AX = DX = (b + c) + d / b = 34
    
    ;mov ebx, 0
    
    mul byte [a] ; AX = AL * a = a * [b + c + d / b] = 12 * 34 = 408
    
    ;push dx
    ;push ax
    ;pop ebx
    
    add ax, [d] ; AX = AX + d = a * [b + c + d / b] + d = 408 + 129 = 537
    
    
    
    
    
    push dword 0 
    call [exit] 