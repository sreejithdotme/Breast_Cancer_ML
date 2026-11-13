import streamlit as st
import requests
import os

API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000/predict"
)

def get_auth_headers():

    # Authenticate only when running on Google Cloud Run
    if os.getenv("K_SERVICE"):

        token_url = (
            "http://metadata.google.internal/computeMetadata/v1/"
            "instance/service-accounts/default/identity"
        )

        audience = API_URL.rsplit("/", 1)[0]

        response = requests.get(
            token_url,
            params={
                "audience": audience,
                "format": "full"
            },
            headers={
                "Metadata-Flavor": "Google"
            },
            timeout=5
        )

        response.raise_for_status()

        return {
            "Authorization": f"Bearer {response.text}"
        }

    # Local development does not require Google authentication
    return {}


st.set_page_config(
    page_title="Breast Cancer Prediction",
    page_icon="🩺",
    layout="wide"
)
st.title("🩺 Breast Cancer Prediction System")

st.markdown("""
### Machine Learning-Based Classification

This application uses a trained Machine Learning model
to classify breast cancer samples as Benign or Malignant.

Enter the cell measurements to obtain a model prediction.
""")

st.divider()

st.subheader("Enter Cell Measurements")

col1, col2, col3 = st.columns(3)

with col1:
    clump_thickness = st.number_input("Clump Thickness", 1, 10, 5)
    cell_size = st.number_input("Uniformity of Cell Size", 1, 10, 5)
    cell_shape = st.number_input("Uniformity of Cell Shape", 1, 10, 5)

with col2:
    marginal_adhesion = st.number_input("Marginal Adhesion", 1, 10, 5)
    epithelial_size = st.number_input("Single Epithelial Cell Size", 1, 10, 5)
    bare_nuclei = st.number_input("Bare Nuclei", 1, 10, 5)

with col3:
    bland_chromatin = st.number_input("Bland Chromatin", 1, 10, 5)
    normal_nucleoli = st.number_input("Normal Nucleoli", 1, 10, 5)
    mitoses = st.number_input("Mitoses", 1, 10, 5)

st.divider()

if st.button("Predict Result", type="primary"):

    input_data = {
        "Clump_Thickness": clump_thickness,
        "Uniformity_Cell_Size": cell_size,
        "Uniformity_Cell_Shape": cell_shape,
        "Marginal_Adhesion": marginal_adhesion,
        "Single_Epithelial_Cell_Size": epithelial_size,
        "Bare_Nuclei": bare_nuclei,
        "Bland_Chromatin": bland_chromatin,
        "Normal_Nucleoli": normal_nucleoli,
        "Mitoses": mitoses
    }

    try:
        headers = get_auth_headers()

        response = requests.post(
            API_URL,
            json=input_data,
            headers=headers,
            timeout=30
        )

        response.raise_for_status()

        result = response.json()

        prediction = result["prediction"]
        malignant_probability = result["malignant_probability"]

        if prediction == "Malignant":
            st.error("Prediction: Malignant")
        else:
            st.success("Prediction: Benign")

        st.metric(
            label="Malignant Probability",
            value=f"{malignant_probability * 100:.2f}%"
        )

        st.progress(float(malignant_probability))

    except requests.exceptions.ConnectionError:
        st.error("Cannot connect to FastAPI. Please check whether the backend is running.")

    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {e}")

    st.divider()

st.subheader("Model Information")

st.write("**Algorithm:** Random Forest Classifier")
st.write("**Number of Estimators:** 300")
st.write("**Hyperparameter Tuning:** GridSearchCV")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Accuracy", "96.35%")
col2.metric("Precision", "92.31%")
col3.metric("Recall", "97.96%")
col4.metric("F1 Score", "95.05%")