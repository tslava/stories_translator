from telegraph import Telegraph


def upload_image(image_path: str):
    print("Uploading image to telegra.ph...")

    telegraph = Telegraph()

    # Create a new Telegraph account or login to an existing one
    # Replace 'python_telegraph' with your preferred short name
    response = telegraph.create_account(short_name='python_telegraph')

    # Use the access_token from the response for further operations
    telegraph = Telegraph(access_token=response['access_token'])

    # Upload the image to Telegraph
    image_url = telegraph.upload_file(image_path)

    full_url = f"https://telegra.ph{image_url[0]['src']}"

    print(f"Done. Image URL: {full_url}")

    return full_url




def upload_to_telegraph(title: str, text: str):
    print("Uploading to telegra.ph...")

    telegraph = Telegraph()

    # Create a new Telegraph account or login to an existing one
    # Replace 'python_telegraph' with your preferred short name
    response = telegraph.create_account(short_name='python_telegraph')

    # Use the access_token from the response for further operations
    telegraph = Telegraph(access_token=response['access_token'])

    # Upload the text to Telegraph
    response = telegraph.create_page(title, html_content=text)

    print("Done. Page URL: https://telegra.ph/{}".format(response['path']))


if __name__ == "__main__":
    # Upload an image to telegra.ph
    upload_image('generated/Wieża_Klimek_w_Grudziądzu_2015/images/1.png')

    # Upload text to telegra.ph
    # upload_to_telegraph('Sample Page', '<p>Hello, world!</p>')