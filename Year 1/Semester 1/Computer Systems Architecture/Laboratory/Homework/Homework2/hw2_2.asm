; Simple exercises: ex. 28: 13/5
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
    mov ax, 13  ; AX = 13
    mov bl, 5   ; DL = 5
    div bl      ; AL = AX / DL = 13 / 5 = 2 
                ; AH = AX % DL = 13 % 5 = 3
    

    push dword 0 
    call [exit] 