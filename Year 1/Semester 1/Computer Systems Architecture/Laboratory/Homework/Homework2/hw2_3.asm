; Additions, subtractions: a,b,c,d: byte, ex. 12: 2-(c+d)+(a+b-c)
bits 32 
global start

extern exit
import exit msvcrt.dll 

segment data use32 class=data
    a db 2
    b db 4
    c db 3
    d db 7

segment code use32 class=code
start:
; ...
    mov ax, 0
    mov bx, 0
    mov dx, 0
    
    mov al, 2    ; AL = 2
    
    mov bl, [c]  ; BL = c = 3
    add bl, [d]  ; BL = c + d = 3 + 7 = 10
    
    mov dl, [a]  ; DL = a = 2
    add dl, [b]  ; DL = DL + b = a + b = 2 + 4 = 6
    sub dl, [c]  ; DL = DL + c = a + b - c = 6 - 3 = 3
    
    sub ax, bx   ; AL = AL - BL = 2 - (c + d) = 2 - 10 = -8
    add al, dl   ; AL = AL + DL = 2 - (c + d) + (a + b - c) = -8 + 3 = -5
    

    push dword 0 
    call [exit] 