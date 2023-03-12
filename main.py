import streamlit as st
import cv2
import datetime

st.header("Motion detector")
button = st.button("Start camera")

if button:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        current_time = datetime.datetime.now()
        weekday = current_time.strftime("%A")
        timestamp = current_time.strftime("%H:%M:%S")

        cv2.putText(img=frame, text=weekday, org=(50, 50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(255, 255, 255), thickness=2, lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text=timestamp, org=(50, 85),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

        streamlit_image.image(frame)
