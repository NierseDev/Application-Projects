_start:
	mov edx,14
	mov ecx,msg
	mov ebx,1
	mov eax,4
	int 0x80
	mov eax,1
msg		db 'Hello, World!', 0xa
