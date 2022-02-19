; Instructions working on strings of bytes/words/doublewords/quadwords
; 27. Being given a string of words, compute the longest substring of ordered words (in increasing order) from this string.
; A: 1234h, 1567h, 1007h, 2345h, 2678h, 2000h
; B: 1007h, 2345h, 2678h
bits 32 
global start

extern exit
import exit msvcrt.dll 

segment data use32 class=data 
    A dw 1234h, 1567h, 1007h, 2345h, 2678h, 2000h
    l equ ($-A)/2

    B times l dw 0    
    max dw 0
    start_pos dw 0
    end_pos dw 0
    startt dw 0
    endd dw 0
    

    
segment code use32 class=code
start:
    
    mov esi, 0
    mov ecx, 0
    mov edx, 0
    mov eax, 0
    mov ebx, 0
    
    mov ecx, l    ; the length of the string A
    mov esi, A    ; the source string A
    
    mov edx, 1    ; index
    For_loop:
        mov ax, word[esi]           ; AX = ESI[index] <=> v[i]
        cmp ax, word[esi+1]         ; compare the current element in the string with the next one <=> v[i] ? v[i+1]
       
        jnl final                   ; if ax not less than [ESI+1] jump to final <=> else (if (v[i] > v[i+1]))
        jle sequence                ; if ax less or equal than [ESI+1] jump to sequence <=> if (v[i] <= v[i+1])
        
        sequence:
            mov [startt], dx        ; save the index in startt (the starting point of the current sequence)
            push ecx                ; save ecx
            While_loop:             ; loop <=> while v[i] <= v[i+1] && i<n
                mov ax, word[esi]   ; AX = ESI[index] <=> v[i]
                cmp ax, word[esi+1] ; compare the current element in the string with the next one <=> v[i] ? v[i+1]
                jnl final1          ; if ax not less than [ESI+1] jump to final1 <=> else (if (v[i] > v[i+1]))
                
                jle sequence2       ; if ax less or equal than [ESI+1] jump to sequence2 <=> if (v[i] <= v[i+1])
                sequence2:
                    inc dx          ; increment the index
                    mov [endd], dx  ; save the index in endd (the ending point of the current sequence)
                
                add esi, 2          ; increment ESi (DW)
            loop While_loop         ; end of loop
            pop ecx                 ; exctract the saved ecx
            final1:
                mov bx, [ endd]     ; save in bx the dimension of the sequence (endd - start + 1)
                sub bx, [startt]
                inc bx
                cmp bx, [max]       ; compare bx with max <=> (end - start + 1 ? max)
                
                jng stop            ; if bx is not greater than max <=> else (if (end - start + 1 < max)
                jge attr            ; if bx is greater or equal than max <=> if (end - start + 1 >= max)
                
                attr:
                    mov [max], bx   ; max = BX = endd - startt + 1 (the maximum length of a sequence)
                    mov bx, 0
                    mov bx, [startt]
                    mov [start_pos], bx ; start_pos = BX = startt (the starting point of the maximum sequence)
                    mov bx, 0
                    mov bx, [endd]
                    mov [end_pos], bx   ; end_pos = BX = endd (the ending point of the maximum sequence)
                 
            stop:
            
        final:
            add esi, 2              ; increment ESi (DW)
            
    loop For_loop                   
    
    mov ecx, l                      ; the length of the string A
    
    mov edx, 0                      ; index
    
    mov esi, A                      ; the source string A
    mov edi, B                      ; the destination string B
    
    mov ebx, 0
    
    For_loop2                       ; loop for saving the maximum increasing sequence in B
        cmp dx, [start_pos]         ; compare the index with the starting position of the sequence
        jl continue                 ; if dx less than start_pos jump to continue <=> else( if (index < start_pos))
        jle continue1               ; if dx greater or equal than start_pos jump to continue <=>  if (index >= start_pos)
        continue1: 
            cmp dx, [end_pos]       ; compare the index with the ending position of the sequence
            jg continue             ; if dx greater end_pos jump to continue <=> else( if (index > end_pos))
            jle move                ; if dx less or equal than start_pos jump to move <=>  if (index <= end_pos)
            move:
                mov ax, word[esi]   ; AX = ESI[index]
                mov [B+edx+edx], AX ; B[index] = AX
        
        continue:
            inc edx                 ; increment index
            add esi, 2              ; increment ESi (DW)

    loop For_loop2
    
    
    push dword 0 
    call [exit]