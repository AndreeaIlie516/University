;Additions, subtractions: a - byte, b - word, c - double word, d - qword - Signed representation
;ex. 12:(a-b-c)+(d-b-c)-(a-d)
bits 32 
global start

extern exit
import exit msvcrt.dll 

segment data use32 class=data
    a db 12h
    b dw 3456h
    c dd 7890abcdh
    d dq 1122334455667788h 

    res1 dd 0
    res2 dd 0
    res3 dd 0
    res4 dd 0
    res5 dd 0
    res6 dd 0
    res7 dd 0
    res8 dd 0
    
segment code use32 class=code
start:
    
    mov eax, 0
    mov edx, 0
    mov al, [a]   ; AL = a = 12h
    cbw           ; Converts the byte AL to the word AX in the signed interpretation
    sub ax, [b]   ; AX = AX + b = 12h - 3456h = CBBC; C = 1
    cwde
    sub eax, [c]  ; EAX = EAX - c = FFFF CBBC - 7890ABCDh = 876F 1FEFh; C = 1
    cdq           ; EDX = FFFF FFFFh
    mov [res1], edx  ; res1 = FFFF FFFFh
    mov [res2], eax  ; res2 = 876F 1FEFh
    
    mov eax, 0
    mov edx, 0
    mov ebx, 0
    mov ecx, 0
    mov eax, dword[d+0]   ; EAX = 5566 7788h
    mov bx, [b]           ; BX = b = 3456h
    sub eax, ebx          ; EAX = EAX - EX = 5566 7788h - 3456h = 55664332
    cdq                   ; EDX = 0000 0000h
    add edx, dword[d+4]   ; EDX = 0000 0000h + 1122 3344h = 1122 3344h
    mov [res3], edx       ; res3 = 1122 3344h
    mov [res4], eax       ; res4 = 5566 4332h
    mov edx, 0
    mov ecx, [c]          ; ECX = 7890 ABCDh
    sub eax, ecx          ; EAX = EAX - ECX = 5566 4332h - 7890 ABCDh = DCD5 9765h
    cdq                   ; EDX = FFFF FFFFh
    add edx, [res3]       ; EDX = EDX + res3 = FFFF FFFFh + 1122 3344 = 1122 3343h
    mov [res3], edx       ; res3 = EDX = 1122 3343h
    mov [res4], eax       ; res4 = EAX = DCD5 9765h
    
    mov eax, 0
    mov ebx, 0
    mov ecx, 0
    mov edx, 0
    mov eax, [res2]       ; EAX = res2 = 876F 1FEFh
    mov ebx, [res4]       ; EBX = res4 = DCD5 9765h
    add eax, ebx          ; EAX = EAX + EBX = res2 + res 4 = 876F 1FEFh + DCD5 9765h = 6444 B754h
    cdq                   ; EDX = 0000 0000h
    adc edx, [res1]       ; EDX = 0000 0000h + FFFF FFFFh + CF = 0000 0000h
    add edx, [res3]       ; EDX = 0000 0000h + 11223343 = 1122 3343h
    
    mov [res5], edx       ; res5 = 1122 3343h
    mov [res6], eax       ; res6 = 6444 B754h
    
    
    
    mov eax, 0
    mov edx, 0
    mov ebx, 0
    mov ecx, 0
    mov ebx, dword[d+0]   ; EBX = 5566 7788h
    mov ecx, dword[d+4]   ; ECX = 1122 3344h
    
    mov al, [a]   ; AL = a = 12h
    cbw           ; Converts the byte AL to the word AX in the signed interpretation
    cwd
    cwde
    sub eax, ebx  ; EAX = EAX - EBX = 0000 0012h - 5566 7788h = AA99888A
    cdq           ; EDX = FFFF FFFFh
    sub edx, ecx  ; EDX = EDX - ECX = FFFF FFFFh - 1122 3344h = EEDD CCBBh
    mov [res7], edx   ; res7 = EDX = EEDD CCBBh
    mov [res8], eax   ; res8 = EAX = AA99 888Ah
    
    mov eax, 0
    mov ebx, 0
    mov ecx, 0
    mov edx, 0
    mov eax, [res6]  ; EAX = res6 = 6444 B754h
    sub eax, [res8]  ; EAX = EAX - res8 = 6444 B754h - AA99 888Ah = B9Ab 2ECAh
    cdq              ; EDX = FFFF FFFFh
    add edx, [res5]  ; EDX = FFFF FFFFh + 1122 3343h = 1122 3342h
    sub edx, [res7]  ; EDX = EDX - res7 = 1122 3342 - EEDD CCBBh = 2244 6687
    
   
    
    push dword 0 
    call [exit] 