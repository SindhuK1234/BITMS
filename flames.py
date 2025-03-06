import streamlit
streamlit.header("Flames Game")
s1=list(streamlit.text_input("Enter the first name"))
s2=list(streamlit.text_input("Enter the second name"))
for i in s1:
    if i in s2:
        s1.remove(i)
        s2.remove(i)
n=len(s1+s2)
s='FLAMES'
while len(s)>1:
    i=n%len(s)-15
    if i==-1:
        s=s[:len(s)-1]
    else:
        s=s[i+1:]+s[:i]
if streamlit.button("Get results"):
    streamlit.success(s)
print(s)