import cv2
import mediapipe as mp

video = cv2.VideoCapture(0)

hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=2) 
mpDraw = mp.solutions.drawing_utils 

while True:
    check,img = video.read() 
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) 
    results = Hand.process(imgRGB) 
    handsPoints = results.multi_hand_landmarks 
    h,w,_ = img.shape
    total_count = 0
    if handsPoints:
        for hand_idx, points in enumerate(handsPoints):
            mpDraw.draw_landmarks(img, points, hand.HAND_CONNECTIONS)
            pontos = []
            for id, cord in enumerate(points.landmark):
                cx, cy = int(cord.x * w), int(cord.y * h)
                pontos.append((id, cx, cy))

            dedos = [8, 12, 16, 20]
            contador = 0

            if len(pontos) >= 21:
                hand_label = None
                if results.multi_handedness and len(results.multi_handedness) > hand_idx:
                    hand_label = results.multi_handedness[hand_idx].classification[0].label
                if hand_label == "Right":
                    if pontos[4][1] < pontos[3][1]:
                        contador += 1
                else:
                    if pontos[4][1] > pontos[3][1]:
                        contador += 1
                for x in dedos:
                    if pontos[x][2] < pontos[x - 2][2]:
                        contador += 1

            total_count += contador

        cv2.putText(img, str(total_count), (50,100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,0,0), 5)
    cv2.imshow("Imagem" , img) 
    cv2.waitKey(1) 
