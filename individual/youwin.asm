section .text
global main
extern scanf

main:
  mov rax, 1
  mov rdi, 1
  mov rsi, message
  mov rdx, 28
  syscall

  push rax
  push rcx

  mov rdi, format
  mov rsi, buff

  call scanf

  pop rcx
  pop rax

  xor rbx, rbx
enc:
  mov rdx, buff
  add rdx, rbx
  mov byte al, [rdx]
  xor al, 0x27

  mov rdx, encbuff
  add rdx, rbx

  mov byte [rdx], al

  inc rbx
  cmp rbx, 13
  jne enc

  xor rbx, rbx
iseq:
  mov rdx, enctext
  add rdx, rbx
  mov byte al, [rdx]

  mov rdx, encbuff
  add rdx, rbx

  mov byte cl, [rdx]

  cmp al, cl
  jne end

  inc rbx
  cmp rbx, 13
  je win

  jmp iseq

win:
  mov rax, 1
  mov rdi, 1
  mov rsi, winmessage
  mov rdx, 8
  syscall

end:
  mov rax, 60
  xor rdi, rdi
  syscall

section .data
message: db `welcome to the ground floor\n`,27
format: db '%13s\n',6
enctext: db 074h, 06ch, 07eh, 0ah, 066h, 074h, 06ah, 065h, 0ah, 013h, 01fh, 015h, 01eh
winmessage: db `You win\n`,8

section .bss
buff: resb 14
encbuff: resb 14
