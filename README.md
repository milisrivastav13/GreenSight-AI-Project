
# Project Title

*🌱 GreenSight AI - Smart Waste Classification
“AI-Driven Waste Classification for a Cleaner, Greener Tomorrow”*

Welcome to GreenSight AI! This project, created by Mili Srivastava, is a complete **"Sustainability Platform"** built in Python and Streamlit.

It's not just a simple AI model but an entire ecosystem built to teach and promote real-world "green skills." ♻️

This multi-functional web application identifies, educates, and empowers the user. The platform is built around a core AI classifier that instantly identifies waste, but it expands on this with several unique features.


## Features

**🤖 AI Classifier:** An AI model trained to identify waste as Biodegradable or Non-Biodegradable.

**📸 Dual Input:** Users can either upload an image file or use their live webcam for real-time classification.

**🇮🇳 Local Recycling Guide:** A built-in, 100% free guide with specific recycling rules for major Indian states, making the AI's advice actionable.

**📚 Educational Hub:** The app includes tabs explaining:

National "Govt. Initiatives" for sustainability

Practical "Sustainable Tips"

An "About" section explaining why segregation is important.

**🎨 Professional Branding:** The project has a custom logo, a clear title, and a professional multi-tab layout.


## Roadmap


    
    root((GreenSight AI - Future Vision 🌳))
    Core AI Model (Milestone 1) 🧠
      Multi-Class Classification 📦
        (e.g., Glass, Plastic, Paper, Metal, Organic, E-Waste)
      Object Detection 🎯
        (Bounding boxes for multiple items in one photo)
      Accuracy Boost 📈
        (Fine-tuning with larger, real-world datasets)
    Application Features (Milestone 2) 📱
      Hyper-Local Recycling 📍
        (Pincode/City-level rules & depot locations)
      User Impact Tracking 📊
        (Personal dashboard to gamify sorting & see positive impact)
    Community & Deployment (Milestone 3) 🌍
      Live Deployment ☁️
        (Streamlit Community Cloud for public web access)
      PWA Conversion 📲
        ("Installable" app for mobile home screens)
      Feedback Loop 🔄
        ("Report Incorrect Classification" button for new training data)



**Explanation of the Roadmap:**

**🌳 GreenSight AI - Future Vision (Central Hub):** This is the core project, evolving into a more powerful and community-driven platform.

**🧠 Core AI Model (Milestone 1)**: This layer focuses on making the "brain" of the app smarter and more capable than its current binary classification.

**📦 Multi-Class Classification:** Moving beyond "bio/non-bio" to identify specific materials, which is key for proper recycling.

**🎯 Object Detection:** Allowing the AI to find and identify multiple different waste items in a single, complex photo.

**📈 Accuracy Boost:** Making the model more robust for real-world use by training it on "messy" data.

**📱 Application Features (Milestone 2):** This layer is about enhancing the user's experience and making the app's advice more actionable and engaging.

**📍 Hyper-Local Recycling:** Providing truly actionable advice based on the user's exact location, not just their state.





**🌍 Community & Deployment (Milestone 3):** This layer focuses on getting the app into users' hands and creating a self-improving system.

**☁️ Live Deployment:** Making the app publicly accessible to anyone with a web browser.

**📲 PWA Conversion:** Improving mobile access by making it feel like a native app.

**🔄 Feedback Loop:** Empowering users to help train the AI, creating a virtuous cycle of improvement.




## Tech Stack
graph TD

    A[🌱 GreenSight AI] --> B[Python];
    A --> C[Streamlit];
    A --> D[AI Model];

subgraph "Core Technologies"

    B[🐍 Python (Core Language)];
    C[🎈 Streamlit (Web Framework)];
    D --> TF[🧠 TensorFlow (ML Library)];
    D --> NP[🔢 Numpy (Data Processing)];
    D --> PIL[🖼️ Pillow (Image Processing)];


