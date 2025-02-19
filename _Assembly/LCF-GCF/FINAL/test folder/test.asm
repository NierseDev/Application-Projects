section .data
    ; TITLE
	opening db "Hi! This is Mediado and Cuadra and We are here to help you perform operations for two-digit signed numbers (-99 to 99).", 10, 0
    title db "====SIMPLE CALCULATOR by Mediado and Cuadra====", 10, 0
    choiceprompt	db	"[0] Exit", 10, \
						"[1] LCM", 10, \
						"[2] GCF", 10, 0
    choice db "Enter choice: ", 0
	
	lcm_title db "====Least Common Multiple====", 10, 0
    gcf_title db "====Greatest Common Factor====", 10, 0

    ; INPUT FORMATTING
    input_format db "%d", 0
	num_format dd "%d %d %d", 0
    
    ; INPUTS
    num_inputs db "Enter the three numbers with space seperation (n1 n2 n3): ", 0
    
    ; OUTPUTS
	exit_msg db "Thank you!", 10, 0
	
    lcm_result db "LCM: %d", 10, 0
    gcf_result db "GCF: %d", 10, 0
    
    ; ERRORS
    choice_overflow db "Choice is out of range. Please try again!", 10, 0
    overflow_err db "Input should only be between -99 to 99. Please enter again a valid input.", 10, 0
    zerodiv_err db "You cannot divide by 0. Please enter again a valid divisor.", 10, 0

section .bss
    num1 resd 4			; Number 1
    num2 resd 4			; Number 2
	num3 resd 4			; Number 3
	input_choice resd 1	; Input Buffer
	result resd 1		; Result Buffer

section .text
    global _main
    extern _printf
    extern _scanf

; Display Function
title_display:
    push title
	call _printf
	add esp, 4
    push choiceprompt
	call _printf
	add esp, 4
	
	jmp main_loop

; Operation Choice Function
main_loop:
	; Fetch User Choice
    push choice
    call _printf
    add esp, 4
	
	push input_choice
    push input_format
    call _scanf
    add esp, 4
	
	; Compare the User Choice with the Options Available
    cmp dword [input_choice], 0
    je end_program
	
    cmp dword [input_choice], 1
    je calc_lcm
	
    cmp dword [input_choice], 2
    je calc_gcf
	
	; User Choice Validation
    mov eax, [input_choice]
    cmp eax, 2
    ja choice_outofrange
    cmp eax, 0
    jb choice_outofrange

    jmp main_loop

; User Choice Validation Function
choice_outofrange:
    push choice_overflow
    call _printf
    add esp, 4
    jmp main_loop


; Operations
calc_lcm:
	push lcm_title
	call _printf
	add esp, 4

	call read_num
	
    ; Calculate LCM (Pass-by-Value)
    mov eax, [num1]
    mov ebx, [num2]
    mov ecx, [num3]
    call lcm3

    mov [result], eax
    push eax
    push lcm_result
    call _printf
    add esp, 8
    jmp title_display

lcm3:
    ; LCM of three numbers a, b, c = LCM(LCM(a, b), c)
    push ebx
    push ecx

    ; Calculate LCM(a, b)
    mov edx, eax
    mul ebx
    mov eax, edx
    mov edx, 0
    div ebx
    mov ebx, eax

    ; Calculate LCM(LCM(a, b), c)
    mov eax, ebx
    mov ebx, ecx
    call gcf3
    mul ecx
    mov eax, ecx
    mov edx, 0
    div ebx

    pop ecx
    pop ebx
    ret

calc_gcf:
    ; Calculate GCF
    push gcf_title
    call _printf
    add esp, 4

    call read_num
	
    mov eax, [num1]
    mov ebx, [num2]
    mov ecx, [num3]
    call gcf3

    mov [result], eax
    push eax
    push gcf_result
    call _printf
    add esp, 8
    jmp title_display

gcf3:
    ; GCF of three numbers a, b, c
    push ecx
    call gcf
    mov ecx, eax
    pop eax
    call gcf
    ret

gcf:
    ; GCF of two numbers using Euclidean algorithm
    mov edx, 0

gcf_loop:
    test ebx, ebx
    je gcf_done
    xchg eax, ebx
    div ebx
    mov eax, ebx
    mov ebx, edx
    jmp gcf_loop

gcf_done:
    ret

read_num:
	push num_inputs
	call _printf
	add esp, 4
	
	push num1
	push num2
	push num3
	push num_format
	call _scanf
	add esp, 16
	
    mov eax, [num1]
    cmp eax, 1
    jl num_overflow_err
    cmp eax, 99
    jg num_overflow_err
	
    mov ebx, [num2]
    cmp ebx, 1
    jl num_overflow_err
    cmp ebx, 99
    jg num_overflow_err

    mov ebx, [num2]
    cmp ebx, 1
    jl num_overflow_err
    cmp ebx, 99
    jg num_overflow_err
	ret

; Overflow Errors for exceeding (-99 to 99)
num_overflow_err:
    push overflow_err
    call _printf
    add esp, 4
    jmp read_num

; Initialize Stack Frame
init_stack_frame:
    ret

; EXIT
end_program:
    push exit_msg
    call _printf
    add esp, 4
    ret

