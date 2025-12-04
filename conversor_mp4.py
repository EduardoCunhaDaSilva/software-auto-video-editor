from moviepy import VideoFileClip
import os

# Caminho do vídeo .mov
input_file = "video.mov"  # coloque o nome do seu arquivo .mov aqui
# Nome do arquivo de saída
output_file = "video_convertido.mp4"

# Verifica se o arquivo existe
if not os.path.exists(input_file):
    print(f"Arquivo {input_file} não encontrado.")
else:
    # Carrega o vídeo
    clip = VideoFileClip(input_file)
    # Converte para MP4
    clip.write_videofile(output_file, codec="libx264", audio_codec="aac")
    print(f"Vídeo convertido com sucesso para {output_file}")
