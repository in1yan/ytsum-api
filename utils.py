import google.generativeai as ai
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
import os




def summarize(script):
    ai.configure(api_key=os.environ["gen_key"])

    model = ai.GenerativeModel('gemini-1.5-flash')
    res = model.generate_content(f"""
                                 summarize the following text and extract the key points
                                 , if possible add wikipedia links to concepts and create a output in 
                                 markdown syntax such that the summary should be first and the key point should be next.
                                 if possible write the code examples in a seperate section. 
                                 the key point section should follow this template:
                                - *key point name*:description. here is the text : {script}""")
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
