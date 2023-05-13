import boto3
from PIL import Image, ImageDraw, ImageFont

def face():
    rekognition = boto3.client('rekognition',region_name='us-east-1',
    aws_access_key_id = 'AKIAZEIUBHY7MVYHTA4S',
                        aws_secret_access_key = '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',
                               )
    with open('faces/achern.jpg', 'rb') as image_data:
        response_content = image_data.read()

    rekognition_response = rekognition.detect_faces(
        Image={'Bytes': response_content}, Attributes=['ALL'])
    print(rekognition_response)

if __name__=="__main__":
    print(42)
    face()