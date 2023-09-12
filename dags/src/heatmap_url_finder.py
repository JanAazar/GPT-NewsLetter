from bs4 import BeautifulSoup
from simplegmail import Gmail
import os

def get_starred_messages():

    gmail = Gmail(client_secret_file=os.path.join("dags","src","client_secret.json"),
                  creds_file=os.path.join("dags","src","gmail_token.json"))

    # Starred messages
    messages = gmail.get_starred_messages()

    # for message in list(messages)[0]:
    #     html_message = message.html
    html_message = messages[0].html
    return html_message


def find_image_url(html,class_name):
    soup = BeautifulSoup(html, 'html.parser')
    image_wrap = soup.find('p', class_=class_name)
    
    if image_wrap:
        image_url = image_wrap.find('img')['src']
        # print(image_url)
        return image_url
    return "No image found"


def find_class(html):
    soup = BeautifulSoup(html, 'html.parser')
    classes = set()
    image_classes = []
    # Find all tags that have the "class" attribute
    tags_with_classes = soup.find_all(class_=True)

    # Extract class names from each tag
    for tag in tags_with_classes:
        class_names = tag.get('class')
        # if class_names[:2] == "m_" and class_names[-10:] == "image-wrap": 
        classes.update(class_names)

    for class_name in list(classes):
        if "image" in class_name and "wrap" in class_name:
            image_classes.append(class_name)   

    return image_classes[0]


def get_url():
    with open("dags//src//market_status.txt", "r") as file:
        market_status = file.read()
    if market_status == "open":
        html_message = get_starred_messages()
        class_name = find_class(html_message)
        url = find_image_url(html_message,class_name)
        return url
    else:
        return "No image found"

if __name__ == "__main__":
    get_url()
