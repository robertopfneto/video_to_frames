# 🎞️ video_to_frames

Extrai automaticamente frames de vídeos organizados em subpastas, salvando 1 frame a cada N dentro da mesma estrutura de diretórios.

### 📦 Instalação do ambiente

Crie um ambiente virtual com Python 3.9:

conda create -n videotoframes python=3.9 -y
conda activate videotoframes

Instale as dependências:
```
pip install numpy opencv-python
```

### 🚀 Como usar

Organize seus vídeos em subpastas dentro de um diretório principal.
  Exemplo:
```
videos/
├── grupo1/
│   └── video1.mp4
├── grupo2/
│   └── video2.avi
```
Configure o caminho no seu script:
```
import caminho_video

caminho_videos = caminho_video.caminho  # Caminho para a pasta "videos"
each_frames = 10  # Salvar 1 frame a cada X frames
```
Execute o script. Os frames serão salvos em subpastas chamadas frames/ dentro de cada grupo:
```
videos/
├── grupo1/
│   ├── video1.mp4
│   └── frames/
│       └── video1_frame_0000.png
```

### ⚙️ Personalização

Altere each_frames = 10 para definir o intervalo de frames salvos.

Modifique o nome da pasta "frames" no código, se quiser outro nome de saída.

🧠 Requisitos

- Python 3.9
- numpy
- opencv-python

