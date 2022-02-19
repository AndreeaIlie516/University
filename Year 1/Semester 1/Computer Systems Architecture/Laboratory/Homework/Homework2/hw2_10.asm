; Multiplications, divisions: a,b,c,d-byte, e,f,g,h-word, ex. 28: (e+g-h)/3+b*c
bits 32 
global start

extern exit
import exit msvcrt.dll 

segment data use32 class=data
    a db 13
    b db 7
    c db 24
    d db 10
    
    e dw 121
    f dw 135
    g dw 235
    h dw 142


segment code use32 class=code
start:
; ...
    
    mov ax, 0
    mov ax, [e]   ; AX = e = 121
    add ax, [g]   ; AX = AX + g = e + g = 121 + 235 = 356
    sub ax, [h]   ; AX = AX - h = e + g - h = 356 - 142 = 214

    mov dx, 0
    mov dl, 3
    div byte dl    ; Al = AX / 3 = (e + g - h) / 3 = 214 / 3 = 71
                   ; AH = AH % 3 = (e + g - h) % 3 = 214 % 3 =  1 
                  
    mov bx, 0
    mov bl, al     ; use BL to store only AL in BX, not AX (AL and AH)
                  
    mov ax, 0
    mov al, [b]    ; AL = AL + b = 7
    mul byte [c]   ; AX = AL * c = b * c = 7 * 24 = 168
    
    add bx, ax     ; BX = BX + AX = (e+g-h)/3+b*c = 71 + 168 = 239

    
    
    push dword 0 
    call [exit] 