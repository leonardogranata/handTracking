# 🖐️ Hand Tracking - Contador de Dedos

Projeto de visão computacional que utiliza **OpenCV** e **MediaPipe** para detectar mãos em tempo real através da webcam e contar quantos dedos estão levantados.

O sistema reconhece até **duas mãos simultaneamente** e exibe na tela o total de dedos levantados.

---

## 🚀 Tecnologias

- Python
- OpenCV
- MediaPipe

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

Instale as depêndencias:

```bash
pip install opencv-python mediapipe
```

---

## ▶️ Como executar

```bash
python nome_do_arquivo.py
```

É necessário possuir uma webcam funcional.

---

## 🧠 Como funciona

O programa captura a imagem da webcam e utiliza o MediaPipe para detectar até duas mãos simultaneamente.

Cada mão possui 21 pontos de referência (landmarks). A contagem dos dedos é feita da seguinte forma:

- O polegar é analisado comparando a posição horizontal (eixo X), considerando se a mão é direita ou esquerda.
- Os outros quatro dedos são analisados comparando a posição vertical (eixo Y) entre a ponta do dedo e a articulação anterior.
- Cada dedo levantado soma +1 no contador.
- O total de dedos levantados (somando ambas as mãos) é exibido na tela em tempo real.

---

## 📌 Características

- Detecção de até 2 mãos
- Contagem automática de dedos
- Exibição do resultado em tempo real
- Desenho dos landmarks na mão detectada

---

## ⚠️ Limitações

- Requer boa iluminação.
- Pode apresentar imprecisão com inclinação excessiva da mão.
- Não possui tecla de encerramento dedicada.
- Não há tratamento de erro para falha na webcam.

---

## 🔮 Melhorias futuras

- Adicionar tecla para encerrar o programa.
- Implementar reconhecimento de gestos específicos.
- Integrar com automações (controle de volume, slides, cursor).
- Criar interface gráfica.
