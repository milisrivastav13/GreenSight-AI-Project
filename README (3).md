# ♻️ Title And Description
 GreenSight AI - Smart Waste Classification

“AI-Driven Waste Classification for a Cleaner, Greener Tomorrow”

Welcome to GreenSight AI! This project, created by Mili Srivastava, is a complete "Sustainability Platform" built in Python and Streamlit.

It's not just a simple AI model but an entire ecosystem built to teach and promote real-world "green skills." ♻️

This multi-functional web application identifies, educates, and empowers the user. The platform is built around a core AI classifier that instantly identifies waste, but it expands on this with several unique features.

# ✨ Key Features

🤖 AI Classifier: An AI model trained to identify waste as Biodegradable or Non-Biodegradable.

📸 Dual Input: Users can either upload an image file or use their live webcam for real-time classification.

🎮 Interactive Game: A "Sorting Challenge" game to test your knowledge by dragging and dropping waste into the correct bins.

🇮🇳 Local Recycling Guide: A built-in, 100% free guide with specific recycling rules for major Indian states.

📚 Educational Hub: The app includes tabs explaining:

National "Govt. Initiatives" for sustainability

Practical "Sustainable Tips"

An "About" section explaining why segregation is important.

🎨 Professional Branding: The project has a custom logo, a clear title, and a professional multi-tab layout.

# 🛠️ Tech Stack

graph TD

    A[🌱 GreenSight AI] --> B[Python];
    A --> C[Streamlit];
    A --> D[AI Model];
    A --> E[HTML/CSS/JS];

subgraph "Core Technologies"

    B[🐍 Python (Core Language)];
    C[🎈 Streamlit (Web Framework)];
    D --> TF[🧠 TensorFlow (ML Library)];
    D --> NP[🔢 Numpy (Data Processing)];
    D --> PIL[🖼️ Pillow (Image Processing)];
    E[🕹️ HTML/CSS/JS (Sorting Game)];
end

subgraph "Technology Roles"

    Python --> Logic[Core application logic & scripting];
    Streamlit --> UI[Renders all UI components, tabs, & inputs];
    TensorFlow --> Model[Loads & runs the `.h5` classification model];
    Pillow --> Images[Opens, resizes, & normalizes image files];
    Numpy --> Arrays[Converts processed images into arrays for the model];
    E --> Game[Provides interactive drag-and-drop game];
end

subgraph "Key Process Flow"

    Input(User Input<br/>Image/Webcam) --> PIL;
    PIL --> NP;
    NP --> TF;
    TF --> Output[Classification Result<br/>Bio / Non-Bio];
    Output --> Streamlit;
end


# 🚀 Deployment (NEW!)

This app is ready to be deployed on Streamlit Community Cloud (which is free!). Because the ecovision_model.h5 file is too large for a normal GitHub upload, you must use Git LFS (Large File Storage).

Step 1: Install Git LFS

First, you need to install Git LFS on your computer. You can download it from git-lfs.github.com.
After installing, run this command once in your terminal:

git lfs install


Step 2: Track Large Files

In your project folder, tell Git LFS which files to track.

git lfs track "*.h5"


This creates a new file called .gitattributes. You must commit this file.

Step 3: Add Files to Git

Add all your project files to git as you normally would.

# Add all your files
git add app.py


git add game.html


git add requirements.txt

git add greensight_logo.png

git add train_model.py

# Add your large model file

git add ecovision_model.h5


Step 4: Commit and Push

Now, commit and push your files to your GitHub repository. When you push, Git LFS will upload the .h5 file to LFS storage.

git commit -m "Add project files for deployment"
git push -u origin main


Step 5: Deploy on Streamlit Cloud

Go to share.streamlit.io and sign in with your GitHub account.

Click "New app".

Select your GitHub repository (GreenSight-AI-Project).

The "Main file path" should be app.py.

Click "Deploy!"

Streamlit will automatically read your requirements.txt file, install the libraries, download your model from Git LFS, and launch your app.

# ⚙️ Setup & Instructions (For Local Use)

1. Download Project Files (IMPORTANT)

The AI model and the game file are needed to run the app.

Download the Trained Model:
➡️ Download Model (ecovision_model.h5)
After downloading, place ecovision_model.h5 in the main project folder (next to app.py).

Download the Game File:
Make sure you have the game.html file in the same folder as app.py.

(Optional) Download the Dataset:
The dataset is only needed for training the model, not for running the app.
➡️ Download Dataset : https://www.kaggle.com/datasets/techsash/waste-classification-data


