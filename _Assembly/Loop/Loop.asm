section 	.text
global		_start
_start:
	mov edx,len
	mov ecx,msg
	mov ebx,1
	mov eax,4
	int 0x80
	
	mov edx,126
	mov ecx,s2
	mov ebx,1
	mov eax,4
	int 0x80
	
	mov eax,1
	int 0x80
section		.data
msg		db 'Displaying "Hello, World!" 9 Times',0xa
len 		equ $ - msg
s2 		times 9 db 'Hello, World! '