subgraph "Technology Roles"

    Python --> Logic[Core application logic & scripting];
    Streamlit --> UI[Renders all UI components, tabs, & inputs];
    TensorFlow --> Model[Loads & runs the `.h5` classification model];
    Pillow --> Images[Opens, resizes, & normalizes image files];
    Numpy --> Arrays[Converts processed images into arrays for the model];


subgraph "Key Process Flow"

    Input(User Input<br/>Image/Webcam) --> PIL;
    PIL --> NP;
    NP --> TF;
    TF --> Output[Classification Result<br/>Bio / Non-Bio];
    Output --> Streamlit;



## Setup & Instructions

1. Download the Trained Model (IMPORTANT)

The AI model file (ecovision_model.h5) is too large for GitHub.
You can download the trained model file from this Google Drive link:

➡️https://drive.google.com/file/d/1xo6eK1V3VdEsqLC6ZkANSS1n8YTpBJm2/view?usp=sharing from Google Drive

After downloading, place the ecovision_model.h5 file in the same main folder as app.py.

2. Install the Required Libraries

You will need the following Python libraries. You can install them using pip:

**pip install streamlit tensorflow pillow numpy**



3. Run the Streamlit App

Once the libraries are installed and the .h5 model file is in the correct folder, run the following command in your terminal:

**streamlit run app.py**


*The application will open automatically in your web browser. 🎈*
## Screenshots
<img width="1920" height="1080" alt="Screenshot (485)" src="https://github.com/user-attachments/assets/121258d6-cedc-4cc5-8edd-5cd474dab28e" />
<img width="1920" height="1080" alt="Screenshot (486)" src="https://github.com/user-attachments/assets/38f453a0-c33b-46bb-bba1-187abdc74406" />

<img width="1920" height="1080" alt="Screenshot (487)" src="https://github.com/user-attachments/assets/33b9b67e-effb-493d-83f4-7dbe6ad29026" />
<img width="1920" height="1080" alt="Screenshot (488)" src="https://github.com/user-attachments/assets/48242bab-3d53-484e-a0ed-86a2c0be5ebe" />




<img width="1920" height="1080" alt="Screenshot (489)" src="https://github.com/user-attachments/assets/161c92fc-7187-4ad7-b5ce-170785846c18" />

## FAQ

#### Question 1: Why do I need to download the ecovision_model.h5 file separately?
A: The trained model file is over 100MB, which is too large for GitHub's standard file storage. Hosting it on Google Drive ensures anyone can download and run the project.

#### Question 2: I'm getting an error when I run streamlit run app.py. What's wrong?
A: The most common errors are:

Model not found: Make sure you have placed the ecovision_model.h5 file in the exact same folder as app.py.

Missing libraries: Ensure you have installed all the required libraries by running pip install streamlit tensorflow pillow numpy.

#### Question 3: What kind of images work best for classification?
A: For the best results, use a clear, well-lit image of a single item against a simple background. The model is trained to classify one item at a time.

#### Question 4: Is the recycling guide for my specific city?
A: Currently, the guide provides general recycling rules for major Indian states. Providing hyper-local, city-specific, and pincode-level guidance is a key goal for a future update (see Milestone 2 in our Roadmap!).







## Feedback

*💬 Feedback & Contributing*

Your feedback and contributions are highly welcome!

🐛 Report a Bug: If you find a bug, please open an issue on my git ID .

💡 Suggest a Feature: Have an idea to make GreenSight AI better? Open an issue to discuss it.

🧑‍💻 Make a Contribution: Feel free to fork the repository and submit a pull request.

## Acknowledgements

This project was made possible by the invaluable resources and communities listed below. A special thank you to:

**TensorFlow** & **Keras** for the powerful and accessible deep learning tools.

The **Streamlit team** for making web app creation in Python so magical.

**Kaggle** and the **creators of the waste datasets** used for training this model.

All the open-source contributors whose libraries support this project.




## Authors

This project was created by:

*Mili Srivastava* 

GitHub: @milisrivastav13
