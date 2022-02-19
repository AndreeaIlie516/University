; Additions, subtractions: a,b,c,d: word, ex. 28: (d-c)+(b+b-c-a)+d
bits 32 
global start

extern exit
import exit msvcrt.dll 

segment data use32 class=data
    a dw 145
    b dw 203
    c dw 346
    d dw 425


segment code use32 class=code
start:
; ...
    mov dx, 0
    mov bx, 0
   
    mov dx, [d]  ; DX = a = 425
    sub dx, [c]  ; DX = DX - c = d - c = 425 - 346 = 79
    
    mov bx, [b]  ; BX = b = 203
    add bx, [b]  ; BX = BX + b = b + b = 203 + 203 = 406
    sub bx, [c]  ; BX = BX - c = b + b - c = 406 - 346 = 60
    sub bx, [a]  ; BX = BX - a = b + b - c - a = 60 - 145 = -85
    
    add dx, bx   ; DX = DX + BX = (d - c) + (b + b - c - a) = 79 + (-85) = -6
    add dx, [d]  ; DX = DX + d = (d - c) + (b + b - c - a) + d = -6 + 425 = 419
    
    
    push dword 0 
    call [exit] 