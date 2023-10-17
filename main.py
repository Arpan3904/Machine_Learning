import pickle
import streamlit as st
import warnings


def recommend(news):
  index = news[news['title'] == selected_news].index[0]
  distances = sorted(list(enumerate(similarity[index])),
                     reverse=True,
                     key=lambda x: x[1])
  recommended_news_names = []
  for i in distances[1:6]:
    recommended_news_names.append(news.iloc[i[0]].title)
  return recommended_news_names


st.header('NEWS Recommender System')
news = pickle.load(open('news_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

news_list = news['title'].values
selected_news = st.selectbox("Type or select a news from the dropdown",
                             news_list)

if st.button('Show Recommendation'):
  recommended_news_names = recommend(news)
  for recommended_news_name in recommended_news_names:
    st.text(recommended_news_name)
