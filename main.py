from tkinter import *  # pip install tkinter
from tkinter import filedialog
import nltk  # pip install nltk
from textblob import TextBlob  # pip install textblob
from newspaper import Article  # pip install newspaper3k
import speech_recognition as sr  # pip install speechrecognition

import PyPDF2  # pip install pypdf2
import spacy  # pip install -U spacy,  # python -m spacy download en_core_web_sm
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest

import tkinter as tk
import requests
import webbrowser
from googlesearch import search  # pip install google,   # pip install beautifulsoup4

from tkinter import ttk
from tkinter.messagebox import askyesno

from transformers import pipeline  # pip install transformers,  # pip install transformers
from youtube_transcript_api import YouTubeTranscriptApi  # pip install pipeline youtube-transcript-api
from IPython.display import YouTubeVideo
import threading

# The whole form
form = Tk()
form.geometry('1110x650')
form.configure(bg='#262626')
form.resizable(0, 0)
form.title("PS Tech")  # Top title


# --------------- HOME ---------------- DONE
def home():
    f2 = Frame(form, width=1100, height=645, bg='#262626')
    f2.place(x=0, y=45)
    l2 = Label(form, text="PS Tech", fg='white', bg='#262626')
    l2.config(font=('Comic Sans MS', 50))
    l2.place(x=510, y=250)
    toggle_win()


