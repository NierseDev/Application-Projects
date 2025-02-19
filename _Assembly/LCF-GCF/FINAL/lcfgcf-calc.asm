section .data
    ; Prompt Messages
    title db "==== LCM and GCF CALCULATOR by YourName and YourName2 ====", 0
    lcm_title db "====Least Common Multiple====", 10, 0
    gcf_title db "====Greatest Common Factor====", 10, 0
    lcm_result db "LCM: %d", 10, 0
    gcf_result db "GCF: %d", 10, 0
    choice_prompt db "Enter choice: ", 10, \
                     "[0] Exit", 10, \
                     "[1] LCM", 10, \
                     "[2] GCF", 10, 0
    err_invalid_input db "Inputs should only be between 1 to 99. Please enter your valid inputs.", 10, 0
    prompt db "Enter the 3 two-digit numbers (separated by space): ", 0
    exit_prompt db "Enter '0' to exit or any other number to continue: ", 0
    choice_error db "Entered choice is not on the menu. Please enter a valid choice.", 10, 0

section .bss
    ; Input Variables
    num1 resd 4
    num2 resd 4
    num3 resd 4
    result resd 1
    choice resd 1

section .text
    ; External Functions
    extern _printf, _scanf

    ; Main Program
    global _main

_main:
    ; Initialize Stack Frame
    call init_stack_frame

    ; Display Welcome Message
    push title
    call _printf
    add esp, 4

main_loop:
    ; Display Choice Prompt
    push choice_prompt
    call _printf
    add esp, 4

    ; Fetch User Choice
    push choice
    push "%d"
    call _scanf
    add esp, 8
    mov eax, [choice]
    cmp eax, 0
    je exit_program
    cmp eax, 1
    je calculate_lcm
    cmp eax, 2
    je calculate_gcf
    jmp invalid_choice

calculate_lcm:
    ; Calculate LCM
    push lcm_title
    call _printf
    add esp, 4

    call read_numbers
    mov eax, [num1]
    mov ebx, [num2]
    call lcm2
    mov [result], eax
    push eax
    push lcm_result
    call _printf
    add esp, 8
    jmp main_loop

calculate_gcf:
    ; Calculate GCF
    push gcf_title
    call _printf
    add esp, 4

    call read_numbers
    mov eax, [num1]
    mov ebx, [num2]
    mov ecx, [num3]
    call gcf
    mov [result], eax
    push eax
    push gcf_result
    call _printf
    add esp, 8
    jmp main_loop

invalid_choice:
    ; Display Choice Error
    push choice_error
    call _printf
    add esp, 4
    jmp main_loop

exit_program:
    ; Exit Program
    mov eax, 1
    mov ebx, 0
    int 0x80

read_numbers:
    ; Read Input
    push prompt
    call _printf
    add esp, 4

    push num1
    push num2
    push num3
    push "%d %d %d"
    call _scanf
    add esp, 16

    ; Validate Input
    mov eax, [num1]
    cmp eax, 1
    jl invalid_input
    cmp eax, 99
    jg invalid_input

    mov ebx, [num2]
    cmp ebx, 1
    jl invalid_input
    cmp ebx, 99
    jg invalid_input

    mov ecx, [num3]
    cmp ecx, 1
    jl invalid_input
    cmp ecx, 99
    jg invalid_input

    ret

invalid_input:
    ; Display Invalid Input
    push err_invalid_input
    call _printf
    add esp, 4
    jmp read_numbers

init_stack_frame:
    ; Initialize Stack Frame
    ret

lcm2:
    ; LCM of two numbers a, b = LCM(a, b) = a * b / GCF(a, b)
    mov edx, eax
    imul ebx, eax   ; a * b / GCF(a, b)
    mov eax, ebx
    mov edx, 0
    div dword [num2] ; a / GCF(a, b) * b = LCM(a, b)
    ret

gcf:
    ; GCF of three numbers a, b, c
    ; Parameters are passed by reference
    mov eax, [ebp+8]
    mov ebx, [ebp+12]
    call gcf2
    mov ecx, [ebp+16]
    mov [result], eax
    mov eax, ecx
    call gcf2
    ret

gcf2:
    ; GCF of two numbers a, b using Euclidean algorithm
    mov edx, 0

gcf_loop:
    cmp ebx, 0
    je gcf_done
    div ebx
    mov eax, ebx
    mov ebx, edx
    jmp gcf_loop
    
gcf_done:
    ret
