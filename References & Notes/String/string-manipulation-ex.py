#Write code using find() and string slicing (see section 6.10) to extract the 
#number at the end of the line below. Convert the extracted value to a floating 
#point number and print it out. text = "X-DSPAM-Confidence:    0.8475";

text = "X-DSPAM-Confidence:    0.8475"
length = text.__len__()
colonPosition = text.find(':')
extractedValue = text[colonPosition+1:length]
float_ExtractedValue = float(extractedValue)
print(float_ExtractedValue)