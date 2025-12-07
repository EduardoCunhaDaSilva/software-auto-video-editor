
<img width="1080" height="1080" alt="Sem Título-121" src="https://github.com/user-attachments/assets/27e5121e-0ab4-42d0-b340-35223b7c883e" />


## 🎬 Video Toolkit: Editor e Conversor Simples com Python
**Status: 🚧 Em Construção**

Este projeto **oferece duas ferramentas** simples em Python para processamento de vídeo:

**Editor de Vídeo:** Detecta e corta silêncios automaticamente.

**Conversor:** Transforma vídeos .mov para o formato .mp4.

## 📦 1. Dependências e Instalação
Instale as bibliotecas Python necessárias usando pip:

Bash

pip install pydub moviepy

## 🧰 2. FFmpeg (Obrigatório)

* Ambos os scripts exigem que a ferramenta externa FFmpeg esteja instalada e acessível no seu sistema (no seu PATH).

* Verifique a instalação rodando no terminal:

* ffmpeg -version

## 📁 3. Nome dos arquivos

* video.mov
Arquivo de entrada original. Use esse nome para o vídeo .mov que será convertido para .mp4.

**Depois da conversão:**

* input.mp4
Renomeie o arquivo convertido para input.mp4. É esse arquivo que o script vai usar para fazer a edição.

 ## 🎧 4. Editor de Vídeo (Remove Silêncio)

 Arquivo: editor_video.py

**✨ Funcionalidade Detalhada**
O script automatiza o corte de pausas longas e silêncios.

* Lê o arquivo de entrada (input.mp4).

* Detecta trechos que contêm áudio.

* Corta e salva apenas as partes faladas/úteis.

* Gera arquivos temporários (part_X.mp4).

* Junta todas as partes no vídeo final.

## ▶️ Como Executar
**Pré-requisito:** O arquivo de entrada deve ser nomeado input.mp4.

rode: python editor_video.py

**Resultado:** O vídeo final sem silêncios será salvo como output.mp4.

## 🎥 5. Conversor MOV → MP4

Arquivo: conversor_mp4.py

**✨ Funcionalidade**
* Converte rapidamente vídeos .mov (comum em iPhones e Macs) para o formato .mp4, usando o codec H.264 + AAC para máxima compatibilidade.

**▶️ Como Executar** 
Pré-requisito: O arquivo de entrada deve ser nomeado video.mov

rode: python conversor_mp4.py

Resultado: O vídeo convertido será salvo como video_convertido.mp4.

## ❗ Avisos

**Tempo de Processamento:** O Editor de Vídeo precisa re-encodar cada trecho cortado, o que pode demorar. Não é um processo instantâneo.

**Tamanho dos Arquivos:** A qualidade do vídeo de entrada afeta o tamanho dos arquivos gerados (part_X.mp4 e output.mp4).

**Evolução:** O projeto está em desenvolvimento e a estrutura dos scripts pode ser alterada em futuras atualizações.




 
