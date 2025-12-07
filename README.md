🛠 Editor de Vídeo + Conversor MP4

Status: EM CONSTRUÇÃO

Este projeto contém dois scripts Python:

editor_video.py — Remove partes silenciosas de um vídeo e junta os trechos com áudio.

conversor_mp4.py — Converte arquivos .mov para .mp4.

📦 Dependências

Instale tudo antes de rodar:

pip install pydub moviepy


Além disso, é obrigatório ter o FFmpeg instalado no sistema.

Verificar o FFmpeg
ffmpeg -version


Se não aparecer versão nenhuma, instale:

Windows

Baixe em: https://ffmpeg.org/download.html

Adicione o binário ao PATH.

Linux (Debian/Ubuntu)
sudo apt install ffmpeg

MacOS (Homebrew)
brew install ffmpeg

📁 Estrutura recomendada
/projeto
  editor_video.py
  conversor_mp4.py
  input.mp4
  video.mov

▶️ Como usar
1) Editor de Vídeo (remove silêncio)
Arquivo: editor_video.py
O que ele faz

Carrega input.mp4

Detecta trechos com áudio

Corta somente esses trechos

Cria vários arquivos part_X.mp4

Junta tudo em output.mp4

Também tem a função compile_parts() caso você queira recompilar manualmente

Rodar:
python editor_video.py


O arquivo final gerado será:

output.mp4


Se quiser recompilar manualmente depois:

from editor_video import compile_parts
compile_parts("final_output.mp4")

2) Conversor de MOV ➜ MP4
Arquivo: conversor_mp4.py
O que ele faz

Carrega video.mov

Converte para video_convertido.mp4

Rodar:
python conversor_mp4.py


Se o arquivo video.mov não existir, ele avisa.

⚠️ Avisos

O editor de vídeo re-encoda os trechos, ou seja, não é instantâneo.

O projeto está em construção, então pode ter comportamento estranho ou gerar arquivos muito grandes dependendo do vídeo.
