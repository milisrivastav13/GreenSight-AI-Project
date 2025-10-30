import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import os
import random

logo_path = "greensight_logo.png" 
st.set_page_config(
    page_title="GreenSight AI: Smart Waste Classification",
    page_icon=logo_path if os.path.exists(logo_path) else "♻️", 
    layout="centered"
)


MODEL_PATH = 'ecovision_model.h5'


@st.cache_resource
def load_model():
    """Loads the trained Keras model."""
    if not os.path.exists(MODEL_PATH):
        
        st.error(f"Error: Model file not found at {MODEL_PATH}")
        st.write("Please run `python train_model.py` to train and save the model.")
        st.stop()
        
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.stop()

model = load_model()



BIO_TIPS = [
    "This item is **biodegradable**! You can add it to your **compost bin** to create nutrient-rich soil.",
    "Composting this item reduces landfill waste and methane emissions.",
    "Did you know? Biodegradable items can break down naturally without harming the environment."
]

NON_BIO_TIPS = [
    "This item is **not compostable**. Please place it in the **recycling bin** if it's clean plastic, glass, or metal.",
    "Recycling this item saves energy and natural resources. Check your local recycling guidelines!",
    "Many non-biodegradable items can be repurposed! Can this be a new container or part of a craft project?"
]



def predict_waste(image_data, model):
    """
    Preprocesses the image and returns a prediction and confidence.
    """
    
    size = (150, 150) 
    
   
    image = ImageOps.fit(image_data, size, Image.Resampling.LANCZOS)
    
   
    image_array = np.asarray(image)
    
  
    normalized_image_array = (image_array.astype(np.float32) / 255.0) 
    
    
    data = np.expand_dims(normalized_image_array, axis=0)
    
   
    prediction = model.predict(data)
    
   
    confidence = prediction[0][0]
    
   
    
    if confidence > 0.5:
        return "Non-Biodegradable", confidence
    else:
        return "Biodegradable", (1 - confidence)


if os.path.exists(logo_path):
    st.image(logo_path, width=200)
else:
    st.title("♻️ GreenSight AI") 
st.title("GreenSight AI")
st.subheader("“AI-Driven Waste Classification for a Cleaner, Greener Tomorrow”")


tab1, tab2, tab3, tab4 = st.tabs(["🤖 AI Classifier", "ℹ️ Local Recycling Guide", "🌍 About This Project", "🇮🇳 Govt. Initiatives"])

with tab1:
    st.markdown(
        "Upload an image or use your webcam, and the AI will classify your waste item."
    )
    
   
    sub_tab1, sub_tab2 = st.tabs(["⬆️ Upload Image", "📸 Use Webcam"])
    uploaded_image = None

    with sub_tab1:
        file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], key="uploader")
        if file:
            uploaded_image = Image.open(file)

    with sub_tab2:
        cam_file = st.camera_input("Take a picture of the waste item", key="camera")
        if cam_file:
            uploaded_image = Image.open(cam_file)


    if uploaded_image is not None:
        image = uploaded_image

       
        st.image(image, caption='Uploaded Image', use_container_width=True)
        
        
        with st.spinner("Classifying..."):
            
            label, confidence = predict_waste(image, model)

       
        if label == "Non-Biodegradable":
          
            st.error(f"**Prediction: ♻️ {label}**")
            
            st.progress(float(confidence), text=f"Confidence: {confidence*100:.2f}%")
            
            st.subheader("Eco-Friendly Tip 💡")
            st.warning(random.choice(NON_BIO_TIPS))
        else:
           
            st.success(f"**Prediction: 🌿 {label}**")
            
            st.progress(float(confidence), text=f"Confidence: {confidence*100:.2f}%")
            
            st.subheader("Eco-Friendly Tip 💡")
            st.info(random.choice(BIO_TIPS))



