# -*- coding: utf-8 -*-
"""
Created on Sun May 27 13:25:42 2018

@author: broch
"""

import os
all_files = os.listdir('./') # Lista todos os itens na pasta onde está o Script.

executaveis = ['.exe' , '.msi']
imagens = ['.jpeg', '.jpg', '.tiff', '.gif', '.bmp', '.png', '.PNG', '.bpg', '.svg', '.heif', '.psd']
documentos = ['.txt', '.epub', '.pages', '.docx', '.doc', '.fdf', '.ods','.odt','.xps', '.dotx', '.docm', '.dox','.xls', '.xlsx', '.ppt','.pptx']
pdfs = ['.pdf']
compactados = ['.rar','.zip','.7z','.bzip2','.gzip','.tar','.wim','.xz',]
scripts = ['.ahk', '.py']

# NOMES DAS PASTAS A SEREM CRIADAS CASO SEJA NECESSÁRIO
EXECUTAVEIS_FOLDER = './Executaveis/'
IMAGES_FOLDER = './Imagens/'
DOC_FOLDER = './Documentos/'
PDF_FOLDER = './Pdfs/'
COMPACT_FOLDER = './Compactados/'
SCRIPT_FOLDER = './Scripts/'

print('Brock Organiser - Python [Version.1 - May 27, 2018]')
print()
print('Lista de arquivos e pastas encontrados:')
print()
# Printa todos arquivos e pastas que foram encontrados
for i in range(0, len(all_files)):
    print('{}'.format(all_files[i]))
print()

for i in all_files:
    # ------ Arquivos Executáveis ------------------------------------------
    if str(i[i.rfind('.'):]) in executaveis: # str(i[i.rfind('.'):]) --- Retira a extensão do arquivo # verifica se essa extenção está em 'executáveis'
        print('\tfoi movido << {} >>'.format(i)) # Printa a ação que foi realizada
        if not os.path.exists(EXECUTAVEIS_FOLDER): # Verifica se a pasta existe
            os.makedirs(EXECUTAVEIS_FOLDER) # Cria Pasta, caso ainda não exista
        os.rename(os.path.join('./', i) , os.path.join(EXECUTAVEIS_FOLDER, i)) # move o arquivo
        continue # Já moveu o arquivo, então não precisa realizar os outros 'if' abaixo, pode voltar para o inicio do 'For'
    
    # ------ Arquivos Imagens ------------------------------------------
    if str(i[i.rfind('.'):]) in imagens: # str(i[i.rfind('.'):]) --- Retira a extensão do arquivo # verifica se essa extenção está em 'imagens'
        print('\tfoi movido << {} >>'.format(i))  # Printa a ação que foi realizada
        if not os.path.exists(IMAGES_FOLDER): # Verifica se a pasta existe
            os.makedirs(IMAGES_FOLDER) # Cria Pasta, caso ainda não exista
        os.rename(os.path.join('./', i) , os.path.join(IMAGES_FOLDER, i)) # move o arquivo
        continue # Já moveu o arquivo, então não precisa realizar os outros 'if' abaixo, pode voltar para o inicio do 'For'
    
    # ------ Arquivos Documentos ------------------------------------------
    if str(i[i.rfind('.'):]) in documentos: # str(i[i.rfind('.'):]) --- Retira a extensão do arquivo # verifica se essa extenção está em 'imagens'
        print('\tfoi movido << {} >>'.format(i))  # Printa a ação que foi realizada
        if not os.path.exists(DOC_FOLDER): # Verifica se a pasta existe
            os.makedirs(DOC_FOLDER) # Cria Pasta, caso ainda não exista
        os.rename(os.path.join('./', i) , os.path.join(DOC_FOLDER, i)) # move o arquivo
        continue # Já moveu o arquivo, então não precisa realizar os outros 'if' abaixo, pode voltar para o inicio do 'For'

    # ------ Arquivos Pdfs ------------------------------------------
    if str(i[i.rfind('.'):]) in pdfs: # str(i[i.rfind('.'):]) --- Retira a extensão do arquivo # verifica se essa extenção está em 'executáveis'
        print('\tfoi movido << {} >>'.format(i)) # Printa a ação que foi realizada
        if not os.path.exists(PDF_FOLDER): # Verifica se a pasta existe
            os.makedirs(PDF_FOLDER) # Cria Pasta, caso ainda não exista
        os.rename(os.path.join('./', i) , os.path.join(PDF_FOLDER, i)) # move o arquivo
        continue # Já moveu o arquivo, então não precisa realizar os outros 'if' abaixo, pode voltar para o inicio do 'For'

    # ------ Arquivos Compactados ------------------------------------------
    if str(i[i.rfind('.'):]) in compactados: # str(i[i.rfind('.'):]) --- Retira a extensão do arquivo # verifica se essa extenção está em 'executáveis'
        print('\tfoi movido << {} >>'.format(i)) # Printa a ação que foi realizada
        if not os.path.exists(COMPACT_FOLDER): # Verifica se a pasta existe
            os.makedirs(COMPACT_FOLDER) # Cria Pasta, caso ainda não exista
        os.rename(os.path.join('./', i) , os.path.join(COMPACT_FOLDER, i)) # move o arquivo
        continue # Já moveu o arquivo, então não precisa realizar os outros 'if' abaixo, pode voltar para o inicio do 'For'

    # ------ Arquivos Scripts ------------------------------------------
    if str(i[i.rfind('.'):]) in scripts: # str(i[i.rfind('.'):]) --- Retira a extensão do arquivo # verifica se essa extenção está em 'executáveis'
        print('\tfoi movido << {} >>'.format(i)) # Printa a ação que foi realizada
        if not os.path.exists(SCRIPT_FOLDER): # Verifica se a pasta existe
            os.makedirs(SCRIPT_FOLDER) # Cria Pasta, caso ainda não exista
        os.rename(os.path.join('./', i) , os.path.join(SCRIPT_FOLDER, i)) # move o arquivo
        continue # Já moveu o arquivo, então não precisa realizar os outros 'if' abaixo, pode voltar para o inicio do 'For'

