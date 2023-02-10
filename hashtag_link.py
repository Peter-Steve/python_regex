import re

regex = lambda text : re.sub("#\w+",lambda match : "<a href=\"\">"+ str(match.group())+"</a>",text)
    
text = "Je suis allé sur #facebook après sur #whatsapp puis sur #instagram #."

print(regex(text))
