"""
NLP 19CNTThuc
Bui Phu Thinh - 19127558
Nguyen Van Hung Dung - 19127126
Nguyen Duy Khang - 19127172
Final Project
Xây dựng web tìm kiếm và hiển thị các nội dung tương đồng với 1 văn bản cần kiểm tra bằng Google
"""
# pip install tkinter
from tkinter import *
import tkinter as tk
from tkinter.font import Font
from tkinter import filedialog
# python -m pip install requests
import requests
# pip install beautifulsoup4
from bs4 import BeautifulSoup
# pip install google
# pip install googlesearch-python
from googlesearch import search
import os

# pip install rake-nltk
from rake_nltk import Rake
from nltk import tokenize

# for similarity check:
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def init_landing_page():
    bg = Canvas(rt, bg="#4290f5", width=w, height=h)
    bg.grid(row=0, column=0)
    str1 = Entry(bg)
    bg.create_text(w / 2, h / 2 - 150, text="FIND SIMILARITY TEXT ON THE INTERNET", font=bFont)
    bg.create_text(w / 2, h / 2 - 125, text="19127558 - Bùi Phú Thịnh", font=mFont)
    bg.create_text(w / 2, h / 2 - 100, text="19127126 - Nguyễn Văn Hùng Dũng", font=mFont)
    bg.create_text(w / 2, h / 2 - 75, text="19127172 - Nguyễn Duy Khang", font=mFont)
    bg.create_text(w / 2, h / 2 - 50, text="19CNTT - NLP", font=mFont)
    bg.create_text(w / 2, h / 2 - 25, text="Instructors: Assoc Prof. Đinh Điền ", font=mFont)
    bg.create_text(w / 2, h / 2 - 0, text="TA: Lương An Vinh ", font=mFont)
    b1 = Button(bg, text="Begin", bg='green', activebackground='#7842f5', command=init_Input_page)
    bg.create_window(w / 2, h / 2 - -25, window=b1, width=w / 8)


def init_Input_page():
    bg = Canvas(rt, bg="#c242f5", width=w, height=h)
    bg.grid(row=0, column=0)
    bg.create_text(w / 2, h / 2 - 250, text="FIND SIMILARITY TEXT ON THE INTERNET", font=bFont)
    bg.create_text(w / 2, h / 2 - 200, text="Enter the sentence you want to check: ", font=mFont)
    str1 = Entry(bg)
    bg.create_window(w / 2, h / 2 - 175, window=str1, width=w / 3)
    b0 = Button(bg, text="Back", bg='#ffd700', fg='black', command=init_landing_page)
    bg.create_window(w / 2 - 100, h / 2, window=b0, width=w / 8)
    b1 = Button(bg, text="Confirm", bg='green', activebackground='#7842f5', command=lambda: Input_Handler(str1,eng,vie))
    bg.create_window(w / 2 + 100, h / 2, window=b1, width=w / 8)
    eng=IntVar()
    vie=IntVar()
    b2 = Button(bg, text="Choose Language", bg='light blue', activebackground='#7842f5', command=lambda: Language_choose(eng,vie))
    bg.create_window(w / 2, h / 2-125, window=b2, width=w / 8)
    
def Language_choose(eng,vie):
    Error_Handler = Toplevel(rt)
    Error_Handler.geometry("250x90")
    Error_Handler.title("Choose language that you want to search")
    Checkbutton(Error_Handler, text="eng", variable=eng).grid(row=1, sticky=W)
    Checkbutton(Error_Handler, text="vie", variable=vie).grid(row=2, sticky=W)



def Input_Handler(str1,eng,vie):
    s1 = str1.get()
    if s1 == '':
        # empty input case:
        Error_Handler = Toplevel(rt)
        Error_Handler.geometry("250x90")
        Error_Handler.title("Warning!")
        Label(Error_Handler, text="Input cannot be empty").pack()
        Button(Error_Handler, text="OK", command=Error_Handler.destroy).pack()
    else:
        init_Search_page(str1,eng,vie)


