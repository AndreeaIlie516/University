; Simple exercises: ex. 12: 4-5
bits 32 
global start

extern exit
import exit msvcrt.dll 

segment data use32 class=data


segment code use32 class=code
start:
; ...
    mov ax, 0
    mov bx, 0
    mov ax, 4    ; AX = 4
    mov bx, 5    ; BX = 5
    sub ax, bx   ; AX = AX - BX = 4 - 5 = -1
    
    


    push dword 0 
    call [exit] 

