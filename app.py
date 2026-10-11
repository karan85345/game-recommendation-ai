import streamlit as st

st.set_page_config(page_title="AI Game Recommender", page_icon="🎮")

st.title("🎮 AI Game Recommendation")
st.write("Apna favourite game enter karo aur similar games ki recommendation pao!")

games = {
    "minecraft": ["Terraria", "Roblox", "Subnautica"],
    "free fire": ["PUBG Mobile", "Call of Duty Mobile", "Fortnite"],
    "fortnite": ["Apex Legends", "PUBG", "Call of Duty"],
    "gta v": ["Watch Dogs 2", "Red Dead Redemption 2", "Mafia"],
    "valorant": ["Counter-Strike 2", "Overwatch 2", "Apex Legends"],
    "pubg": ["Free Fire", "Call of Duty", "Fortnite"],
}

choice = st.text_input("Apna favourite game likho:")

if st.button("Recommend Games"):
    if choice.strip():
        recommendations = games.get(choice.strip().lower())

        if recommendations:
            st.subheader("Aapke liye recommended games:")
            for game in recommendations:
                st.write("🎯", game)
        else:
            st.warning("Is game ki recommendation abhi available nahi hai.")
    else:
        st.warning("Pehle apna favourite game likho!")