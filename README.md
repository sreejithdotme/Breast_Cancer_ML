# Breast Cancer Classification Using Machine Learning

An end-to-end Machine Learning application that classifies breast cancer samples as **Benign or Malignant** using the Wisconsin Breast Cancer Original dataset.

The project combines a trained Random Forest classification pipeline with a Streamlit frontend, FastAPI backend, Docker containerization, and Google Cloud Run deployment.


## 1. Project Overview

The objective of this project is to develop an end-to-end Machine Learning application that accepts cell measurements and predicts whether a breast cancer sample is benign or malignant.

The application uses nine numerical features from the Wisconsin Breast Cancer Original dataset.

The trained Machine Learning pipeline is served through a FastAPI backend, while users interact with the model through a Streamlit web interface.

### Key Features

- Data inspection and preprocessing.
- Missing-value handling using median imputation.
- Random Forest classification.
- Hyperparameter tuning using GridSearchCV.
- Model evaluation using classification metrics.
- Model explainability using permutation importance and SHAP.
- Interactive Streamlit frontend.
- FastAPI prediction API.
- Docker containerization.
- Docker Compose orchestration.
- Google Cloud Run deployment.
- IAM-based authentication between frontend and backend.

---

## 2. System Architecture

The application follows a frontend-backend architecture.

**Prediction workflow:**

1. User enters nine cell measurements through Streamlit.
2. Streamlit sends the input data to the FastAPI prediction endpoint.
3. FastAPI validates the input using Pydantic.
4. The input is converted into a Pandas DataFrame.
5. The trained Random Forest pipeline processes the input.
6. The model generates a classification and probability scores.
7. FastAPI returns the results as JSON.
8. Streamlit displays the prediction and malignant probability.

### Architecture Diagram

```text
                 USER
                  |
                  v
          STREAMLIT FRONTEND
              Port 8501
                  |
                  | HTTP POST
                  v
           FASTAPI BACKEND
              Port 8000
                  |
                  v
          INPUT VALIDATION
              Pydantic
                  |
                  v
          PANDAS DATAFRAME
                  |
                  v
        RANDOM FOREST PIPELINE
                  |
          +-------+-------+
          |               |
          v               v
       PREDICTION      PROBABILITY
          |               |
          +-------+-------+
                  |
                  v
           JSON RESPONSE
                  |
                  v
          STREAMLIT RESULT
```

### Google Cloud Architecture

The application is deployed using two independent Cloud Run services.

- **Frontend:** Public-facing Streamlit service.
- **Backend:** Private FastAPI service.
- **Artifact Registry:** Stores Docker container images.
- **IAM authentication:** Allows the frontend service account to invoke the private backend.

The frontend obtains an identity token from the Google Cloud metadata server when running on Cloud Run.

---

## 3. Dataset Description

**Dataset:** Wisconsin Breast Cancer Original Dataset

**Source:** University of Wisconsin Hospitals, Madison, Wisconsin, USA.

The database was obtained from Dr. William H. Wolberg.

The dataset contains 699 instances and 11 columns, including sample identifiers, nine cell measurements, and class labels.

### Input Features

The following nine features are used by the Machine Learning model:

| Feature | Description |
|---|---|
| Clump Thickness | Thickness of cell clumps |
| Uniformity of Cell Size | Uniformity of cell size |
| Uniformity of Cell Shape | Uniformity of cell shape |
| Marginal Adhesion | Cell marginal adhesion |
| Single Epithelial Cell Size | Epithelial cell size |
| Bare Nuclei | Bare nuclei measurement |
| Bland Chromatin | Bland chromatin measurement |
| Normal Nucleoli | Normal nucleoli measurement |
| Mitoses | Mitoses measurement |

Each feature has values ranging from 1 to 10.

### Target Classes

| Original Class | Encoded Class | Meaning |
|---|---|---|
| 2 | 0 | Benign |
| 4 | 1 | Malignant |

The `Sample_ID` column is excluded from model training.

---

## 4. Data Preprocessing

The following preprocessing operations were performed:

1. Dataset inspection and data type verification.
2. Removal of eight exact duplicate rows.
3. Identification of missing values.
4. Median imputation for missing values in `Bare_Nuclei`.
5. Separation of input features and target variable.
6. Exclusion of `Sample_ID` from model training.
7. Group-aware training and testing split.

### Dataset Summary

| Description | Value |
|---|---:|
| Original records | 699 |
| Exact duplicate rows removed | 8 |
| Records after deduplication | 691 |
| Benign samples | 453 |
| Malignant samples | 238 |
| Missing values in Bare_Nuclei | 16 |
| Input features | 9 |

