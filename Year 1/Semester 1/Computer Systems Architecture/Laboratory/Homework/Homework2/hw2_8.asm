; Multiplications, divisions: a,b,c - byte, d - word, ex. 28: d+10*a-b*c
bits 32 
global start

extern exit
import exit msvcrt.dll 

segment data use32 class=data
    a db 24
    b db 12
    c db 10
    d dw 235


segment code use32 class=code
start:
; ...
    
    mov ax, 0
    mov bx, 0
    mov dx, 0
    mov al, 10
    mul byte [a]   ; AX = AL * a = 10 * a = 10 * 24 = 240
    mov bx, ax     ; BX = AX = 10*a = 240
    
    
    mov al, [b]    ; AL = b = 12
    mul byte [c]   ; AX = AL * c = b * c = 12 * 10 = 120
    
    mov dx, [d]    ; DX = d = 235
    add dx, bx     ; DX = DX + BX = d + 10*a = 235 + 240 = 475
    sub dx, ax     ; DX = DX - AX = d + 10*a - b*c = 475 - 120 = 355 
    
    
    
    push dword 0 
    call [exit] 