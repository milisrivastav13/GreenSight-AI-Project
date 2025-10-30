GreenSight AI - Smart Waste Classification

“AI-Driven Waste Classification for a Cleaner, Greener Tomorrow”

This is the Week 1 Milestone for the AI for Green Skills project by Mili Srivastava.

About The Project

GreenSight AI is a complete "Sustainability Platform" built in Python and Streamlit. It is not just a simple AI model but an entire ecosystem built to teach and promote real-world "green skills."

It is a multi-functional web application that identifies, educates, and empowers the user. The platform is built around a core AI classifier that instantly identifies waste, but it expands on this with several unique features:

AI Classifier: An AI model trained to identify waste as Biodegradable or Non-Biodegradable.

Dual Input: Users can either upload an image file or use their live webcam for real-time classification.

Local Recycling Guide: A built-in, 100% free guide with specific recycling rules for major Indian states, making the AI's advice actionable.

Educational Hub: The app includes tabs explaining national "Govt. Initiatives" for sustainability, practical "Sustainable Tips," and the "About" section explaining why segregation is important.

Professional Branding: The project has a custom logo, a clear title, and a professional multi-tab layout.

How to Run This Project

1. Download the Trained Model (IMPORTANT)

The AI model file (ecovision_model.h5) is too large for GitHub.

You can download the trained model file from this Google Drive link:

https://drive.google.com/file/d/1xo6eK1V3VdEsqLC6ZkANSS1n8YTpBJm2/view?usp=sharing

After downloading, place the ecovision_model.h5 file in the same main folder as app.py.

2. Install the Required Libraries

You will need the following Python libraries. You can install them using pip:

pip install streamlit tensorflow pillow numpy


(You can also find these listed in the requirements.txt file).

3. Run the Streamlit App

Once the libraries are installed and the .h5 model file is in the correct folder, run the following command in your terminal:

streamlit run app.py


The application will open automatically in your web browser.

© 2025, Mili Srivastava. All rights reserved.