The preprocessing pipeline uses `SimpleImputer` with median strategy.

The imputation step is included within the trained Machine Learning pipeline to ensure that the same preprocessing is applied during prediction.

### Training and Testing Split

A group-aware split was used to reduce the risk of data leakage associated with repeated sample identifiers.

| Dataset | Samples |
|---|---:|
| Training set | 554 |
| Testing set | 137 |

---

## 5. Machine Learning Model

The primary classification algorithm used in this project is **Random Forest Classifier**.

### Model Configuration

| Parameter | Value |
|---|---|
| Algorithm | Random Forest |
| Number of estimators | 300 |
| Maximum depth | None |
| Minimum samples split | 10 |
| Minimum samples leaf | 1 |
| Hyperparameter tuning | GridSearchCV |
| Missing-value handling | Median imputation |

The trained pipeline combines preprocessing and classification.

### Model Explainability

Model interpretation was explored using:

- Permutation Feature Importance.
- SHAP (SHapley Additive exPlanations).

The strongest feature contributions observed in the analysis included:

1. Bare Nuclei
2. Uniformity of Cell Shape
3. Uniformity of Cell Size

These are model-derived feature importance findings, not evidence of biological causation.

---

## 6. Model Performance

The Random Forest model was evaluated on the held-out test dataset.

### Evaluation Metrics

| Metric | Score |
|---|---:|
| Accuracy | 96.35% |
| Precision | 92.31% |
| Recall | 97.96% |
| F1 Score | 95.05% |
| ROC-AUC | ~0.988 |

### Confusion Matrix

```text
                 Predicted
               Benign  Malignant

Actual Benign     84       4
Actual Malignant   1      48
```

The model achieved a test accuracy of 96.35%.

These results represent performance on this particular test split and should not be interpreted as clinical validation or expected real-world diagnostic accuracy.

---

## 7. Project Structure

```text
Breast_Cancer_ML/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── data/
│   ├── breast-cancer-wisconsin.data
│   └── breast-cancer-wisconsin.names
│
├── models/
│   └── random_forest_pipeline.joblib
│
├── Notebook/
│   ├── 01_data_inspection.ipynb
│   ├── breast-cancer-wisconsin.data
│   ├── breast-cancer-wisconsin.names
│   └── results/
│       └── model_comparison.csv
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## 8. Technologies Used

### Programming and Data Science

- Python
- Pandas
- NumPy
- Scikit-learn
- SciPy
- Joblib
- SHAP

### Frontend and Backend

- Streamlit
- FastAPI
- Pydantic
- Uvicorn
- Requests

### DevOps and Cloud

- Docker
- Docker Compose
- Google Cloud Platform
- Google Artifact Registry
- Google Cloud Run
- Google Cloud IAM

### Development Environment

- Visual Studio Code
- Jupyter Notebook
- PowerShell

---

## 9. Installation and Local Setup

### Prerequisites

Install the following:

- Python 3.11
- Git
- Docker Desktop (for containerized execution)

Clone the repository:

```bash
git clone https://github.com/sreejithdotme/Breast_Cancer_ML.git
```

Navigate into the project directory:

```bash
cd Breast_Cancer_ML
```

### Running the Backend

Create and activate a virtual environment if desired.

Install backend dependencies:

```bash
pip install -r backend/requirements.txt
```

Start the FastAPI server:

```bash
uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI interactive documentation:

```text
http://127.0.0.1:8000/docs
```

### Running the Frontend

Open another terminal.

Install frontend dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

For local development, the frontend uses:

```text
http://127.0.0.1:8000/predict
```

The local application does not require Google Cloud authentication.

---

## 10. Running with Docker Compose

Docker Compose starts the frontend and backend as separate containers.

Build and start the services:

```bash
docker compose up -d --build
```

Check container status:

```bash
docker compose ps
```

Access the application:

| Service | URL |
|---|---|
| Streamlit Frontend | http://localhost:8501 |
| FastAPI Backend | http://localhost:8000 |
| FastAPI Swagger Docs | http://localhost:8000/docs |
| Backend Health Check | http://localhost:8000/health |

### Stop the containers

```bash
docker compose down
```

### Rebuild the application

```bash
docker compose up -d --build
```

Docker Compose uses its internal service network to allow the frontend to communicate with the backend using:

```text
http://backend:8000/predict
```

---

## 11. API Documentation

The FastAPI backend exposes the following endpoints:

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API welcome message |
| GET | `/health` | Health check |
| GET | `/model-info` | Model information |
| POST | `/predict` | Generate prediction |

### Prediction Request

Endpoint:

```text
POST /predict
```

