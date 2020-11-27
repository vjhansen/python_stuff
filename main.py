from wordcloud import WordCloud
import PyPDF2
import argparse


def get_string_from_pdf(pdf_path, start_page, end_page):
    content = ""
    p = open(pdf_path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(p)
    if pdfReader.isEncrypted:
        pdfReader.decrypt('')
    for pageNum in range(start_page, end_page):
        page = pdfReader.getPage(pageNum)
        if page.extractText() is not None:
            pageContents = page.extractText()
            content += pageContents
    return content


def makecloud(words, width, height, num_of_words, image_file_name):
    excludewords = []
    f = open('words_to_ignore.txt', 'r')
    for line in f.readlines():
        excludewords.append(line.strip())

    wordcloud = WordCloud(max_words=num_of_words, width=width, height=height,
                          stopwords=excludewords).generate(words)
    image = wordcloud.to_image()
    image.show()
    image.save(image_file_name + '.jpeg')

def main():
    # specify the name of the pdf. Ensure pdf is in same folder
    path = str(args.pdf)

    # starting page of word cloud
    # zero indexed. So subtract 1 from the  actual start page.
    start_pg = args.sp

    # last page you want to scan
    end_pg = args.lp

    WIDTH = 1280
    HEIGHT = 720
    
    # Number of words in the cloud
    NUM_OF_WORDS = args.w

    # Name of the image
    image_file_name = 'word_cloud'

    # If you want to exclude certain words from the cloud,
    # you can add them as a new line to the file "words_to_ignore.txt"
    pdf_to_word = get_string_from_pdf(path, start_pg, end_pg)
    makecloud(pdf_to_word, WIDTH,
                    HEIGHT, NUM_OF_WORDS, image_file_name)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--pdf", required=True, help="Path to the PDF")
    ap.add_argument('-sp', type=int,  required=True, help="start page in document")
    ap.add_argument('-lp', type=int, required=True, help="last page in document")
    ap.add_argument('-w', type=int, required=True, help="number of words in cloud")

    args = ap.parse_args()
    main()
