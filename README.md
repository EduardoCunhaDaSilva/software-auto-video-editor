🎬 Editor de Vídeo + Conversor MP4
Status: 🚧 Em construção

Este projeto reúne duas ferramentas simples para edição e conversão de vídeos usando Python:

Editor de Vídeo: detecta silêncio, corta automaticamente e recompila o vídeo.

Conversor MOV → MP4: converte vídeos .mov para .mp4 usando MoviePy.

📦 Dependências

Instale as bibliotecas necessárias:

pip install pydub moviepy

🧰 FFmpeg (Obrigatório)

Os dois scripts dependem do FFmpeg.
Verifique se está instalado:

ffmpeg -version


Se não estiver, instale:

Windows: https://ffmpeg.org/download.html
 (adicionar o bin/ ao PATH)
Linux:

sudo apt install ffmpeg


MacOS:

brew install ffmpeg

📁 Estrutura recomendada
/projeto
 ├── editor_video.py
 ├── conversor_mp4.py
 ├── input.mp4
 └── video.mov

🎧 Editor de Vídeo (Remove Silêncio)
📜 Arquivo: editor_video.py
✨ O que ele faz

Lê input.mp4

Detecta trechos com áudio

Corta somente as partes úteis

Gera múltiplos arquivos part_X.mp4

Junta tudo em output.mp4

Possui função compile_parts() caso queira recompilar manualmente

▶️ Como rodar
python editor_video.py


Resultado principal:

output.mp4

🔁 Recompilar manualmente
from editor_video import compile_parts
compile_parts("final_output.mp4")

🎥 Conversor MOV → MP4
📜 Arquivo: conversor_mp4.py
✨ O que ele faz

Abre video.mov

Converte para video_convertido.mp4

Usa MoviePy com codec H.264 + AAC

▶️ Como rodar
python conversor_mp4.py


Resultado:

video_convertido.mp4

⚠️ Avisos importantes

O editor precisa re-encodar os trechos, então não é rápido.

Arquivos gerados podem ficar grandes dependendo da qualidade do vídeo.

O projeto ainda está em construção, então mudanças são esperadas.