# --------------- WEB SUMMARIZER ---------------- DONE
def summ():
    def summarize():
        # nltk.download('punkt')

        url = urltext.get('1.0', "end").strip()

        article = Article(url)

        article.download()
        article.parse()

        article.nlp()

        title.config(state='normal')
        author.config(state='normal')
        publication.config(state='normal')
        summary.config(state='normal')
        sentiment.config(state='normal')

        title.delete('1.0', 'end')
        title.insert('1.0', article.title)

        author.delete('1.0', 'end')
        author.insert('1.0', article.authors)

        publication.delete('1.0', 'end')
        publication.insert('1.0', article.publish_date)

        summary.delete('1.0', 'end')
        summary.insert('1.0', article.summary)

        analysis = TextBlob(article.text)
        sentiment.delete('1.0', 'end')
        sentiment.insert('1.0',
                         f'Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

        title.config(state='disable')
        author.config(state='disable')
        publication.config(state='disable')
        summary.config(state='disable')
        sentiment.config(state='disable')

    f2 = Frame(form, width=1100, height=645, bg='#262626')
    f2.place(x=0, y=45)

    l2 = Label(form, text='Summarizer', fg='white', bg='#262626')
    l2.config(font=('Comic Sans MS', 15))
    l2.place(x=200, y=50)  # position the name

    # Title Label
    tlabel = Label(form, text='Title')
    tlabel.place(x=200, y=90)
    # Title Textbox
    title = Text(form, height=1, width=112)
    title.config(state='disable', bg='#dddddd')
    title.place(x=200, y=120)

    # Author Label
    alabel = Label(form, text='Author')
    alabel.place(x=200, y=150)
    # Author Textbox
    author = Text(form, height=1, width=112)
    author.config(state='disable', bg='#dddddd')
    author.place(x=200, y=180)

    # Published Date Label
    plabel = Label(form, text='Publishing Date')
    plabel.place(x=200, y=210)
    # Published Date Textbox
    publication = Text(form, height=1, width=112)
    publication.config(state='disable', bg='#dddddd')
    publication.place(x=200, y=240)

    # Summary Label
    slabel = Label(form, text='Summary')
    slabel.place(x=200, y=270)
    # Summary Textbox
    summary = Text(form, height=10, width=112)
    summary.config(state='disable', bg='#dddddd')
    summary.place(x=200, y=300)

    # Sentiment analysis Label
    selabel = Label(form, text='Sentiment Analysis')
    selabel.place(x=200, y=470)

    # Published Date Textbox
    sentiment = Text(form, height=1, width=112)
    sentiment.config(state='disable', bg='#dddddd')
    sentiment.place(x=200, y=500)

    # url label
    urllabel = Label(form, text='URL')
    urllabel.place(x=200, y=530)
    # url input
    urltext = Text(form, height=1, width=112)
    urltext.place(x=200, y=560)

    # Button
    btn = Button(form, text="Summarize", command=summarize)
    btn.place(x=200, y=600)

    toggle_win()


# ----------- BOT --------------
def bot():
    def listen():
        listener = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening...")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                print(command)
        except:
            print("not working")
            pass
        convertedtext = Text(form, height=13, width=95)
        convertedtext.config(state='normal', bg='#dddddd')
        convertedtext.delete('1.0', 'end')
        convertedtext.insert('1.0', command)
        convertedtext.config(state='disabled')
        convertedtext.place(x=310, y=130)

    def listenThread():
        thread = threading.Thread(target=listen)
        thread.start()

    def stop():
        pass

    def reset():
        pass

    def summarize():
        pass

    def rephrase():
        pass

    f2 = Frame(form, width=1100, height=645, bg='#262626')
    f2.place(x=0, y=45)

    l2 = Label(form, text='BOT', fg='white', bg='#262626')
    l2.config(font=('Comic Sans MS', 15))
    l2.place(x=200, y=50)  # position the name

    # Label
    textlabel = Label(form, text='Your Text')
    textlabel.place(x=310, y=100)

    # TextBox from voice
    convertedtext = Text(form, height=13, width=95)
    convertedtext.config(state='disable', bg='#dddddd')
    convertedtext.place(x=310, y=130)

    # result Label
    resultlabel = Label(form, text='Result')
    resultlabel.place(x=310, y=360)

    # TextBox for result
    resulttext = Text(form, height=13, width=95)
    resulttext.config(state='disable', bg='#dddddd')
    resulttext.place(x=310, y=390)

    # Button listen
    btnlisten = Button(form, text="Listen", command=listenThread)
    btnlisten.place(x=220, y=150)

    # Button stop
    btnstop = Button(form, text="Stop", command=stop)
    btnstop.place(x=220, y=230)

    # Button reset
    btnstop = Button(form, text="Reset", command=reset)
    btnstop.place(x=220, y=310)

    # Button summarize
    btnsumm = Button(form, text="Summarize", command=summarize)
    btnsumm.place(x=220, y=420)

    # Button rephrase
    btnspin = Button(form, text="Rephrase", command=rephrase)
    btnspin.place(x=220, y=500)

    toggle_win()


# ---------------- YouTube SUMMARIZER ----------------- Done
def youtube():
    def ytsum():
        url = urltext.get('1.0', "end").strip()

        videoId = url.split('=')[1]

        # YouTubeVideo(videoId)
        # extract the text

        transcript = YouTubeTranscriptApi.get_transcript(videoId)

        result = ''
        for i in transcript:
            result += ' ' + i['text']

        summarizer = pipeline('summarization')

        # length of the list di concatinate jadi int di divisible by 1000
        num_iters = int(len(result) / 1000)
        # ini bakal jadi tempat nampung text
        summarized_text = []
        for i in range(0, num_iters + 1):
            start = 0
            start = i * 1000
            end = (i + 1) * 1000
            out = summarizer(result[start:end])
            out = out[0]
            out = out['summary_text']
            summarized_text.append(out)

        join1 = ' '.join(summarized_text)

        # Show the output in textbox
        summarytxt = Text(form, height=10, width=112)
        summarytxt.config(state='normal', bg='#dddddd')
        summarytxt.delete('1.0', 'end')
        summarytxt.insert('1.0', join1)
        summarytxt.config(state='disabled')
        summarytxt.place(x=200, y=180)
    def ytThread():
        thread = threading.Thread(target=ytsum)
        thread.start()

    f2 = Frame(form, width=1100, height=645, bg='#262626')
    f2.place(x=0, y=45)

    l2 = Label(form, text='YouTube Summarizer', fg='white', bg='#262626')
    l2.config(font=('Comic Sans MS', 15))
    l2.place(x=200, y=50)

    # Title Label
    tlabel = Label(form, text='Enter URL')
    tlabel.place(x=200, y=90)

    # url input
    urltext = Text(form, height=1, width=112)
    urltext.place(x=200, y=120)

    # summarize Button
    btn = Button(form, text="Summarize YouTube Video", command=ytThread)
    btn.place(x=200, y=150)

    # Summary Textbox
    summarytxt = Text(form, height=10, width=112)
    summarytxt.config(state='disable', bg='#dddddd')
    summarytxt.place(x=200, y=180)

    toggle_win()


# ------------- PDF ------------ DONE
def pdf():
    def explorefile():  # Function to open PDF file, then convert it into text
        filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("PDF files", "*.pdf*"),
                                                                                                ("all files", "*.*")))

        # Show file Location
        label_file_explorer.configure(text="File Opened: " + filename)

        pdfFileObj = open(filename, "rb")
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        myText = ''
        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)

            myText += pageObj.extractText()

        # Textbox
        summarytxt = Text(form, height=10, width=112)
        summarytxt.config(state='normal', bg='#dddddd')
        summarytxt.delete('1.0', 'end')
        summarytxt.insert('1.0', myText)
        summarytxt.config(state='disabled')
        summarytxt.place(x=200, y=180)

        def textsumarizer():  # Function to summarize the text
            # load the NLP process in english language
            nlp = spacy.load("en_core_web_sm")

            # get text from textbox
            text = summarytxt.get('1.0', "end").strip()

            # NLP
            doc = nlp(text)

            # counting the keyword and removing the stop words
            keyword = []
            stopwords = list(STOP_WORDS)
            pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB']
            for token in doc:
                if token.text in stopwords or token.text in punctuation:
                    continue
                if token.pos_ in pos_tag:
                    keyword.append(token.text)

            # set the counter for frequent word
            freqWord = Counter(keyword)

            # counting the most frequent word in the article
            maxFreq = Counter(keyword).most_common(1)[0][1]
            for word in freqWord.keys():
                freqWord[word] = (freqWord[word] / maxFreq)
            freqWord.most_common(5)

            sentStrength = {}
            for sent in doc.sents:
                for word in sent:
                    if word.text in freqWord.keys():
                        if sent in sentStrength.keys():
                            sentStrength[sent] += freqWord[word.text]
                        else:
                            sentStrength[sent] = freqWord[word.text]

            summarized_sentences = nlargest(3, sentStrength, key=sentStrength.get)

            final_sentences = [w.text for w in summarized_sentences]
            summaryies = ' '.join(final_sentences)

            # Summarize Textbox
            summary = Text(form, height=15, width=112)
            summary.config(state='normal', bg='#dddddd')
            summary.delete('1.0', 'end')
            summary.insert('1.0', summaryies)
            summary.config(state='disabled')
            summary.place(x=200, y=390)

        # Summarize Button
        btn = Button(form, text="Summarize PDF", command=textsumarizer)
        btn.place(x=200, y=360)

    f2 = Frame(form, width=1110, height=645, bg='#262626')
    f2.place(x=0, y=45)

    l2 = Label(form, text='PDF Summarizer', fg='white', bg='#262626')
    l2.config(font=('Comic Sans MS', 15))
    l2.place(x=200, y=50)

    # Show File Location Label
    label_file_explorer = Label(text="Please Click 'Browse PDF'", width=100, height=2, fg="blue")
    label_file_explorer.place(x=200, y=90)

    # button for browse file
    btnbrowse = Button(form, text="Browse PDF", command=explorefile)
    btnbrowse.place(x=200, y=140)

    toggle_win()


