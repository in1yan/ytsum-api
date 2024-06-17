import google.generativeai as ai
from youtube_transcript_api import YouTubeTranscriptApi

import os




def summarize(text):
    ai.configure(api_key=os.environ["gen_key"])

    model = ai.GenerativeModel('gemini-1.5-flash')

    res = model.generate_content(f"""
                                 summarize the following text and extract the key points
                                 , if possible add wikipedia links to concepts and create a output in 
                                 markdown syntax such that the summary should be first and the key point should be next.
                                 if possible write the code examples in a seperate section. 
                                 the key point section should follow this template:
                                - *key point name*:description. here is the text : {text}""")
    return res.text

def transcript(url):
    id = url.split('v=')[1]
    data = YouTubeTranscriptApi.get_transcript(id)
    transcript=""
    for script in data:
        transcript += script["text"]
    return transcript
if __name__ == '__main__':
    res = transcript('https://www.youtube.com/watch?v=Xly7lpTQELI')
    print(summarize(res))
