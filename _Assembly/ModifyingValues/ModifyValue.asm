section		.text
global		_start
_start:
	;Writing Name: 'Zara Ali'
	mov edx,9
	mov ecx,name
	mov ebx,1
	mov eax,4
	int 0x80
	
	;Modifying the Initial Value
	mov [name],dword 'Nuha'
	
	;Writing Modified Name: 'Nuha Ali'
	mov edx,8
	mov ecx,name
	mov ebx,1
	mov eax,4
	int 0x80
	
	;Exit
	mov eax,1
	int 0x80
section		.data
name		db 'Zara Ali '