# ------------ eBook ------------ Done
def ebook():
    def ebookdownloader():
        query = userinput.get('1.0', "end").strip()
        queryList = query.split(" ")
        query = ""

        # creating the query to be search
        for i in range(len(queryList)):
            if i == 0:
                query = query + queryList[i]
                continue
            query = query + "+" + queryList[i]
        query = query + "+eBook"

        for fileURL in search(query, tld="com", stop=10, pause=2):
            # Show URL Results
            result = Text(form, height=10, width=112)
            result.config(state='normal', bg='#dddddd')
            result.delete('1.0', 'end')
            result.insert('1.0', fileURL)
            result.config(state='disabled')
            result.place(x=200, y=270)
            if fileURL.split(".")[-1] == "pdf":
                # Book Found
                foundlabel = Label(form, text='Book Found')
                foundlabel.place(x=200, y=450)
                break

        # creating the file name
        fileName = fileURL.split("/")[-1]
        fileName = fileName.split(".")[0]
        # creating a HTTP request
        req = requests.get(fileURL, stream=True)

        # send the HTTP request and save the response into an object called e
        # saving the received content as a png file in binary format
        # then, write the content of the response (e.content) to a new file in binary mode
        def btndownload():
            with open(f"{fileName}.pdf", 'wb') as saveData:  # put this code in a button (def)
                for chunk in req.iter_content(chunk_size=1024):
                    # writing one chunk at a time
                    if chunk:
                        saveData.write(chunk)
                    # Status Label
                    statuslabel = Label(form, text='Download Complete, your file name is: ' + fileName)
                    statuslabel.place(x=200, y=510)

            # pop up yes / no
            if statuslabel:
                # click event handler
                answer = askyesno(title='confirmation',
                                  message='Do you want to open the eBook?')
                if answer:
                    webbrowser.open_new(f"{fileName}.pdf")

        # Button Download
        btndwnload = Button(form, text="Download File", command=btndownload)
        btndwnload.place(x=200, y=480)

    f2 = Frame(form, width=1110, height=645, bg='#262626')
    f2.place(x=0, y=45)

    l2 = Label(form, text='eBook Downloader', fg='white', bg='#262626')
    l2.config(font=('Comic Sans MS', 15))
    l2.place(x=200, y=50)

    # Search Label
    searchlabel = Label(form, text='Please Enter the Title of the Book')
    searchlabel.place(x=200, y=150)  # 170

    # User Input
    userinput = Text(form, height=1, width=112)
    userinput.place(x=200, y=180)

    # Button Search
    btnsearch = Button(form, text="Search eBook", command=ebookdownloader)
    btnsearch.place(x=200, y=210)

    # Result Label
    reslabel = Label(form, text='Results')
    reslabel.place(x=200, y=240)

    # Results Box
    result = Text(form, height=10, width=112)
    result.config(state='disabled', bg='#dddddd')
    result.place(x=200, y=270)

    toggle_win()


