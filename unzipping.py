from zipfile import ZipFile

with ZipFile('../../Downloads/ch2_training_images.zip','r') as zObject:
    zObject.extractall(
        path='./training_images'
    )

with ZipFile('../../Downloads/ch2_training_localization_transcription_gt.zip','r') as zObject:
    zObject.extractall(
        path='./localization'
    )