print()
print('Arquivos organizados! =)')





# -*- coding: utf-8 -*-
"""
Created on Sun May 27 13:25:42 2018

Last Update: July 03, 2018

@author: broch
"""

import os
all_files = os.listdir('./') # Lista todos os itens na pasta onde está o Script.

# Extensões do arquivos a serem organizados
executaveis = ['.exe' , '.msi']
imagens = ['.jpeg', '.jpg', '.tiff', '.gif', '.bmp', '.png', '.PNG', '.bpg', '.svg', '.heif', '.psd']
documentos = ['.txt', '.epub', '.pages', '.docx', '.doc', '.fdf', '.ods','.odt','.xps', '.dotx', '.docm', '.dox','.xls', '.xlsx', '.ppt','.pptx']
pdfs = ['.pdf']
compactados = ['.rar','.zip','.7z','.bzip2','.gzip','.tar','.wim','.xz',]
scripts = ['.ahk', '.py']

# NOMES DAS PASTAS A SEREM CRIADAS CASO SEJA NECESSÁRIO
EXECUTAVEIS_FOLDER = './Executaveis/'
IMAGES_FOLDER = './Imagens/'
DOC_FOLDER = './Documentos/'
PDF_FOLDER = './Pdfs/'
COMPACT_FOLDER = './Compactados/'
SCRIPT_FOLDER = './Scripts/'

print('Brock Organiser - Python [Version.2 - July 03, 2018]')
print()
print('Lista de arquivos e pastas encontrados:')
print()
# Printa todos arquivos e pastas que foram encontrados
for i in range(0, len(all_files)):
	print('{}'.format(all_files[i]))
print()

def organizer(file_folder, cont_for): #cont_for contador do for
	if not os.path.exists(file_folder): # Verifica se a pasta existe
        os.makedirs(file_folder) # Cria Pasta, caso ainda não exista
    os.rename(os.path.join('./', cont_for) , os.path.join(file_folder, cont_for)) # move o arquivo
    print('\tfoi movido << {} >>'.format(cont_for)) # Printa a ação que foi realizada
    return
	

for i in all_files:
    # ------ Arquivos Executáveis ------------------------------------------
    if str(i[i.rfind('.'):]) in executaveis: # str(i[i.rfind('.'):]) --- Retira a extensão do arquivo # verifica se essa extenção está em 'executáveis'
        organizer(EXECUTAVEIS_FOLDER,i)
        continue # Já moveu o arquivo, então não precisa realizar os outros 'if' abaixo, pode voltar para o inicio do 'For'
    
    # ------ Arquivos Imagens ---------------------------------------------
    if str(i[i.rfind('.'):]) in imagens: # str(i[i.rfind('.'):]) --- Retira a extensão do arquivo # verifica se essa extenção está em 'imagens'
        organizer(IMAGES_FOLDER,i)
        continue # Já moveu o arquivo, então não precisa realizar os outros 'if' abaixo, pode voltar para o inicio do 'For'
    
    # ------ Arquivos Documentos ------------------------------------------
    if str(i[i.rfind('.'):]) in documentos: # str(i[i.rfind('.'):]) --- Retira a extensão do arquivo # verifica se essa extenção está em 'imagens'
        organizer(DOC_FOLDER,i)
        continue # Já moveu o arquivo, então não precisa realizar os outros 'if' abaixo, pode voltar para o inicio do 'For'

    # ------ Arquivos Pdfs ------------------------------------------------
    if str(i[i.rfind('.'):]) in pdfs: # str(i[i.rfind('.'):]) --- Retira a extensão do arquivo # verifica se essa extenção está em 'executáveis'
        organizer(PDF_FOLDER,i)
        continue # Já moveu o arquivo, então não precisa realizar os outros 'if' abaixo, pode voltar para o inicio do 'For'

    # ------ Arquivos Compactados ------------------------------------------
    if str(i[i.rfind('.'):]) in compactados: # str(i[i.rfind('.'):]) --- Retira a extensão do arquivo # verifica se essa extenção está em 'executáveis'
        organizer(COMPACT_FOLDER,i)
        continue # Já moveu o arquivo, então não precisa realizar os outros 'if' abaixo, pode voltar para o inicio do 'For'

    # ------ Arquivos Scripts ----------------------------------------------
    if str(i[i.rfind('.'):]) in scripts: # str(i[i.rfind('.'):]) --- Retira a extensão do arquivo # verifica se essa extenção está em 'executáveis'
        organizer(SCRIPT_FOLDER,i)
        continue # Já moveu o arquivo, então não precisa realizar os outros 'if' abaixo, pode voltar para o inicio do 'For'

print()
print('Arquivos organizados! =)')