with tab2:
    st.subheader("Local Recycling Guide")
    st.markdown("Recycling rules change. Select your state/city for general guidelines.")
    
    
    RECYCLING_GUIDES = {
        
        "Delhi (NCR)": {
            "text": """
            - **General:** Delhi has multiple municipal bodies (NDMC, SDMC, EDMC), so rules can vary slightly.
            - **Plastics:** Most hard plastics (types 1, 2, 5) are accepted if clean. Avoid thin plastic bags.
            - **E-Waste:** Must be disposed of at dedicated e-waste collection centers. Do not mix with regular trash.
            - **Local Insight:** E-waste is a major challenge in Delhi, often handled by the informal sector. Your effort to use dedicated e-waste bins makes a huge difference.
            """
        },
        "Maharashtra (Mumbai)": {
            "text": """
            - **General:** BMC manages waste. A strong "Dry Waste" vs "Wet Waste" segregation is enforced.
            - **Plastics:** Only hard plastics (PET, HDPE - types 1, 2) are widely recycled.
            - **Paper:** All clean paper and cardboard are recycled. Must be dry.
            - **Local Insight:** Mumbai's success relies on citizens separating wet (food) and dry (recyclables) waste *before* collection.
            """
        },
        "Karnataka (Bengaluru)": {
            "text": """
            - **General:** BBMP mandates a strict **2-bin, 1-bag** system, a model for the country.
            - **Wet Waste (Green Bin):** All biodegradable items (food, garden waste, etc.).
            - **Dry Waste (Blue Bin):** Paper, plastic, metal, glass. Must be clean and dry.
            - **Reject Waste (Red Bag):** Soiled items, sanitary waste, diapers, etc. This goes to the landfill.
            - **Local Insight:** Bengaluru's system is very specific. Your biggest impact is keeping "Reject Waste" separate from "Dry Waste" to avoid contaminating recyclables.
            """
        },
        "Tamil Nadu (Chennai)": {
            "text": """
            - **General:** The Corporation encourages source segregation, with a focus on composting wet waste.
            - **Plastics:** Focus on plastic bottles (PET) and containers.
            - **Glass:** Clear and colored glass bottles are accepted.
            - **Local Insight:** Chennai has a strong network of neighborhood composting centers that process local wet waste. Supporting these is key.
            """
        },
        "West Bengal (Kolkata)": {
            "text": """
            - **General:** KMC is increasing its focus on segregation, but it is still catching up to other metro cities.
            - **Plastics:** PET bottles (type 1) are widely recycled.
            - **E-Waste:** Several collection points are set up, but public awareness is growing.
            - **Local Insight:** Public participation in segregation is the biggest hurdle. Leading by example in your community can drive change.
            """
        },
        "Gujarat (Ahmedabad)": {
            "text": """
            - **General:** AMC has one of the most successful door-to-door segregated waste collection systems.
            - **Dry Waste:** Includes paper, plastic, glass, and metal.
            - **Wet Waste:** Includes kitchen and food waste.
            - **Local Insight:** The success in Ahmedabad is due to a highly efficient collection fleet. The main job for citizens is to have their two (dry/wet) bins ready.
            """
        },
        "Punjab (Chandigarh)": {
            "text": """
            - **General:** As a planned city, Chandigarh has a well-regarded waste management system with high processing rates.
            - **Segregation:** Door-to-door segregated collection (dry/wet) is strictly implemented.
            - **Compost:** A large composting plant processes the majority of the city's wet waste.
            - **Local Insight:** Chandigarh's system works well because of good infrastructure and high citizen compliance.
            """
        }
    }

 
    location = st.radio("Select your location:", options=list(RECYCLING_GUIDES.keys()), index=0)

   
    if location != "Select a Location":
        guide_info = RECYCLING_GUIDES[location]
        st.info(guide_info["text"])
        

