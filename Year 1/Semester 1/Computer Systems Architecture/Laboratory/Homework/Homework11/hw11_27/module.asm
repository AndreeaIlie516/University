bits 32

global module  

extern exit,printf,scanf              
import exit msvcrt.dll    
import printf msvcrt.dll
import scanf msvcrt.dll 

segment data use32 class=data
    x resd 100      
    y resd 100

segment code use32 class=code
module:
    
    mov esi,[esp+12]    ; esi = the string passed as a parameter 
    mov edx, 0
    mov edx, esi
    mov edi,0           
    
    ;mov ecx, [esp+16]
    mov eax, 0
    loop1:
        ;mov eax, 0
        lodsb
        cmp eax, 0
        je final
        mov ebx, 0
        mov bl, 61h
        cmp al, bl
        jl continue
            
        mov bl, 7Ah
        cmp al, bl
        jg continue
        mov [x+edi],al
        inc edi            
        continue:
            jmp loop1
    ;loop loop1    
        final:
        ;dec edi 
    mov [x+edi], byte 10
    ;mov [esp+8],dword x 
    
    ;mov ecx, [esp+16]
    mov edi, 0
    mov esi, 0
    mov esi, edx
    loop2:        
        lodsb
        cmp eax, 0
        je final2
        mov ebx, 0
        mov bl, 41h
        cmp al, bl
        jl continue2 
        
        mov bl, 5Ah
        cmp al, bl
        jg continue2
            
        mov [y+edi],al
        inc edi            
        continue2:
            jmp loop2
                
    ;loop loop2
        final2:
              
    mov [y+edi],dword 10
    ;mov [esp+12],dword y 
    push dword x
    call [printf]
    add esp,4
        
    push dword y
    call [printf]
    add esp,4
    
    ret                  
    