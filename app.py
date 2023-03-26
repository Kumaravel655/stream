import streamlit as st
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

# Load the pre-trained ResNet50 model
model = ResNet50(weights='imagenet')

# Define the Streamlit app
def app():
    # Set the page title
    st.title('Animal Classifier')
    
    # Create a file uploader for images
    uploaded_file = st.file_uploader('Choose an image', type=['jpg', 'jpeg', 'png'])
    
    # If an image is uploaded, display it and make a prediction
    if uploaded_file is not None:
        # Load the image and preprocess it
        img = image.load_img(uploaded_file, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        
        # Make a prediction using the model
        preds = model.predict(x)
        
        # Decode the prediction and display the result
        animal = decode_predictions(preds, top=1)[0][0][1]
        st.write('Predicted animal:', animal)

        # Display the uploaded image
        st.image(img, caption='Uploaded Image', use_column_width=True)
        
# Run the app
if __name__ == '__main__':
    app()
