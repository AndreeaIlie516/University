; Instructions working on strings of bytes/words/doublewords/quadwords
;12. Given an array A of doublewords, build two arrays of bytes:  
; - array B1 contains as elements the lower part of the lower words from A
; - array B2 contains as elements the higher part of the higher words from A
bits 32 
global start

extern exit
import exit msvcrt.dll 

segment data use32 class=data 
    A dd 568B45ACh, 648AB536h, 9D536281h, 4581EF56h
    l equ ($-A)/4

    B1 times l db 0
    B2 times l db 0

    
segment code use32 class=code
start:
    
    mov esi, 0
    mov ecx, 0
    mov edx, 0
    mov eax, 0
    
    mov ecx, l    ; the length of the string A
    mov esi, A    ; the source string A
    
    Loop_:
        mov eax, 0
        lodsb   ; The byte from the address <DS:ESI> is loaded in AL (the lower part of the lower words from A): ACh, 36h, 81h, 56h
        
        mov[B1+edx], AL  ;Move in B1[edx] the byte stored in AL (the lower part of the lower words from A): ACh, 36h, 81h, 56h
        
        lodsw   ; The word from the address <DS:ESI> is loaded in AX
        
        lodsb   ; The byte from the address <DS:ESI> is loaded in AL (the higher part of the higher words from A) : 56h, 64h, 9Dh, 45h
        
        mov[B2+edx], AL  ; ;Move in B2[edx] the byte stored in AL (the higher part of the higher words from A) : 56h, 64h, 9Dh, 45h
        
        inc edx    ; increment EDX
    loop Loop_
    
    push dword 0 
    call [exit]