import streamlit as st

import requests
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
from IPython.display import YouTubeVideo

######################################################################
def youtube_transcript(youtube_video):
    video_id = youtube_video.split("=")[1]
    YouTubeVideo(video_id)
    YouTubeTranscriptApi.get_transcript(video_id)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    result = ""
    for i in transcript:
        result += ' ' + i['text']
    # print(result)
    print(len(result))
    return result


st.cache(allow_output_mutation=True)
def transformer_summarizer(result):
    summarizer = pipeline('summarization')
    num_iters = int(len(result) / 1000)
    summarized_text = []
    for i in range(0, num_iters + 1):
        start = 0
        start = i * 1000
        end = (i + 1) * 1000
        out = summarizer(result[start:end])
        out = out[0]
        out = out['summary_text']
        summarized_text.append(out)
        return summarized_text
######################################################################


def main():

    html_temp = """
        <div style="background-color:pink;padding:10px">
        <h2 style="color:white;text-align:center;">YouTube Video Transcript Summarizer</h2>
        </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.markdown("""
        	#### Description
        	+ This is a Natural Language Processing(NLP) Based App useful for YouTube Video Transcript Summarization
        	""")
    st.subheader('Please enter the YouTube video link for summarization')

    #st.text_input('Please enter the news article link for summarization')
    #message = st.text_area("Enter Text","Type Here ..")

    youtube_video = st.text_input("Youtube Video Link", )
    result = ""
    #num_lines=50
    if st.button("Predict"):
        #with st.spinner("summarizing the text please wait"):
        video_text = youtube_transcript(youtube_video)
        result = transformer_summarizer(video_text)
        st.success('The output is {}'.format(result))
    if st.button(""):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")


if __name__ == '__main__':
    main()
    #app.run_server(debug=True)