# --------------- MENU BAR ------------- DONE
def toggle_win():
    # frame1 (menu form)
    f1 = Frame(form, width=200, height=650, bg='#12c4c0')
    f1.place(x=0, y=0)

    # buttons
    def bttn(x, y, text, bcolor, fcolor, cmd):
        def on_entera(e):
            myButton1['background'] = bcolor  # ffcc66
            myButton1['foreground'] = '#262626'  # 000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground'] = '#262626'

        myButton1 = Button(f1, text=text, width=42, height=2, fg='#262626', border=0,
                           bg=fcolor, activeforeground='#262626', activebackground=bcolor, command=cmd)

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)

    # Buttons in the menu bar
    bttn(-50, 66, 'H O M E', '#0f9d9a', '#12c4c0', home)
    bttn(-50, 103, 'Web Article Summarizer', '#0f9d9a', '#12c4c0', summ)
    bttn(-50, 140, 'BOT', '#0f9d9a', '#12c4c0', bot)
    bttn(-50, 177, 'Youtube Summarizer', '#0f9d9a', '#12c4c0', youtube)
    bttn(-50, 214, 'PDF Summarizer', '#0f9d9a', '#12c4c0', pdf)
    bttn(-50, 251, 'eBook Downloader', '#0f9d9a', '#12c4c0', ebook)


home()

toggle_win()

form.mainloop()
