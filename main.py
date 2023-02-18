import requests
import streamlit as st
# commit: apod details image streamlit page Sec29

st.set_page_config(layout='centered')
st.header('NASA Astronomy Picture Of The Day')

api_key='HbLV6f3kWEyLtbTeooVIxEp4MEEJqY6qgAGqBop4'
# apod_url=f'https://api.nasa.gov/planetary/apod?api_key={api_key}'
apod_url=f'https://api.nasa.gov/planetary/apod?api_key={api_key}&count=1'

def get_response(url):
    try:
        response=requests.get(url=url)
    except:
        print(f'Failed to connect to url: {url}')
        exit()
    return(response)

response=get_response(url=apod_url)
content=response.json()
content=content[0]
# txt=f"{content['title']}\n{content['explanation']}\nAPOD: {content['date']}"

st.subheader(content['title'])
st.write(content['explanation'])
st.write(f"APOD: {content['date']}")

if content['media_type']=='image':
    img_url=content['hdurl']
    img_response=get_response(url=img_url)
    with open('tmp/image.png','wb') as file:
        file.write(img_response.content)
        print('Saved img file')
    st.image('tmp/image.png')
else:
    img_url=None

