import boto3
import pickle
from gpt import compliment

def face(img='faces/achern.jpg'):
    rekognition = boto3.client('rekognition',region_name='us-east-1',
    aws_access_key_id = 'AKIAZEIUBHY7MVYHTA4S',
                        aws_secret_access_key = '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')
    with open(img, 'rb') as image_data:
        response_content = image_data.read()

    rekognition_response = rekognition.detect_faces(
        Image={'Bytes': response_content}, Attributes=['ALL'])
    return (rekognition_response["FaceDetails"][0])

def generate_compliment_prompt(face_details):
    rez = 'write compliment for '
    if face_details['Gender']['Value']=='Male':
        rez+= 'boy'
    else:
        rez+='girl'
    if face_details['Smile']['Value']:
        rez+= ',with a smile '
    if face_details['Eyeglasses']['Value']:
        rez+=', who wears Eyeglasses'
    rez+=' and looks '+ (face_details['Emotions'][0]['Type']).lower()
    return rez


if __name__=="__main__":
    f = face('faces/vgusak.jpg')
    prompt = generate_compliment_prompt(f)
    print(prompt)
    comp = compliment(prompt)
    print(comp)


    # file = open('achern', 'rb')
    # f = pickle.load(file)
    # file.close()

    # file = open('achern', 'wb')
    # pickle.dump(f, file)
    # file.close()