with tab3:
   
    st.subheader("About GreenSight AI")
    st.info(
        "GreenSight AI is an AI-powered tool built to promote sustainable waste management. "
        "It uses a Convolutional Neural Network (CNN) trained with TensorFlow/Keras "
        "to classify waste from images."
    )
    
 
    st.subheader("Project Built With:")
    st.markdown(
        """
        - Python
        - TensorFlow & Keras
        - Streamlit
        - PIL & NumPy
        """
    )


    st.divider()
    st.subheader("🌱 How You Can Help Make Earth More Sustainable")
    st.markdown(
        """ 
        - **Start with the 3 R's:** First **Reduce** what you buy, then **Reuse** what you can (like bags and containers), and *then* **Recycle**.
        - **Compost at Home:** If you have space, composting your food scraps creates amazing soil for plants and keeps waste out of landfills.
        - **Save Water:** Simple acts like fixing leaky taps and taking shorter showers can save thousands of liters of water per year.
        - **Save Energy:** Turn off lights and electronics when you're not using them. Switch to LED bulbs, which use up to 80% less energy.
        - **Eat Local, Waste Less:** Try to eat food that is grown locally to reduce transport emissions. Plan your meals to avoid food waste.
        """
    )
    
  
    st.divider()
    with st.expander("🌍 Why is waste segregation important?"):
        st.markdown("""
            - **Reduces Landfill:** Proper sorting keeps biodegradable waste out of landfills, where it would produce methane, a potent greenhouse gas.
            - **Boosts Recycling:** It keeps recyclable materials (like plastic, glass) clean and ready to be made into new products.
            - **Creates Compost:** Biodegradable waste can be composted to create nutrient-rich soil, helping gardens and farms.
            - **Protects Environment:** It prevents soil and water pollution from hazardous waste.
        """)


with tab4:
    st.subheader("India's Commitment to Sustainable Development")
    st.markdown("""
    India's government policies for sustainable development focus on implementing the 
    Sustainable Development Goals (SDGs) through various flagship programs in social, 
    economic, and environmental sectors.
    """)
    st.info("""
    Key policies include the Swachh Bharat Mission for sanitation, Pradhan Mantri Awas 
    Yojana for housing, National Action Plan on Climate Change for ecological 
    sustainability, and Pradhan Mantri Jan Dhan Yojana for financial inclusion, 
    alongside efforts to increase renewable energy capacity and track progress 
    through the SDG India Index, as reported by NITI Aayog.
    """)
    
    st.divider()

    with st.expander("🏡 Social and Economic Development"):
        st.markdown("""
        - **Swachh Bharat Mission (SBM):** Aims to improve sanitation and cleanliness across the country.
        - **Pradhan Mantri Awas Yojana (PMAY):** Provides housing for the urban and rural poor.
        - **Pradhan Mantri Jan Dhan Yojana (PMJDY):** A financial inclusion program that provides access to banking, insurance, and other financial services.
        - **Pradhan Mantri Ujjwala Yojana (PMUY):** Provides LPG connections to women in below-poverty-line households.
        - **Ayushman Bharat-PMJAY:** A health insurance scheme to provide financial protection for health expenses.
        - **National Food Security Act:** GuaranteES food security for the population.
        """)

  
    with st.expander("☀️ Environmental and Climate Action"):
        st.markdown("""
        - **National Action Plan on Climate Change:** Outlines a national framework for addressing climate change through both adaptation and mitigation.
        - **Renewable Energy Expansion:** Significant focus on increasing the capacity of non-fossil fuel-based power generation, with a target of 500 GW by 2030.
        - **Smart Cities Mission:** Aims to develop sustainable and citizen-friendly cities.
        - **Atal Mission for Rejuvenation and Urban Transformation (AMRUT):** Aims to improve basic urban infrastructure like water supply and sanitation.
        """)

   
    with st.expander("📊 Governance and Monitoring"):
        st.markdown("""
        - **NITI Aayog SDG India Index:** A tool to track the progress of states and union territories on various SDG indicators, fostering competition and enabling informed policy-making.
        - **Direct Benefit Transfers (DBT):** Leveraging programs like PMJDY, the government uses a direct cash transfer system to improve the efficiency of program delivery.
        """)


if os.path.exists(logo_path):
    st.sidebar.image(logo_path, use_container_width=True) 
st.sidebar.title("GreenSight AI")
st.sidebar.markdown("A Smart Waste Classifier")
st.sidebar.divider()

st.sidebar.subheader("Our Mission")
st.sidebar.info(
    "To empower individuals and communities with smart, accessible tools that "
    "promote sustainable habits and drive real-world environmental action."
    "Leveraging deep learning and computer vision, GreenSight EcoVision classifies household and municipal waste into biodegradable and non-biodegradable types — empowering sustainable practice and smarter recycling."
)

st.sidebar.divider()


st.sidebar.caption("© 2025, Mili Srivastava. All rights reserved.")