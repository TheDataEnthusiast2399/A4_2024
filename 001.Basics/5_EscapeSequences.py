"""
Escape characters or Escape sequences are used to insert the characters that are illegal in
string. 
\n -> New Line 
\t -> Tab
\" -> "
\' -> '
\b -> Backspace
\\ -> \
"""

txt = 'We are the so-called "Vikings" from the north.'
print(txt)
txt2 = "I'm \t vengeance \b of the Gotham City"
print(txt2)

# "a\\""bxy/\n"
print('"a\\\\"bxy/\\n"')
