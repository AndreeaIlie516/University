; Additions, subtractions: a,b,c,d: byte, ex. 28: a+b-c+d
bits 32 
global start

extern exit
import exit msvcrt.dll 

segment data use32 class=data
    a db 8
    b db 10
    c db 9
    d db 5


segment code use32 class=code
start:
; ...
    mov ax, 0
    
    mov al, [a]   ; AL = a = 8
    add al, [b]   ; AL = AL + b = a + b = 8+10 = 18
    sub al, [c]   ; AL = AL - c = a + b - c = 18 - 9 = 9 
    add al, [d]   ; Al = AL + d = a + b - c +d = 9 + 5 = 14
    

    push dword 0 
    call [exit] 