import streamlit as st
import requests


def request_recommendations(azure_uri, id_user):

    payload = {'code': '_fpxEYA8azXiJ-w6byYzDF4tvL8hqIsEKVEeW-iPwTLIAzFurQXbyQ=='}

    response = requests.request(
        method='GET', url=azure_uri+id_user, params=payload)

    if response.status_code != 200:
        return "Request failed with status {}, {}".format(response.status_code, response.text)

    return response.json()


def main():
    AZURE_URI = 'https://p9recos.azurewebsites.net/api/'

    st.title('Article recommendations')

    id_user = st.text_input('id_user')

    recommend_btn = st.button('Get recommendations')
    if recommend_btn:
        reco = None
        reco = request_recommendations(AZURE_URI, id_user)
        st.write(reco)


if __name__ == '__main__':
    main()
