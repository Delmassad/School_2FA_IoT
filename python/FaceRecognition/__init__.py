import face_recognition
from miscelaneous import listFiles, listDir
from statistics import mean

userNames = listDir('./static/FaceRecognition/')

def votingRecognition(unknown_image):
    names = []
    user_encodings = []
    for user in userNames:
        userFiles = listFiles('./static/FaceRecognition/'+user+'/')
        for facePath in userFiles[:]:
            path = './static/FaceRecognition/'+user+'/'+facePath
            known_image = face_recognition.load_image_file(path)
            user_encodings.append(face_recognition.face_encodings(known_image)[0])
            names.append(user)
    # print(names)

    unknown_faces = face_recognition.face_encodings(unknown_image)
    if not unknown_faces:
        return 'no face to detect'
    unknown_encoding = unknown_faces[0]
    results = face_recognition.compare_faces(user_encodings, unknown_encoding)
    # print(results)
    zipped = list(zip(results, names))
    # print(zipped)
    userResults = {name: [] for name in names}
    # print(userResults)
    for result, name in zipped:
        userResults[name].append(int(result))
    max = 0
    bestMatch = 'unknown user detected'
    # print(userResults)
    for name in userResults:
        # print(name)
        meanScore = sum(userResults[name])/len(userResults[name])
        # print(meanScore)
        if meanScore > max:
            max = meanScore
            bestMatch = name
    return f'Hello {bestMatch}'
