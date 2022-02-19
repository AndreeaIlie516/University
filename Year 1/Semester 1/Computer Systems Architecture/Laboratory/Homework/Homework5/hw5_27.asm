; Comparison instructions, conditional jumps, loop instructions. String operations.
; 27. Two byte strings S1 and S2 of the same length are given. Obtain the string D where each element is the difference of the corresponding elements from S1 and S2
;Example:
;S1: 1, 3, 6, 2, 3, 2
;S2: 6, 3, 8, 1, 2, 5
;D: -5, 0, -2, 1, 1, -3
bits 32 
global start

extern exit
import exit msvcrt.dll 

segment data use32 class=data
    S1 db 1, 3, 6, 2, 3, 2
    l1 equ $-S1
    S2 db 6, 3, 8, 1, 2, 5
    l2 equ $-S2
    D times l1+l2 dw 0
    
segment code use32 class=code
start:
    
    mov ecx, 0
    mov esi, 0
    mov eax, 0
    mov ebx, 0
    mov edx, 0
    
    mov ecx, l1      ; ecx = the length of s1
    
    mov esi, 0
    
    mov edi, 0

    
    jecxz end_loop      ; jump to end_loop if ecx is 0
    
    loop1:
        mov eax, 0
        mov ebx, 0
        mov al, [S1+esi]    ;  al = s1[esi]
        mov bl, [S2+esi]    ;  bl = s2[esi]
        cbw
        sub ax, bx          ;  ax = ax - bx
        mov [D+edi], ax     ;  D[edi] = AX 
        inc esi             ;  ESI = ESI + 1
        inc edi             ;  EDI = EDI + 1
    loop loop1              ;  ECX = ECX - 1
    
    end_loop
    
    push dword 0 
    call [exit]