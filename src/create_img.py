# system imports
from argparse import ArgumentParser
import sys
import urllib.request

# 3rd party imports
import openai
from PIL import Image


def get_usernumber_input(question):
    sys.stdout.write(question)
    userinput = input()

    return userinput


def main():
    # adding arguments, for a more comfortable use:
    parser = ArgumentParser()
    parser.add_argument('-a', '--apikey')

    # actually parsing the arguments
    args = parser.parse_args()

    openai.api_key = args.apikey

    img_size = "512x512"
    amt_of_images_to_create = 1
    request_to_ai = get_usernumber_input("Provide a prompt: ")

    response = openai.Image.create(
        prompt=request_to_ai,
        n=amt_of_images_to_create,
        size=img_size
    )

    image_url = response['data'][0]['url']
    urllib.request.urlretrieve(image_url, "img.png")
    img = Image.open("img.png")
    img.show()


if __name__ == "__main__":
    main()
