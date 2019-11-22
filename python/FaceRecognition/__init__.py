import face_recognition
from miscelaneous import listFiles, listDir
from statistics import mean

userNames = listDir('./FaceRecognition/data/')
names = []
user_encodings = []
for user in userNames:
    userFiles = listFiles('./FaceRecognition/data/'+user+'/')
    for facePath in userFiles[:]:
        path = './FaceRecognition/data/'+user+'/'+facePath
        known_image = face_recognition.load_image_file(path)
        user_encodings.append(face_recognition.face_encodings(known_image)[0])
        names.append(user)
# print(names)


def votingRecognition(unknown_image):
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    results = face_recognition.compare_faces(user_encodings, unknown_encoding)
    # print(results)
    zipped = list(zip(results, names))
    # print(zipped)
    userResults = {name: [] for name in names}
    # print(userResults)
    for result, name in zipped:
        userResults[name].append(int(result))
    max = 0
    bestMatch = 'unknown user'
    # print(userResults)
    for name in userResults:
        # print(name)
        meanScore = sum(userResults[name])/len(userResults[name])
        # print(meanScore)
        if meanScore > max:
            max = meanScore
            bestMatch = name
    return bestMatch
