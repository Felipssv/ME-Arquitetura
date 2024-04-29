#Biblioteca pygame:
import pygame
print('Digite qualquer caractere para começar a conversão.')
pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

#Conversão de inteiro para bínário:
num = int(input('Digite um número inteiro para ser convertido em binário: '))
binario = str(bin(num)[2:])
print(f'O número {num}, ao ser convertido em binario fica: {binario}')
