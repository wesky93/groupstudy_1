#6_5

text = "X-DSPAM-Confidence: 0.8475"
num = text.index(":")+1
export_text = text[num:]
trans = float(export_text.strip())
print (trans,type(trans))
