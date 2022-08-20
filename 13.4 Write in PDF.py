# from fpdf import FPDF
#
# pdf = FPDF('P', 'mm', 'Letter')
#
# #Add Font
# # pdf.add_font('GIGI', '',r'C:\Windows\Fonts\GIGI.TTF', uni=True)
# pdf.add_font('MAHOUAMJ', '',r'C:\Users\haris\AppData\Local\Microsoft\Windows\Fonts\MAHOUAMJ.TTF', uni=True)
# # Add a page
# pdf.add_page()

# set style and size of font
# that you want in the pdf
# pdf.set_font("GIGI", '', size=15)
#
# # create a cell
# pdf.cell(200, 10, txt="GeeksforGeeks",
#          ln=1, align='C')
#
# # add another cell
# pdf.cell(200, 10, txt="A Computer Science portal for geeks.",
#          ln=2, align='C')
#




#
# file = open("File/myread.txt", "r", encoding="utf8")
#
# print(file.readable())
# text = file.read()
# print(text)
# print("Line: ", len(text))
# file.close()
#
#
# print(text.encode())
# pdf.set_font("MAHOUAMJ", '', size=25)
# pdf.cell(0,200, txt= text, ln=3, align='L', encodings = "utf8")
# # save the pdf with name .pdf
# pdf.output("File/myWrite.pdf")


from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

# Add a DejaVu Unicode font (uses UTF-8)
# Supports more than 200 languages. For a coverage status see:
# http://dejavu.svn.sourceforge.net/viewvc/dejavu/trunk/dejavu-fonts/langcover.txt
pdf.add_font('DejaVu', '', 'Fonts/DejaVuSansCondensed.ttf', uni=True)
pdf.set_font('DejaVu', '', 14)

text = u"""
English: Hello World
Greek: Γειά σου κόσμος
Polish: Witaj świecie
Portuguese: Olá mundo
Russian: Здравствуй, Мир
Vietnamese: Xin chào thế giới
Arabic: مرحبا العالم
Hebrew: שלום עולם
Bangla:  Zvc mfvcwZ KviY ‡Kvb n‡q‡Q ZvB kZvsk
"""

for txt in text.split('\n'):
    pdf.write(8, txt)
    pdf.ln(8)

# Add a Indic Unicode font (uses UTF-8)
# Supports: Bengali, Devanagari, Gujarati,
#           Gurmukhi (including the variants for Punjabi)
#           Kannada, Malayalam, Oriya, Tamil, Telugu, Tibetan
pdf.add_font('gargi', '', 'Fonts/gargi.ttf', uni=True)
pdf.set_font('gargi', '', 14)
pdf.write(8, u'Hindi: नमस्ते दुनिया')
pdf.ln(20)

# Add a AR PL New Sung Unicode font (uses UTF-8)
# The Open Source Chinese Font (also supports other east Asian languages)
pdf.add_font('fireflysung', '', 'Fonts/fireflysung.ttf', uni=True)
pdf.set_font('fireflysung', '', 14)
pdf.write(8, u'Chinese: 你好世界\n')
pdf.write(8, u'Japanese: こんにちは世界\n')
pdf.ln(10)

# Add a Alee Unicode font (uses UTF-8)
# General purpose Hangul truetype fonts that contain Korean syllable
# and Latin9 (iso8859-15) characters.
pdf.add_font('Nirmala', '', 'Fonts/Nirmala.ttf', uni=True)
pdf.set_font('Nirmala', '', 14)
pdf.write(8, u'Bangla:   তাপ সভাপতি কারণ কোন হয়েছে তাই শতাংশ')
pdf.ln(20)

#Bijoy font
pdf.add_font('SutonnyMJ Regular', '', 'Fonts/SutonnyMJ Regular.ttf', uni=True)
pdf.set_font('SutonnyMJ Regular', '', 14)
pdf.write(8, 'Zvc mfvcwZ KviY ‡Kvb n‡q‡Q ZvB kZvsk')
pdf.ln(20)

pdf.output("File/unicode.pdf", 'F')