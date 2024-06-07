import pyttsx3
import PyPDF2

reader = PyPDF2.PdfReader(open("linux-commands-handbook.pdf", "rb"))
speaker = pyttsx3.init()

for page_number in range(len(reader.pages)):
    page = reader.pages[page_number]
    text = page.extract_text()
    clean_text = text.strip().replace("\n", " ")
    print(clean_text)
    
    speaker.save_to_file(clean_text, "new.mp3")
    speaker.runAndWait()
    speaker.stop()
