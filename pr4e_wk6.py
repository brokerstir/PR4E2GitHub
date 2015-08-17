text = "X-DSPAM-Confidence:    0.8475";
pos = text.find(":")
ans = float(text[pos+1:]);
print ans