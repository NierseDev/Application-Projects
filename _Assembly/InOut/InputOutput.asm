section		.data
	usrMsg db 'Please enter a number: '
	lenUsrMsg equ $-usrMsg
	dispMsg db 'You have entered: '
	lenDispMsg equ $-dispMsg
section		.bss
	num resb 5
section		.text
	global _start
_start:
	mov eax,4
	mov ebx,1
	mov ecx,usrMsg
	mov edx,lenUsrMsg
	int 80h
	
	;Read and Store the User Input
	mov eax,3
	mov ebx,2
	mov ecx,num
	mov edx,5
	int 80h
	
	;Output the Number
	mov eax,4
	mov ebx,1
	mov ecx,dispMsg
	mov edx,lenDispMsg
	int 80h
	
	mov eax,4
	mov ebx,1
	mov ecx,num
	mov edx,5
	int 80h
	
	;Exit
	mov eax,1
	mov ebx,0
	int 80h

