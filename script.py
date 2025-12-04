from pydub import AudioSegment, silence
import subprocess
import os

VIDEO_INPUT = "input.mp4"
VIDEO_OUTPUT = "output.mp4"
SILENCE_THRESH = -40
MIN_SILENCE_LEN = 700
PRE_AUDIO_SEC = 0.4

audio = AudioSegment.from_file(VIDEO_INPUT)
non_silences = silence.detect_nonsilent(audio, min_silence_len=MIN_SILENCE_LEN, silence_thresh=SILENCE_THRESH)

# Ajusta 1 segundo antes do áudio e 1 segundo depois
non_silences = [
    (max(0, start - PRE_AUDIO_SEC*1000), end + PRE_AUDIO_SEC*1000)
    for start, end in non_silences
]


# Cria um arquivo temporário com os comandos de corte
with open("cuts.txt", "w") as f:
    for i, (start, end) in enumerate(non_silences):
        f.write(f"file '{VIDEO_INPUT}'\n")
        f.write(f"inpoint {start/1000}\n")
        f.write(f"outpoint {end/1000}\n")

# FFmpeg não suporta diretamente múltiplos cortes com -c copy, precisa re-encode
# Uma alternativa é gerar trechos separados e depois concatenar
for i, (start, end) in enumerate(non_silences):
    subprocess.run([
        "ffmpeg", "-y", "-i", VIDEO_INPUT,
        "-ss", str(start/1000), "-to", str(end/1000),
        "-c:v", "libx264", "-c:a", "aac", f"part_{i}.mp4"
    ])

# Concatenar os trechos
with open("concat_list.txt", "w") as f:
    for i in range(len(non_silences)):
        f.write(f"file 'part_{i}.mp4'\n")

subprocess.run([
    "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "concat_list.txt",
    "-c", "copy", VIDEO_OUTPUT
])

def compile_parts(output_file="final_output.mp4"):
    # Gera o arquivo de lista para concatenação
    with open("concat_list.txt", "w") as f:
        i = 0
        while os.path.exists(f"part_{i}.mp4"):
            f.write(f"file 'part_{i}.mp4'\n")
            i += 1

    # Concatena os vídeos re-encodeando para garantir compatibilidade
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "concat_list.txt",
        "-c:v", "libx264", "-c:a", "aac", output_file
    ])

    print("Vídeo final compilado salvo em", output_file)