def init_Search_page(str1,eng,vie):
    s1 = str1.get()
    engs=eng.get()
    viet=vie.get()
    print(engs)
    print(viet)
    if engs==1:
        sw=stopwords.words('english')
        print("stopwords english")
    elif viet==1:
        with open('vietnamese-stopwords.txt','r', encoding="utf-8") as swfile:
            sw=[line.rstrip() for line in swfile]
        print("stopwords Vienamese")
    else:
        sw=stopwords.words('english')
        print("stopwords english")
    result = ""
    bg = Canvas(rt, bg="#4290f5", width=w, height=h)
    bg.grid(row=0, column=0)
    bg.create_text(w / 2, h / 2 - 250, text="FIND SIMILARITY TEXT ON THE INTERNET", font=bFont)
    bg.create_text(w / 2, h / 2 - 200, text=f"Top 4 in 10 results of some web pages that match with your text: {s1}",
                   font=mFont)
    for link in search(s1, tld="co.in", num=10, stop=10, pause=2):
        result += link + "\n"
    res_arr = result.split("\n")
    with open("Link_result_full.txt", "w") as f1:
        f1.writelines(result)
    temp1 = Entry(bg)
    bg.create_window(w / 2, h / 2 - 175, window=temp1, width=w / 3)
    temp1.insert(END, res_arr[0])
    temp2 = Entry(bg)
    bg.create_window(w / 2, h / 2 - 150, window=temp2, width=w / 3)
    temp2.insert(END, res_arr[1])
    temp3 = Entry(bg)
    bg.create_window(w / 2, h / 2 - 125, window=temp3, width=w / 3)
    temp3.insert(END, res_arr[2])
    temp4 = Entry(bg)
    bg.create_window(w / 2, h / 2 - 100, window=temp4, width=w / 3)
    temp4.insert(END, res_arr[3])
    b0 = Button(bg, text="Back", bg='#ffd700', fg='black', command=init_Input_page)
    bg.create_window(w / 2 - 100, h / 2 - 65, window=b0, width=w / 8)
    b1 = Button(bg, text="Open full log of link", bg='green', activebackground='#000000', command=open_logfile)
    bg.create_window(w / 2 + 100, h / 2 - 65, window=b1, width=w / 8)
    b2 = Button(bg, text="Link 1", bg='orange', activebackground='#FFA500',
                command=lambda: open_details(res_arr[0], str1,sw))
    bg.create_window(w / 2 + 350, h / 2 - 175, window=b2, width=w / 24)
    b3 = Button(bg, text="Link 2", bg='orange', activebackground='#FFA500',
                command=lambda: open_details(res_arr[1], str1,sw))
    bg.create_window(w / 2 + 350, h / 2 - 150, window=b3, width=w / 24)
    b4 = Button(bg, text="Link 3", bg='orange', activebackground='#FFA500',
                command=lambda: open_details(res_arr[2], str1,sw))
    bg.create_window(w / 2 + 350, h / 2 - 125, window=b4, width=w / 24)
    b5 = Button(bg, text="Link 4", bg='orange', activebackground='#FFA500',
                command=lambda: open_details(res_arr[3], str1,sw))
    bg.create_window(w / 2 + 350, h / 2 - 100, window=b5, width=w / 24)
    r = Button(bg, text="Landing Page", bg='red', fg='blue', command=init_landing_page)
    bg.create_window(w / 2, h / 2 - 30, window=r, width=w / 8)


def open_logfile():
    logfile = 'Link_result_full.txt'
    Handler = Toplevel(rt)
    Handler.geometry("350x100")
    Handler.title("File Opening")
    Label(Handler, text="You're about to open txt file with full log").pack()
    Label(Handler, text=logfile).pack()
    os.system('"%s"' % logfile)
    Button(Handler, text="OK", command=Handler.destroy).pack()

def similarity_checker(str1, str2, sw): 
    # Low the UPPERCASE:
    str1=str1.lower()
    str2=str2.lower()
    # Remove punctuation:
    str1=''.join([word for word in str1 if word not in string.punctuation])
    str2=''.join([word for word in str2 if word not in string.punctuation])
    # Tokenize string:
    token1 = word_tokenize(str1) 
    token2 = word_tokenize(str2)
    vect1 =[];vect2 =[]
    # Remove stopwords:
    set1 = {word for word in token1 if not word in sw} 
    set2 = {word for word in token2 if not word in sw}
    vect = set1.union(set2) 
    # Convert 2 string into 2 vector for cosine formula:
    for word in vect:
        if word in set1: vect1.append(1)
        else: vect1.append(0)
        if word in set2: vect2.append(1)
        else: vect2.append(0)
    # Use cosine formular to calculate similarity
    tmp = 0
    for i in range(len(vect)):
            tmp+= vect1[i]*vect2[i]
    Result_cosine = tmp / float((sum(vect1)*sum(vect2))**0.5)
    return Result_cosine

def open_details(link, str1,sw):
    s1 = str1.get()
    rake_nltk_var = Rake()
    rake_nltk_var.extract_keywords_from_text(s1)
    keywords = rake_nltk_var.get_ranked_phrases()

    req = requests.get(link)
    soup = BeautifulSoup(req.content, "html.parser")
    window = tk.Tk()
    window.title(link)

    text = tk.Text(window, height=h, width=185, bg="#FFFFAA", fg="blue")
    scroll = tk.Scrollbar(window)
    text.configure(yscrollcommand=scroll.set)
    text.pack(side=tk.LEFT)

    s = soup.getText()
    m = tokenize.sent_tokenize(s)

    #Test
    for i in m:
        cosine= similarity_checker(s1,i,sw)*100
        if cosine<30:
            text.insert(tk.END, i)
            text.insert(tk.END, "\n")
        elif cosine<=50 and cosine >=30:
            text.tag_config('warning1', foreground="green")
            text.tag_config('cosine', background='green', foreground="yellow")
            text.insert(tk.END, i,'warning1')
            text.insert(tk.END, cosine, 'cosine')
            text.insert(tk.END, "\n")
        elif cosine<=70 and cosine>50:
            text.tag_config('warning2', foreground="orange")
            text.tag_config('cosine', background='green', foreground="yellow")
            text.insert(tk.END, i,'warning2')
            text.insert(tk.END, cosine, 'cosine')
            text.insert(tk.END, "\n")
        elif cosine>70: 
            text.tag_config('warning3',background='yellow', foreground="red")
            text.tag_config('cosine', background='green', foreground="yellow")
            text.insert(tk.END, i,'warning3')
            text.insert(tk.END, cosine, 'cosine')
            text.insert(tk.END, "\n")
        print(cosine)
    scroll.config(command=text.yview)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    tk.mainloop()


if __name__ == "__main__":
    rt = Tk()
    w = rt.winfo_screenwidth()
    h = rt.winfo_screenheight()
    # set title:
    rt.geometry("%dx%d" % (w, h))
    rt.title("NLP-SIMILARITY")
    # fonts:
    sFont = Font(family='Times New Roman', size='12')
    mFont = Font(family='Times New Roman', size='15')
    bFont = Font(family='Times New Roman', size='30')
    init_landing_page()
    rt.mainloop()