Example JSON request:

```json
{
  "Clump_Thickness": 5,
  "Uniformity_Cell_Size": 1,
  "Uniformity_Cell_Shape": 1,
  "Marginal_Adhesion": 1,
  "Single_Epithelial_Cell_Size": 2,
  "Bare_Nuclei": 1,
  "Bland_Chromatin": 3,
  "Normal_Nucleoli": 1,
  "Mitoses": 1
}
```

### Example Response

```json
{
  "prediction": "Benign",
  "benign_probability": 1.0,
  "malignant_probability": 0.0
}
```

The response probabilities are model outputs and are not medical certainty estimates.

All nine input measurements must be integers between 1 and 10. Invalid inputs are rejected by FastAPI validation.

---

## 12. Google Cloud Deployment

The application was deployed using Google Cloud Platform.

### Cloud Services Used

| Service | Purpose |
|---|---|
| Google Artifact Registry | Docker image storage |
| Google Cloud Run | Frontend hosting |
| Google Cloud Run | Backend hosting |
| Google Cloud IAM | Service authentication |

### Deployment Architecture

The frontend and backend run as independent Cloud Run services.

The frontend is configured to obtain a Google identity token and use it when calling the private backend.

The backend allows invocation by the dedicated frontend service account through the `roles/run.invoker` permission.

### Deployment Configuration

| Configuration | Value |
|---|---|
| GCP Region | asia-south1 |
| Frontend port | 8501 |
| Backend port | 8000 |
| CPU | 1 |
| Memory | 1 GiB |
| Minimum instances | 0 |
| Maximum instances | 2 |
| Billing | Request-based |

Container images are stored in Google Artifact Registry.

---

## 13. Limitations

- The project uses a historical breast cancer dataset.
- The dataset is relatively small compared with modern medical imaging and genomic datasets.
- Model performance depends on the dataset and evaluation split.
- The model has not undergone clinical validation.
- Predicted probabilities should not be interpreted as medical certainty.
- The application is intended for educational and demonstration purposes only.

---

## 14. Future Improvements

Potential future development includes:

- Additional model comparison and validation.
- Improved model monitoring.
- Expanded model explainability.
- Automated testing and CI/CD integration.
- Enhanced frontend visualizations.
- Retrieval-Augmented Generation (RAG) assistant for research document Q&A.
- Improved deployment monitoring and logging.

---

## 15. Dataset Attribution and References

The Wisconsin Breast Cancer Original Database was obtained from the University of Wisconsin Hospitals, Madison, Wisconsin, USA, through Dr. William H. Wolberg.

**Dataset acknowledgement:**

William H. Wolberg, University of Wisconsin Hospitals, Madison, Wisconsin, USA. Dataset donor: Olvi Mangasarian.

**Research reference:**

Wolberg, W. H., & Mangasarian, O. L. (1990). Multisurface method of pattern separation for medical diagnosis applied to breast cytology. *Proceedings of the National Academy of Sciences of the United States of America*, 87, 9193–9196.

Dataset documentation: `data/breast-cancer-wisconsin.names`

---

## 16. Application Screenshots

The following screenshots show the application's interface, prediction workflow, API documentation, container setup, and cloud deployment.

### Streamlit Application Interface

![Streamlit Application Interface](screenshots/streamlit-interface.png)

The main Streamlit interface where users can enter the nine cell measurements and view information about the trained Random Forest model and its evaluation metrics.

### Breast Cancer Prediction Results

**Malignant prediction**

![Malignant Prediction Result](screenshots/prediction-result-malignant.png)

Example output in which the model classifies the entered cell measurements as **Malignant**, with a displayed malignant probability of 93.05%.

**Benign prediction**

![Benign Prediction Result](screenshots/prediction-result-benign.png)

Example output in which the model classifies the entered cell measurements as **Benign**, with a displayed malignant probability of 28.83%.

### FastAPI Swagger Documentation

![FastAPI Swagger Documentation](screenshots/fastapi-swagger.png)

The FastAPI Swagger UI displays the available API endpoints and the `/predict` request body, allowing the prediction endpoint to be explored and tested.

### Docker Containers

![Docker Containers](screenshots/docker-containers.png)

Docker Desktop showing the project containers, including the Streamlit frontend container and its exposed application port.

### Google Cloud Run Deployment

![Google Cloud Run Services](screenshots/gcp-cloud-run.png)

Google Cloud Run showing the separately deployed frontend and backend services for the application.

---

## Author

Developed as an end-to-end Machine Learning portfolio project.

**GitHub Repository:**  
https://github.com/sreejithdotme/Breast_Cancer_ML

