; Comparison instructions, conditional jumps, loop instructions. String operations.
; 12. Two character strings S1 and S2 are given. Obtain the string D by concatenating the elements found on even positions in S2 and the elements found on odd positions in S1.
;S1: 'a', 'b', 'c', 'd', 'e', 'f'
;S2: '1', '2', '3', '4', '5'
;D:  '2', '4','a','c','e'
bits 32 
global start

extern exit
import exit msvcrt.dll 

segment data use32 class=data
    S1 db 'a', 'b', 'c', 'd', 'e', 'f'
    l1 equ $-S1
    S2 db '1', '2', '3', '4', '5'
    l2 equ $-S2
    D times (l2/2)+(l1/2) db 0
    
segment code use32 class=code
start:
    
    mov ecx, 0
    mov esi, 0
    mov eax, 0
    mov edx, 0
    
    mov ecx, l2/2 ; half of the dimension of S2
    
    mov esi, 1    ;the second position in the string(the first even position)
    
    mov edi, 0
    
    
    jecxz end_loop_s2       ; jump to end_loop_s2 if ecx is 0
    
    loop_s2:
        mov al, [S2+esi]    ; AL = S2[esi] = S2[even_position] 
        mov [D+edi], al     ; D[edi] = AL 
        add esi, 2          ; ESI = ESI + 2
        inc edi             ; EDI = EDI + 1
    loop loop_s2            ; ECX = ECX - 1
    
    end_loop_s2:

    mov ecx, 0
    mov ecx, l1/2  ; half of the dimension of S1
    
    mov esi, 0    ;the first position in the string(the first odd position)
    
    jecxz end_loop_s1  ; jump to end_loop_s1 if ecx is 0
    
    loop_s1:
        mov al, [S1+esi]    ; AL = S1[esi] = S1[odd_position]
        mov [D+edi], al     ; D[edi] = AL 
        add esi, 2          ; ESI = ESI + 2
        inc edi             ; EDI = EDI + 1
    loop loop_s1            ; ECX = ECX - 1
    
    end_loop_s1:
    
    push dword 0 
    call [exit]