; MAIN
_main:
	call init_stack_frame

	push opening
	call _printf
	add esp, 4
	
    call title_display
	ret

section .data
    ; TITLE
	opening db "Hi! This is Mediado and Cuadra and We are here to help you perform operations for two-digit signed numbers (-99 to 99).", 10, 0
    title db "====SIMPLE CALCULATOR by Mediado and Cuadra====", 10, 0
    choiceprompt	db	"[0] Exit", 10, \
						"[1] LCM", 10, \
						"[2] GCF", 10, 0
    choice db "Enter choice: ", 0
	
	lcm_title db "====Least Common Multiple====", 10, 0
    gcf_title db "====Greatest Common Factor====", 10, 0

    ; INPUT FORMATTING
    input_format db "%d", 0
	num_format dd "%d %d %d", 0
    
    ; INPUTS
    num_inputs db "Enter the three numbers with space seperation (n1 n2 n3): ", 0
    
    ; OUTPUTS
	exit_msg db "Thank you!", 10, 0
	
    lcm_result db "LCM: %d", 10, 0
    gcf_result db "GCF: %d", 10, 0
    
    ; ERRORS
    choice_overflow db "Choice is out of range. Please try again!", 10, 0
    overflow_err db "Input should only be between -99 to 99. Please enter again a valid input.", 10, 0
    zerodiv_err db "You cannot divide by 0. Please enter again a valid divisor.", 10, 0

section .bss
    num1 resd 4			; Number 1
    num2 resd 4			; Number 2
	num3 resd 4			; Number 3
	input_choice resd 1	; Input Buffer
	result resd 1		; Result Buffer

section .text
    global _main
    extern _printf
    extern _scanf

; Display Function
title_display:
    push title
	call _printf
	add esp, 4
    push choiceprompt
	call _printf
	add esp, 4
	
	jmp main_loop

; Operation Choice Function
main_loop:
	; Fetch User Choice
    push choice
    call _printf
    add esp, 4
	
	push input_choice
    push input_format
    call _scanf
    add esp, 4
	
	; Compare the User Choice with the Options Available
    cmp dword [input_choice], 0
    je end_program
	
    cmp dword [input_choice], 1
    je calc_lcm
	
    cmp dword [input_choice], 2
    je calc_gcf
	
	; User Choice Validation
    mov eax, [input_choice]
    cmp eax, 2
    ja choice_outofrange
    cmp eax, 0
    jb choice_outofrange

    jmp main_loop

; User Choice Validation Function
choice_outofrange:
    push choice_overflow
    call _printf
    add esp, 4
    jmp main_loop


; Operations
calc_lcm:
	push lcm_title
	call _printf
	add esp, 4

	call read_num
	
    ; Calculate LCM (Pass-by-Value)
    mov eax, [num1]
    mov ebx, [num2]
    mov ecx, [num3]
    call lcm3

    mov [result], eax
    push eax
    push lcm_result
    call _printf
    add esp, 8
    jmp title_display

lcm3:
    ; LCM of three numbers a, b, c = LCM(LCM(a, b), c)
    push ebx
    push ecx

    ; Calculate LCM(a, b)
    mov edx, eax
    mul ebx
    mov eax, edx
    mov edx, 0
    div ebx
    mov ebx, eax

    ; Calculate LCM(LCM(a, b), c)
    mov eax, ebx
    mov ebx, ecx
    call gcf3
    mul ecx
    mov eax, ecx
    mov edx, 0
    div ebx

    pop ecx
    pop ebx
    ret

calc_gcf:
    ; Calculate GCF
    push gcf_title
    call _printf
    add esp, 4

    call read_num
	
    mov eax, [num1]
    mov ebx, [num2]
    mov ecx, [num3]
    call gcf3

    mov [result], eax
    push eax
    push gcf_result
    call _printf
    add esp, 8
    jmp title_display

gcf3:
    ; GCF of three numbers a, b, c
    push ecx
    call gcf
    mov ecx, eax
    pop eax
    call gcf
    ret

gcf:
    ; GCF of two numbers using Euclidean algorithm
    mov edx, 0

gcf_loop:
    test ebx, ebx
    je gcf_done
    xchg eax, ebx
    div ebx
    mov eax, ebx
    mov ebx, edx
    jmp gcf_loop

gcf_done:
    ret

read_num:
	push num_inputs
	call _printf
	add esp, 4
	
	push num1
	push num2
	push num3
	push num_format
	call _scanf
	add esp, 16
	
    mov eax, [num1]
    cmp eax, 1
    jl num_overflow_err
    cmp eax, 99
    jg num_overflow_err
	
    mov ebx, [num2]
    cmp ebx, 1
    jl num_overflow_err
    cmp ebx, 99
    jg num_overflow_err

    mov ebx, [num2]
    cmp ebx, 1
    jl num_overflow_err
    cmp ebx, 99
    jg num_overflow_err
	ret

; Overflow Errors for exceeding (-99 to 99)
num_overflow_err:
    push overflow_err
    call _printf
    add esp, 4
    jmp read_num

; Initialize Stack Frame
init_stack_frame:
    ret

; EXIT
end_program:
    push exit_msg
    call _printf
    add esp, 4
    ret

; MAIN
_main:
	call init_stack_frame

	push opening
	call _printf
	add esp, 4
	
    call title_display
	ret
