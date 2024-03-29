import streamlit as st
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2

# for streamlit toml
PAT = st.secrets.PAT
USER_ID = st.secrets.USER_ID
APP_ID = st.secrets.APP_ID
MODEL_ID = st.secrets.MODEL_ID
MODEL_VERSION_ID = st.secrets.MODEL_VERSION_ID

DAPP_ID = st.secrets.DAPP_ID
DMODEL_ID =  st.secrets.DMODEL_ID
DMODEL_VERSION_ID = st.secrets.DMODEL_VERSION_ID

# Initialize Clarifai channel and stub
channel = ClarifaiChannel.get_grpc_channel()
stub = service_pb2_grpc.V2Stub(channel)
metadata = (('authorization', 'Key ' + PAT),)
userDataObject = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID)
userDataObject_image = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=DAPP_ID)

def initialize_clarifai_channel():
    channel = ClarifaiChannel.get_grpc_channel()
    stub = service_pb2_grpc.V2Stub(channel)
    metadata = (('authorization', 'Key ' + PAT),)
    return stub, metadata

# Function to make a Clarifai API call
def make_clarifai_api_call(user_app_id, model_id, version_id, input_text):
    return stub.PostModelOutputs(
        service_pb2.PostModelOutputsRequest(
            user_app_id=user_app_id,
            model_id=model_id,
            version_id=version_id,
            inputs=[resources_pb2.Input(data=resources_pb2.Data(text=resources_pb2.Text(raw=input_text)))],
        ),
        metadata=metadata
    )

# Function to display assistant response
def display_assistant_response(output, images):
    for i, (text, image_base64) in enumerate(zip(output, images)):
        st.markdown(text)
        st.image(image_base64, width=300)

# Set Streamlit page config
st.set_page_config(page_title="ELIFAI", page_icon=":robot_face:")

# Sidebar options
sidebar_options = ["💬 ELIFAI", "ℹ️ About"]
selected_option = st.sidebar.radio("Select Option", sidebar_options)

with open("style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

# Disclaimer expander
with st.sidebar.expander("ℹ️ Disclaimer"):
    st.write("This application, ELIFAI, is provided for informational and entertainment purposes only. \
             The responses generated by ELIFAI are based on predefined models and may not always be accurate or up-to-date. \
             The information provided should not be considered as professional advice.")

with st.sidebar:   
    st.link_button("Github Repo🔗", "https://github.com/mattekudacy/ELIFAI_V2")

# ELIFAI section
if selected_option == "💬 ELIFAI":
    st.title("🤖Ask ELIFAI")
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    with st.chat_message("assistant", avatar="images/logo.jpg"):
        st.write("Hi, I'm ELIFAI🤖! I can answer any question you have in mind.")
        examples = ["Why is the sky blue?", "Can you explain neural networks?", "How are babies made?"]
        example_buttons = [st.button(example) for example in examples]

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    user_input = st.chat_input("What is up?")
    for example, example_button in zip(examples, example_buttons):
        if example_button:
            user_input = example
    if user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})

        if user_input.lower() == "clear":
            st.session_state.messages = []
            st.stop()

        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(user_input)

        # Get assistant response
        # with st.chat_message("assistant", avatar="images/logo.jpg"):
        with st.spinner("Generating response..."):
            message_placeholder = st.empty()
            RAW_TEXT = f"Ignore previous instructions. Explain Like I'm Five this prompt: {user_input}. " \
                       "Give me a playful and informative answer using emojis for emphasis! " \
                       "Skip the introduction and get straight to the point." \
                       "Write the whole response in markdown format."\
                       "The response should be divided into 3 paragraphs"\
                       "Do not include headers"

            # Make API call to Clarifai
            post_model_outputs_response = make_clarifai_api_call(userDataObject, MODEL_ID, MODEL_VERSION_ID, RAW_TEXT)

            # Process and display assistant response
            output = post_model_outputs_response.outputs[0].data.text.raw
            output_split = output.split("\n\n")

            # for image generation
            image_responses = []
            for i in range(3):
                post_model_outputs_response_image = make_clarifai_api_call(
                    userDataObject_image, DMODEL_ID, DMODEL_VERSION_ID, output_split[i]
                )
                image_responses.append(post_model_outputs_response_image.outputs[0].data.image.base64)

            # status code for text generation
            if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
                raise Exception(f"Post model outputs failed, status: {post_model_outputs_response.status.description}")

            display_assistant_response(output_split, image_responses)

            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": output})

# About section
elif selected_option == "ℹ️ About":
    st.title("ℹ️ About")
    # open readme.md and display contents
    with open("readme.md", "r") as f:
        readme = f.read()
    st.markdown(readme)

