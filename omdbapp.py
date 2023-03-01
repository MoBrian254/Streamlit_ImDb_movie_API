import requests
import streamlit as st
from keys import api

st.header('IMDB MOVIES DATABASE | MoBrian254 Demo')
movie = st.text_input('Enter movie title and press Enter')

if movie:
    try:
        url = f"http://www.omdbapi.com/?t={movie}&apikey={api}"
        r = requests.get(url)
        r = r.json()

        col1, col2 = st.columns([2, 3])
        with col1:
            st.image(r['Poster'])

        with col2:
            st.subheader(r['Title'])
            st.text(f"Ratings: {r['imdbRating']} | Duration: {r['Runtime']} | Rated: {r['Rated']}")
            st.progress(float(r['imdbRating']) / 10)
            st.caption(f"Genre: {r['Genre']}")
            st.caption(f"Released: {r['Released']} | BoxOffice: {r['BoxOffice']}")
            st.text(f"Website: {r['Website']}")
            st.text(f"Writers: {r['Writer']}")
            st.text(f"Actors: {r['Actors']}")
            st.write(r['Plot'])

    except:
        st.error('Found no results...')

git = 'https://github.com/MoBrian254'
linkdin = 'https://www.linkedin.com/in/brian-owana-web-developer/'
portfolio = 'https://mobrian-portfolio-01.vercel.app/'
st.markdown(f"<span>Follow me: <a href={git} target='_blank'>@Github</a> | <a href='{linkdin}' target='_blank'>@LinkedIn</a> | <a href='{portfolio}' target='_blank'>@Portfolio</a></span>", unsafe_allow_html=True)
