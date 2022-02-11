import yagmail
import time
import random

import streamlit as st

import pandas as pd

st.set_page_config(
    page_title= 'VEDA Email',
    page_icon= '🙂',
)

st.title('VEDA Email')

yag = yagmail.SMTP('thecustodien@gmail.com', 'Awesom3o', 'smtp.gmail.com')

recipients = pd.read_csv('./cb.csv')['email'].tolist()

message = 'Hello there,\n\nHappy Valentine\'s Day! I write to invite you to send your valentines this year using veda-amrita.herokuapp.com. It is completely pseudonymous. This platform supports the sharing of friendly and happy messages only - we do have a sentiment analysis bot checking every message before it gets sent.\n\nFun Fact: This was made in-house by a student.\n\nSincerely,\nThe Custodien'

notSent = []

for recipient in recipients:
  try:
    yag.send(to = recipient.lower() + '@cb.students.amrita.edu', subject = 'Meet VEDA', contents = message)
    st.write(f'Sent to {recipient}')
    sec = random.randrange(1, 60)
    time.sleep(sec)
  except:
    st.write(f'Not sent to {recipient}')
    notSent.append(recipient)
