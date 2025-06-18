#bibliotecas
import cv2
import os

#caminho 
import caminho_video

caminho_videos = caminho_video.caminho #trocar isso pelo caminho ate os videos
videos_salvos = caminho_videos.videos_salvos # isso tambem
each_frames = 10

def processar_video(videos_input, videos_output):
    os.makedirs(videos_output,exist_ok=True)

    for video in os.listdir(videos_input):
        if video.lower().endswith(('mp4','.avi','.mov','.mkv')):
            caminho_video = os.path.join(videos_input, video)
            nome = os.path.splitext(video)[0] #pegar so o nome do arquivo
        
            cap = cv2.VideoCapture(caminho_video)

            if not cap.isOpened():
                print(f"Erro ao abrir vídeo: {nome}")
                continue

            n_frames = 0
            saved_frames = 0

            while True:
                ret, frame = cap.read() #le o proximo frame
                if not ret: # ret eh booleano e retorna falso quando nao tem proximo frame
                    break

                if n_frames % each_frames == 0:
                    image_out = f"{nome}_frame_{saved_frames:04d}.png"
                    output_path = os.path.join(videos_output, nome)
                    cv2.imwrite(output_path, frame)
                    saved_frames += 1
                
                n_frames += 1

            cap.release()
            print(f"Video processado com sucesso, Total de Frames extraidos: {n_frames}")


processar_video(caminho_videos, videos_salvos)

