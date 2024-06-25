import google.generativeai as ai
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
import os




def summarize(script):
    ai.configure(api_key=os.environ["gen_key"])

    model = ai.GenerativeModel('gemini-1.5-flash')
    res = model.generate_content(f"""
                                 summarize the following text and extract the key points and include inline codes where it is necessary
                                 ,create a output in 
                                 markdown syntax such that it follow the following template: 
                                 ## summary
                                 // summary text here important words should be in bold
                                 ## key points
                                 // key points and their explanation with links
                                 - **key point**: explanation
                                 ## Code examples
                                 // if the video is not related to coding ignore this section
                                 ## Resource links
                                 // internet resource links
                                 . here is the text : {script}""")
    return res.text

def transcript(url):
    video = YouTube(url)
    id = video.video_id
    thumbnail = video.thumbnail_url
    title = video.title
    raw_transcript = YouTubeTranscriptApi.get_transcript(id)
    transcript=""
    for script in raw_transcript:
        transcript += script["text"]
    data = {
        "title":title,
        "thumbnail":thumbnail,
        "transcript":transcript
    }
    return data
if __name__ == '__main__':
    res = transcript('https://www.youtube.com/watch?v=Xly7lpTQELI')
    print(summarize(res))