2. Install the Required Libraries

You will need the following Python libraries. You can install them using pip:

pip install streamlit tensorflow pillow numpy


3. Run the Streamlit App

Once the libraries are installed and the .h5 model & .html game files are in the correct folder, run this command in your terminal:

streamlit run app.py


The application will open automatically in your web browser. 🎈

# 📸 Screenshots
<img width="1920" height="1080" alt="Screenshot (494)" src="https://github.com/user-attachments/assets/84fab324-d920-4364-818b-ef075f82072a" />
<img width="1920" height="1080" alt="Screenshot (495)" src="https://github.com/user-attachments/assets/fe954fb3-3b9c-4e0f-9ea2-861e21504a27" />
<img width="1920" height="1080" alt="Screenshot (496)" src="https://github.com/user-attachments/assets/d4f44671-2e4a-41cc-a975-24854adaace5" />
<img width="1920" height="1080" alt="Screenshot (497)" src="https://github.com/user-attachments/assets/83220b48-5f5f-4367-a2ef-d4607b88654a" />
<img width="1920" height="1080" alt="Screenshot (498)" src="https://github.com/user-attachments/assets/8657f69c-4b36-4cb1-8414-4ab1d6a598d9" />
<img width="1920" height="1080" alt="Screenshot (499)" src="https://github.com/user-attachments/assets/ac7df74a-8854-4a93-a2d9-d53308967301" />
<img width="1920" height="1080" alt="Screenshot (500)" src="https://github.com/user-attachments/assets/ff457dda-abb3-4d40-8a58-5ac5962ed258" />
<img width="1920" height="1080" alt="Screenshot (501)" src="https://github.com/user-attachments/assets/fbc883bf-f14a-4e86-81b7-c797e8d3537a" />
# 🗺️ Future Roadmap

mindmap
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


Explanation of the Roadmap:

🌳 GreenSight AI - Future Vision (Central Hub): This is the core project, evolving into a more powerful and community-driven platform.

🧠 Core AI Model (Milestone 1): This layer focuses on making the "brain" of the app smarter and more capable than its current binary classification.

📦 Multi-Class Classification: Moving beyond "bio/non-bio" to identify specific materials.

🎯 Object Detection: Allowing the AI to find and identify multiple different waste items in a single photo.

📈 Accuracy Boost: Making the model more robust for real-world use.

📱 Application Features (Milestone 2): This layer is about enhancing the user's experience.

📍 Hyper-Local Recycling: Providing truly actionable advice based on the user's exact location.

🌍 Community & Deployment (Milestone 3): This layer focuses on getting the app into users' hands.

☁️ Live Deployment: Making the app publicly accessible.

📲 PWA Conversion: Improving mobile access by making it feel like a native app.

🔄 Feedback Loop: Empowering users to help train the AI.

 # FAQ (Frequently Asked Questions)

Question 1: Why do I need to download the ecovision_model.h5 file separately?

A: The trained model file is over 100MB, which is too large for GitHub's standard file storage. Hosting it on Google Drive is great for local use. For deployment (see above), we use Git LFS to handle this.

Question 2: I'm getting an error when I run streamlit run app.py. What's wrong?

A: The most common errors are:

Files not found: Make sure you have ecovision_model.h5 and game.html in the exact same folder as app.py.

Missing libraries: Ensure you have installed all the required libraries by running pip install streamlit tensorflow pillow numpy.

Question 3: What kind of images work best for classification?

A: For the best results, use a clear, well-lit image of a single item against a simple background.

Question 4: Is the recycling guide for my specific city?

A: Currently, the guide provides general recycling rules for major Indian states. Providing hyper-local, city-specific guidance is a key goal for a future update (see Milestone 2 in our Roadmap!).

# 💬 Feedback & Contributing

Your feedback and contributions are highly welcome!

🐛 Report a Bug: If you find a bug, please open an issue.

💡 Suggest a Feature: Have an idea? Open an issue to discuss it.

🧑‍💻 Make a Contribution: Feel free to fork the repository and submit a pull request.

# 🙏 Acknowledgements

This project was made possible by the invaluable resources and communities listed below. A special thank you to:

TensorFlow & Keras for the powerful and accessible deep learning tools.

The Streamlit team for making web app creation in Python so magical.

Kaggle and the creators of the waste datasets used for training this model.

All the open-source contributors whose libraries support this project.

# ✍️ Author

Mili Srivastava - @milisrivastav13

© 2025, Mili Srivastava. All rights reserved.

