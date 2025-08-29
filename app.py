import streamlit as st
from agent import track_search
from pathlib import Path

# page configuration
st.set_page_config(
    page_title="VibeSmith 🎧",
    page_icon="🎵",
    layout="wide"
)

# load external CSS
def load_css(file_name: str):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

# title and subtitle
st.markdown("""
<div class="title-container">
    <h1>🎧 VibeSmith - AI Playlist Curator</h1>
</div>
<p class="subtitle">Generate Spotify playlists based on your mood, vibe, or theme!</p>
""", unsafe_allow_html=True)

# input section
with st.container():
    prompt = st.text_input(
        "Describe the vibe for your playlist:",
        placeholder="e.g., Chill evening lofi beats"
    )
    num_tracks = st.slider(
        "Number of tracks",
        min_value=1,
        max_value=20,
        value=6
    )
    generate_btn = st.button("Generate Playlist 🎵")
    

# playlist results 
if generate_btn:
    if not prompt:
        st.error("Please enter a vibe or theme!")
    else:
        with st.spinner("Curating your playlist..."):
            tracks = track_search(prompt, limit=num_tracks)
            
            if tracks:
                st.markdown('<h3 class="playlist-header">Playlist</h3>', unsafe_allow_html=True)
                
                num_cols = 3 if num_tracks >= 3 else num_tracks
                for row_start in range(0, len(tracks), num_cols):
                    row_tracks = tracks[row_start:row_start + num_cols]
                    cols = st.columns(num_cols)

                    for i, t in enumerate(row_tracks):
                        with cols[i % num_cols]:
                            album_img = t.get("album_art_url")
                            if album_img:
                                st.markdown(
                                    f'<img src="{album_img}" class="album-img" width="180"/>',
                                    unsafe_allow_html=True
                                )
                            st.markdown(
                                f'''
                                <div class="track-text">
                                    <strong>{t['name']}</strong><br>
                                    {t['artist']}<br>
                                    <a href="{t['url']}">Listen on Spotify</a>
                                </div>
                                ''',
                                unsafe_allow_html=True
                            )
                    st.markdown('<div style="margin-bottom:30px;"></div>', unsafe_allow_html=True)
            else:
                st.warning("No tracks found for this prompt.")
