section .data
    prompt db "Enter the 3 two-digit numbers (separated by space): ", 0
    invalid_input db "Inputs should only be between 1 to 99. Please enter your valid inputs.", 10, 0
    lcm_result db "LCM: %d", 10, 0
    gcf_result db "GCF: %d", 10, 0
    exit_prompt db "Enter '0' to exit or any other number to continue: ", 0
    choice_prompt db "==== LCM and GCF CALCULATOR by YourName and YourName2 ====[0] Exit[1] LCM[2] GCFEnter choice: ", 0
    choice_error db "Entered choice is not on the menu. Please enter a valid choice.", 10, 0
    welcome_message db "Hi! This is YourName and YourName2 and I am here to help you determine the LCM and GCF for three positive two-digit numbers (1 to 99).", 10, 0

section .bss
    num1 resd 1
    num2 resd 1
    num3 resd 1
    result resd 1
    choice resd 1

section .text
    extern _printf, _scanf
    global _main

; Main Program
_main:
    call init_stack_frame

    ; Display welcome message
    push welcome_message
    call _printf
    add esp, 4

main_loop:
    push choice_prompt
    call _printf
    add esp, 4

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
    call read_numbers
    ; Calculate LCM (Pass-by-Value)
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
    call read_numbers
    ; Calculate GCF (Pass-by-Reference)
    lea eax, [num1]
    lea ebx, [num2]
    lea ecx, [num3]
    call gcf
    mov [result], eax
    push eax
    push gcf_result
    call _printf
    add esp, 8
    jmp main_loop

invalid_choice:
    push choice_error
    call _printf
    add esp, 4
    jmp main_loop

exit_program:
    mov eax, 1
    mov ebx, 0
    int 0x80

read_numbers:
    push prompt
    call _printf
    add esp, 4

    push num1
    push num2
    push num3
    push "%d %d %d"
    call _scanf
    add esp, 16

    mov eax, [num1]
    cmp eax, 1
    jl input_error
    cmp eax, 99
    jg input_error

    mov eax, [num2]
    cmp eax, 1
    jl input_error
    cmp eax, 99
    jg input_error

    mov eax, [num3]
    cmp eax, 1
    jl input_error
    cmp eax, 99
    jg input_error

    ret

input_error:
    push invalid_input
    call _printf
    add esp, 4
    jmp read_numbers

lcm2:
    ; LCM of three numbers a, b, c = LCM(LCM(a, b), c)
    push ebx
    push ecx

    ; Calculate LCM(a, b)
    mov edx, eax
    imul ebx, eax   ; a * b / GCF(a, b)
    mov eax, ebx
    mov edx, 0
    div dword [num2] ; a / GCF(a, b) * b = LCM(a, b)
    mov ebx, eax

    ; Calculate LCM(LCM(a, b), c)
    mov edx, eax
    imul ecx, eax   ; LCM(a, b) * c / GCF(LCM(a, b), c)
    mov eax, ecx
    mov edx, 0
    div dword [num3] ; LCM(LCM(a, b), c) = LCM(a, b) * c / GCF(LCM(a, b), c)

    pop ecx
    pop ebx
    ret

gcf:
    ; Calculate GCF of three numbers a, b, c
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
    ; Calculate GCF of eax and ebx using Euclidean algorithm
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

init_stack_frame:
    ; Initialize stack frame
    mov ebp, esp
    sub esp, 4
    ret


