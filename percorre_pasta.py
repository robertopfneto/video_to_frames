import cv2
import os
import caminho_video

# Caminho principal com as subpastas que contêm os vídeos
caminho_videos = caminho_video.caminho
each_frames = 10  # Salva um frame a cada X frames

def processar_video(caminho_base):
    for subpasta in os.listdir(caminho_base):
        caminho_subpasta = os.path.join(caminho_base, subpasta)

        if not os.path.isdir(caminho_subpasta):
            continue  # Pula arquivos soltos

        # Cria subpasta 'frames/' dentro da subpasta atual
        pasta_saida = os.path.join("frames")
        os.makedirs(pasta_saida, exist_ok=True)

        for video in os.listdir(caminho_subpasta):
            if video.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
                caminho_video_completo = os.path.join(caminho_subpasta, video)
                nome = os.path.splitext(video)[0]

                cap = cv2.VideoCapture(caminho_video_completo)
                if not cap.isOpened():
                    print(f"Erro ao abrir vídeo: {caminho_video_completo}")
                    continue

                n_frames = 0
                saved_frames = 0

                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break

                    if n_frames % each_frames == 0:
                        nome_frame = f"{nome}_frame_{saved_frames:04d}.png"
                        caminho_saida_frame = os.path.join(pasta_saida, nome_frame)
                        cv2.imwrite(caminho_saida_frame, frame)
                        saved_frames += 1

                    n_frames += 1

                cap.release()
                print(f"[✓] {video} → {saved_frames} frames salvos em {pasta_saida}")

# Executa
processar_video(caminho_videos)
