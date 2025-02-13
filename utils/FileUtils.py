import markdown2
import base64

def encode_image(image_path):   
    image_file=open(image_path, "rb")
    print(image_file)
    return base64.b64encode(image_file.read()).decode('utf-8')

def encode_bytes(image_bytes):
    return base64.b64encode(image_bytes).decode('utf-8')

def markdown_to_text(markdown_input):
    
    html = markdown2.markdown(markdown_input)
    
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    
    return text

if __name__ == "__main__":
    markdown_input = """
    # This is a header

    This is some **bold** text and this is *italic* text.
    """
    plain_text = markdown_to_text(markdown_input)
    print(plain_text)
