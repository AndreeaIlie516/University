; Multiplications, divisions: a,b,c,d-byte, e,f,g,h-word, ex. 12: (a*d+e)/[c+h/(c-b)]
bits 32 
global start

extern exit
import exit msvcrt.dll 

segment data use32 class=data
    a db 13
    b db 7
    c db 24
    d db 10
    
    e dw 423
    f dw 135
    g dw 235
    h dw 142


segment code use32 class=code
start:
; ...
    
    mov ax, 0
    
    mov al, [a]   ; AL = a = 13
    mul byte [d]  ; AX = AL * d = 13 * 10 = 130
    
    add ax, [e]   ; AX = AX + e = a*d + e = 130 + 423 = 553
    mov bx, ax    ; BX = AX = a*d + e = 553
    
    mov ax, 0
    mov ax, [h]   ; AX = h = 142 
    
    mov dx, 0
    mov dl, [c]   ; DL = c = 24
    sub dl, [b]   ; DL = DL - b = c - b= 24 - 7 = 17
    
    div dl        ; AL = AX / DL = h / (c - b) = 142 / 17 = 8
                  ; AH = AX % DL = h % (c - b) = 142 % 17 = 6
                  
    mov dx, 0
    mov dl, al    ; use DL to store only AL in DX, not AX (AL and AH)
                  ; DL = AL = 8
    add dl, [c]   ; AX = AX + c = c + h / (c - b) = 24 + 8 = 32
    
    mov ax, 0
    mov ax, bx    ; AX = BX = a*d + e = 553
    div dl        ; AL = AX / DL = (a*d+e)/[c+h/(c-b)] = 553 / 32 = 17
                  ; AH = AX % DL = (a*d+e)%[c+h/(c-b)] = 553 % 32 = 17 = 9
    
    
    
    push dword 0 
    call [exit] 