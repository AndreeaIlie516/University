; Additions, subtractions: a,b,c,d: word, ex. 12: d-(a+b)-(c+c)
bits 32 
global start

extern exit
import exit msvcrt.dll 

segment data use32 class=data
    a dw 256
    b dw 124
    c dw 356
    d dw 548


segment code use32 class=code
start:
; ...
    mov dx, 0
    mov ax, 0
    mov bx, 0
    
    mov dx, [d]   ; DX = d = 548
    
    mov ax, [a]   ; AX = a = 256
    add ax, [b]   ; Ax = AX + b = a + b = 256 + 124 = 380
    
    mov bx, [c]   ; BX = 356
    add bx, [c]   ; BX = BX + c = 356 + 356 = 712
    
    sub dx, ax    ; DX = DX - AX = d - (a + b) = 548 - 380 = 168
    sub dx, bx    ; DX = DX - BX = d - (a + b) - (c + c) = 168 - 712 = -544
    

    push dword 0 
    call [exit] 