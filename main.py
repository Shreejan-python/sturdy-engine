import os

def create(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}") 

if __name__ == "__main__":
        
    files = os.listdir()

    create('Images')
    create('Docs')
    create('Media')
    create('Others')

    imgExts = [".png", ".jpg", ".jpeg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts ]

    docExts = [".txt", ".docx", ".doc", ".pdf", ".xlsx", ".pptx", ".ppt", ".csv"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]


    mediaExts = [".mp4", ".mp3", ".flv"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
            others.append(file)

    move("Images", images)
    move("Docs", docs)
    move("Media", medias)
    move("Others", others)

