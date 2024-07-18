import streamlit as st 
import requests


def fetch_data():
    with st.spinner("Working..."):
        api_url = "https://api.freeapi.app/api/v1/public/randomproducts/product/random"

        response = requests.get(url=api_url)

        if response.status_code == requests.codes.ok:
            data =  response.json()
            status = "OK"
        else:
            data = {"code": response.status_code, "message": response.text}
            status = "ERROR"

        return data,status
    

def main():
    st.title("Random Product Generator")

    if st.button("Generate"):
        data,status = fetch_data()

        if status == "OK":
            st.success("Data fetched successfully!")
            st.subheader("Random Product : ")
            st.write(f'## {data['data']['title']}')
            
        else:
            st.error(f"Failed to fetch data. Status code: {data['code']}")
            st.write("Error message:")
            st.write(data['message'])


if __name__ == '__main__':
    main()
