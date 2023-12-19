# 2023_capstone
Advanced StarGAN-VC: Extracting precise speaker feature using speaker encoder from AutoVC

# architecture
기존의 StarGAN-VC 모델에 Auto-VC의 (pretrained 된) Speaker Encoder 모듈만을 가지고 옴

StarGAN-VC 모델의 Discriminator 와 Generator 내부에서 마지막 Convnet 들어가기 전에 Speaker Encoder에서 추출된 D-vector 과 Discriminator에서 추출된 D-vector 의 차이 값을 loss 값으로 정의해 학습을 진행

