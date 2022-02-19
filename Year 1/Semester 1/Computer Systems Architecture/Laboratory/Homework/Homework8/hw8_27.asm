; Text file operation
; 27. A text file is given. The text file contains numbers (in base 10) separated by spaces. Read the content of the file, determine the minimum number (from the numbers that have been read) and write the result at the end of file.

; The following code will open a file called "ana.txt" from current folder,
; it will read maximum 100 characters from this file,
; and it will display to the console the number of chars and the text we've read.

; The program will use:
; - the function fopen() to open/create the file
; - the function fread() to read from file
; - the function printf() to display a text
; - the function fclose() to close the created file.

; Because the fopen() call uses the file access mode "r", the file will be open for
; reading. The file must exist, otherwise the fopen() call will fail.
; For details about the file access modes see the section "Theory".

; Any string used by printf() must be null-terminated ('\0').

bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fread, fclose, fopen, printf, fprintf
               ; tell nasm that exit exists even if we won't be defining it
import fread msvcrt.dll
import fclose msvcrt.dll
import fopen msvcrt.dll
import printf msvcrt.dll
import fprintf msvcrt.dll

import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
	file_name DB "numbers.txt", 0   ; filename to be read
	file_descriptor dd -1           ; variable to hold the file descriptor
	access_mode DB "r+", 0          ; file access mode
	number DB 0
	aux DD 0
	f DD '%d', 0
	formatnew DD '%c', 0
	mini DD 0FFFFh
	ten DD 10	
	newline DD 10

; our code starts here
segment code use32 class=code
    start:
        ; call fopen() to create the file
        ; fopen() will return a file descriptor in the EAX or 0 in case of error
        ; eax = fopen(file_name, access_mode)
		push dword access_mode
		push dword file_name
		call [fopen]
		add ESP, 2 * 4      ; clean-up the stack
        
		mov [file_descriptor], EAX  ; store the file descriptor returned by fopen
        
        ; check if fopen() has successfully created the file (EAX != 0)
        cmp EAX, 0
		je final
        
        
		mov EBX, 0
		mov EAX, 0
		Loop_:
        
            ; read the text from file using fread()
            ; after the fread() call, EAX will contain the number of chars we've read 
            ; eax = fread(text, 1, len, file_descriptor)
			push dword[file_descriptor]
			push 1
			push 1            ;len
			push number
			call [fread]
			add ESP, 4 * 4    ; clean-up the stack
            
            ; check if fopen() has successfully created the file (EAX != 0)
			cmp EAX, 0
			je final
			add ESP, 2 * 4    ; clean-up the stack
            
			mov AX, BX
			cmp byte[number], ' '  ; verify if it is space
			jne notspace           ; if it is not space, jumpt to notspace, otherwise continue
			cmp BX, word[mini]     
			ja notmini             ; if BX > mini jump to notmini, otherwise continue
			mov dword[mini], EAX   ; mini = EAX
			mov EAX, 0
			mov EBX, 0
			mov word[number], '0'  ; number = '0'
			jmp notmini
			notspace:
				sub dword[number], '0'    ; transform the character into the decimal
				mul dword[ten]
				add EAX, dword[number]    ; EAX = number
				mov EBX, EAX              ; EBX = EAX = number
			notmini:
			jmp Loop_              ; continue the loop
		final:
		cmp BX, word[mini]         
		ja notmini2                ; if BX > mini jump to notmini2, otherwise continue
		mov [mini], EBX            ; mini = EBX
		notmini2:
        
        ; append the newline to file using fprintf()
        ; fprintf(file_descriptor, newline)
		push dword[newline]
		push formatnew
		push dword[file_descriptor]
		call [fprintf]
		add ESP, 2 * 4        ; clean-up the stack
        
        ; append the number to file using fprintf()
        ; fprintf(file_descriptor, number)
		push dword[mini]
		push f
		push dword[file_descriptor]
		call [fprintf]
		add ESP, 2 * 4        ; clean-up the stack
		
        ; call fclose() to close the file
        ; fclose(file_descriptor)
		push dword[file_descriptor]
		call [fclose]

		
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program