section .data
    ; TITLE
    opening db "Hi! This is Hamzah Cuadra and We are here to help you perform operations for two-digit signed numbers (1 to 99).", 10, 0
    title db "====SIMPLE CALCULATOR by Hamzah Cuadra====", 10, 0
    choiceprompt db "[0] Exit", 10, \
                        "[1] LCM", 10, \
                        "[2] GCF", 10, 0
    choice db "Enter choice: ", 0

    lcm_title db "====Least Common Multiple====", 10, 0
    gcf_title db "====Greatest Common Factor====", 10, 0

    ; INPUT FORMATTING
    input_format db "%d", 0
    num_format db "%d %d %d", 0

    ; INPUTS
    num_inputs db "Enter three two-digit numbers with space separation (n1 n2 n3): ", 0

    ; OUTPUTS
    exit_msg db "Thank you!", 10, 0

    lcm_result db "LCM: %d", 10, 0
    gcf_result db "GCF: %d", 10, 0

    ; ERRORS
    choice_overflow db "Choice is out of range. Please try again!", 10, 0
    overflow_err db "Input should only be between 1 to 99. Please enter again a valid input.", 10, 0
    zerodiv_err db "You cannot divide by 0. Please enter again a valid divisor.", 10, 0

section .bss
    num1 resd 1         ; Number 1
    num2 resd 1         ; Number 2
    num3 resd 1         ; Number 3
    input_choice resd 1 ; Input Buffer
    result resd 1       ; Result Buffer

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
    add esp, 8

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

    push lcm_result
    call _printf
    add esp, 8
    ret

calc_gcf:
    push gcf_title
    call _printf
    add esp, 4

    call read_num

    push gcf_result
    call _printf
    add esp, 8
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

    mov ebx, [num3]
    cmp ebx, 1
    jl num_overflow_err
    cmp ebx, 99
    jg num_overflow_err
    ret

; Overflow Errors for exceeding (1 to 99)
num_overflow_err:
    push overflow_err
    call _printf
    add esp, 4
    jmp read_num

; EXIT
end_program:
    push exit_msg
    call _printf
    add esp, 4
    ret

; MAIN
_main:
    push opening
    call _printf
    add esp, 4

    call title_display
    ret


